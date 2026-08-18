import csv
import os
import requests
from datetime import datetime, timedelta

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_alert(alert_text):
    # FORCE CORRECT PATHWAY
    gateway_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": alert_text, "parse_mode": "Markdown"}
    try:
        api_response = requests.post(gateway_url, json=payload, timeout=10)
        if api_response.status_code != 200:
            print(f"Telegram API Error: {api_response.text}")
    except Exception as e:
        print(f"Network error sending telegram alert: {e}")

def parse_flexible_date(date_str):
    clean_str = date_str.replace("/", "-").replace(".", "-").replace(",", "-").strip()
    for date_format in ("%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(clean_str, date_format).date()
        except ValueError:
            continue
    raise ValueError(f"Unknown date structure: {date_str}")

def evaluate_calendar():
    # FIX: Force alignment to Indian Standard Time (UTC + 5:30) regardless of GitHub server location
    utc_now = datetime.utcnow()
    ist_now = utc_now + timedelta(hours=5, minutes=30)
    
    current_date = ist_now.date()
    target_tomorrow = current_date + timedelta(days=1)
    print(f"Running engine scan for Today: {current_date} | Tomorrow: {target_tomorrow}")
    
    with open("birthdays.csv", mode="r", encoding="utf-8-sig") as target_file:
        reader = csv.reader(target_file)
        headers = [h.strip().lower() for h in next(reader)]
        
        name_idx = headers.index("name") if "name" in headers else 0
        bday_idx = headers.index("birthdate") if "birthdate" in headers else 1

        for row in reader:
            if not row or len(row) <= max(name_idx, bday_idx):
                continue
            
            name_val = row[name_idx].strip()
            raw_date_val = row[bday_idx].strip()
            
            try:
                original_bday = parse_flexible_date(raw_date_val)
                
                # FIX: Match based on Month and Day directly to handle year rolling boundaries cleanly
                # Condition 1: 1 Day Advance Reminder
                if original_bday.month == target_tomorrow.month and original_bday.day == target_tomorrow.day:
                    turning_age = target_tomorrow.year - original_bday.year  # FIX: Uses tomorrow's year context
                    send_alert(f"⏰ *Advance Reminder:* {name_val}'s birthday is tomorrow! They are turning *{turning_age}*.")
                    print(f"Notification queued (Advance): {name_val}")
                
                # Condition 2: Exact Birthday Match Reminder (Isolated via elif)
                elif original_bday.month == current_date.month and original_bday.day == current_date.day:
                    turning_age = current_date.year - original_bday.year   # Uses today's year context
                    send_alert(f"🎉 *Birthday Alert:* Today is {name_val}'s birthday! They are turning *{turning_age}*! 🎂")
                    print(f"Notification queued (Exact Day): {name_val}")
                    
            except Exception as error:
                print(f"Skipping row for [{name_val}] due to error: {error}")

if __name__ == "__main__":
    if TOKEN and CHAT_ID:
        evaluate_calendar()
    else:
        print("Fatal Execution Error: Environment Secrets Undefined.")
