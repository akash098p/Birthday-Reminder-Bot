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

- 🎂 **Automatic Birthday Detection** — Checks your birthday database every day.
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

Before implementing the cloud code, you must establish an authenticated Telegram bot.

1. **Initialize the Bot**:
   * Open Telegram and search for **@BotFather**.
   * Send `/newbot`.
   * Follow the setup wizard and create your bot username.
   * Copy the generated **HTTP API Token** and keep it private.

2. **Start Your Bot**:
   * Search for your newly created bot in Telegram.
   * Click **Start**.
   * This is required so the bot can communicate with you.

3. **Retrieve Your Chat ID**:
   * Search for **@userinfobot** in Telegram.
   * Click Start.
   * Copy the numeric **Id** value.

---

### Phase 2: Codebase Implementation

#### File 1: The Birthday Database (`birthdays.csv`)

```csv
Name,Birthdate
Subrata Bera,2006-03-26
Nisha Roy,2005-09-01
Ajay Ghorai,2004-01-04
Raju Maity,2003-04-03
```

#### File 2: The Logic Processing Engine (`reminder.py`)

This script reads the birthday database, checks upcoming birthdays, and sends the appropriate Telegram notification.

#### File 3: The GitHub Actions Workflow (`.github/workflows/main.yml`)

The workflow executes automatically every day and can also be started manually using **workflow_dispatch**.

---

### Phase 3: Configure GitHub Secrets

Store your Telegram credentials securely in GitHub instead of placing them directly inside the source code.

1. Open the repository's **Settings**.
2. Go to **Secrets and variables → Actions**.
3. Create these repository secrets:

   * **`TELEGRAM_TOKEN`** — Your BotFather API token.
   * **`TELEGRAM_CHAT_ID`** — Your Telegram chat ID.

> ⚠️ Never commit your Telegram token directly into the repository.

---

## 🧪 Pipeline Diagnostics & Validation

### Standard Gateway Verification

If the workflow completes successfully but no Telegram notification arrives, verify that your bot has been started and that the configured chat ID is correct.

You can also manually trigger the workflow from the repository's **Actions** tab using **Run workflow**.

### GitHub Actions Logs

To inspect the automation:

1. Open the repository's **Actions** tab.
2. Select the **Birthday Tracker Engine** workflow.
3. Open the latest workflow run.
4. Expand **Trigger Notification System** to inspect the execution logs.

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
