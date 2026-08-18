<div align="center">

# 🎂 Automated Birthday Tracker & Notification Engine

### ✨ Smart • Automated • Zero-Maintenance Birthday Notifications

<p>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-Automated-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge&logo=statuspage&logoColor=white" alt="Status Active"/>
  <img src="https://img.shields.io/badge/Automation-Daily-8B5CF6?style=for-the-badge&logo=githubactions&logoColor=white" alt="Daily Automation"/>
  <img src="https://img.shields.io/badge/License-Open_Source-F59E0B?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="Open Source"/>
</p>

</div>

A zero-maintenance birthday tracking engine built using Python and GitHub Actions. The system automatically checks birthdays and sends customized Telegram notifications **1 day before** a birthday and on the **exact day**.

---

## ✨ Features

- 🎂 **Automatic Birthday Detection** — Checks the birthday database every day.
- 📅 **Advance Reminder** — Sends a notification one day before the birthday.
- 🎉 **Exact-Day Notification** — Sends a notification on the actual birthday.
- 🤖 **Telegram Integration** — Delivers reminders directly through Telegram.
- ⚙️ **GitHub Actions Automation** — Runs automatically in the cloud without requiring your computer to stay online.
- 🔐 **Secure Secrets** — Telegram credentials are stored securely using GitHub Actions Secrets.
- ☁️ **Zero Maintenance** — No local server or continuous hosting required.
- ▶️ **Manual Execution** — Workflow can also be triggered manually from GitHub Actions.

---

## 🔄 How It Works

```text
┌───────────────────┐
│   birthdays.csv   │
│  Birthday Data    │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│  GitHub Actions   │
│  Daily Scheduler  │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│    reminder.py    │
│ Birthday Detection│
└─────────┬─────────┘
          ↓
┌───────────────────┐
│  Telegram Bot API │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ 📱 Notification   │
└───────────────────┘
```

---

## 🛠 Project Architecture & Data Flow

```text
📁 Birthday-Reminder-Bot

├── 📄 birthdays.csv
├── 📄 reminder.py
└── 📁 .github/workflows/
                        └── 📄 main.yml
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python 3.11** | Birthday detection and notification logic |
| ⚙️ **GitHub Actions** | Cloud-based daily automation |
| ✈️ **Telegram Bot API** | Birthday notification delivery |
| 📄 **CSV** | Simple birthday data storage |
| ⏰ **Cron** | Daily workflow scheduling |
| 🔐 **GitHub Secrets** | Secure credential management |

---

## 📸 Demo

<p align="center">
  <!-- Add your Telegram notification screenshot here -->
  <img src="" width="450" alt="Birthday Reminder Bot Demo"/>
</p>

---

## 📋 Comprehensive Setup Roadmap

### Phase 1: Provisioning Your Telegram Notification Channel
Before implementing cloud code, you must establish an authenticated endpoint on Telegram's network gateway.

1. **Initialize the Bot Architecture**:
   * Open Telegram, search for the official account **@BotFather**, and initiate a chat.
   * Send the command `/newbot`.
   * Follow the conversational wizard to define a display name and a unique system username ending strictly in `_bot` (e.g., `MyReminders_bot`).
   * Copy the generated alphanumeric access string labeled **HTTP API Token**. Keep this hidden.

2. **Verify User Communication Channel Access**:
   * Search for your newly created bot username in Telegram and click **Start**. 
   * *Critical*: If you skip this, the Telegram API gateway will block incoming scripts with a `400 Bad Request: chat not found` protection error.

3. **Retrieve Your Encrypted Destination Chat ID**:
   * Search for **@userinfobot** in Telegram and click start.
   * Instantly capture the numeric string labeled **Id** (e.g., `513742847`). This is your direct inbox route on the Telegram system network.

---

### Phase 2: Codebase Implementation
Create or update the three essential project files inside your private repository precisely as outlined below.

#### File 1: The Input Database Matrix (`birthdays.csv`)
This file houses your core dates. Ensure all rows match the standard formatting below. Do not add spacing around commas.

```csv
Name,Birthdate
Subrata Bera,2006-03-26
Nisha Roy,2005-09-01
Ajay Ghorai,2004-01-04
Raju Maity,2003-04-03
```

#### File 2: The Logic Processing Engine (`reminder.py`)
This script executes datetime conversions, filters the dates, and strips hidden system characters like carriage returns (`\r`).


#### File 3: The CRON Orchestration Blueprint (`.github/workflows/main.yml`)
The workflow executes automatically every day and can also be started manually using **workflow_dispatch**.


---

### Phase 3: Configure GitHub Secrets

Store your Telegram credentials securely in GitHub instead of placing them directly inside the source code.

1. Open the repository's **Settings**.
2. Go to **Secrets and variables → Actions**.
3. Create these repository secrets:
   

      * **`TELEGRAM_TOKEN`**: Paste your full API string generated by BotFather. Make sure there are no brackets (`<` or `>`) or trailing spaces.
   * **`TELEGRAM_CHAT_ID`**: Paste your numeric identifier sequence provided by userinfobot.
  

> ⚠️ Never commit your Telegram token directly into the repository.

---

## 🧪 Pipeline Diagnostics & Validation Workflows

### Standard Gateway Verification
If your pipeline executes with a green checkmark but no transmission reaches your handset, you can isolate network delivery bottlenecks by running a manual URL execution check.

Clear your web browser's URL address field entirely, paste the template below, replace the placeholder text with your parameters, and press enter:

```text
https://api.telegram.org/bot[YOUR_TELEGRAM_TOKEN]/sendMessage?chat_id=[YOUR_TELEGRAM_CHAT_ID]&text=System_Diagnostics_Pass
```

* **Expected Output**: The page should render `{"ok":true,"result":{...}}`, and your device will instantly display the alert message.
* **Error Response 401**: Your token contains a typo or has expired. Request a new one via BotFather.
* **Error Response 400**: Your chat ID is incorrect, or you have not yet sent a manual message to start your bot channel.

### Deciphering GitHub Action Terminal Outputs
To verify tracking activity, open your repository's **Actions** tab, choose your workflow execution, click **`execute-pipeline`**, and expand the step log titled **`Trigger Notification System`**.

* **`Running privacy engine scan...`**: Indicates the runtime server initialized correctly and read your current system calendar timezone.
* **`Notification queued (Advance): [Name]`**: The logic discovered a match scheduled for tomorrow. The alert has been sent.
* **`Notification queued (Exact Day): [Name]`**: The logic discovered an anniversary matching today's date. The menu interface containing your three custom message options has been dispatched to Telegram.

---

## 🔐 Security

This project is designed to keep sensitive Telegram credentials outside the source code by using **GitHub Actions Secrets**.

Never publish:

- Telegram Bot API tokens
- Private credentials
- Personal access tokens
- Sensitive chat identifiers

---

## 💡 Why This Project?

This project demonstrates how a small Python application can be transformed into a fully automated cloud workflow using GitHub Actions. It combines **Python automation, scheduled workflows, API integration, secure secrets management, and Telegram notifications** into a practical real-world project.

---

## 🚀 Future Improvements

- 🎨 Custom notification templates
- 👥 Support for multiple Telegram users
- 🌍 Time-zone aware birthday notifications
- 📊 Web-based birthday management dashboard
- 🗓️ Calendar integration
- 🧠 Smart personalized birthday messages

---

## 🧑‍💻 Developer

**Akash Pramanik**

<p>
  <strong>For questions or support: </strong>
<a href="https://instagram.com/akash.098p" target="_blank">
  <img src="https://img.shields.io/badge/akash.098p-E4405F?style=flat&logo=instagram&logoColor=white"/>
</a>

<a href="mailto:akashpramanik098@gmail.com">
  <img src="https://img.shields.io/badge/akashpramanik422%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white"/>
</a>
</p>
