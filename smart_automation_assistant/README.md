# Smart Automation Assistant (Python)

A standalone Python-based automation assistant that runs in the background and performs useful desktop automation tasks such as file organization, system monitoring, notifications, and backups.

This project demonstrates real-world Python automation skills and is suitable for portfolios, demos, and practical use.

---

## Features

- **Automatic File Organization**
  - Organizes files in the `Downloads` folder into categories like Images, Documents, Videos, Music, and Archives.

- **System Health Monitoring**
  - Monitors CPU usage, RAM usage, and battery level.
  - Sends alerts when system usage crosses safe thresholds.

- **Desktop Notifications**
  - Displays real-time notifications for alerts, backups, and automation status.

- **Automatic Backup**
  - Periodically creates timestamped backups of the `Documents` folder.

- **Activity Logging**
  - Logs all actions and system status into a log file (`automation_log.txt`).

- **Continuous Background Execution**
  - Runs automatically every 5 minutes without user interaction.

---

##  Technologies Used

- Python 3
- `psutil` – system monitoring
- `plyer` – desktop notifications
- Built-in Python libraries:
  - `os`
  - `shutil`
  - `time`
  - `datetime`

---

##  Installation

### Clone or Download the Project
```bash
git clone <your-repo-url>
cd smart-automation-assistant
````

### Install Required Libraries

```bash
pip install psutil plyer
```

---

## How to Run

```bash
python smart_automation_assistant.py
```

Once started:

* The assistant runs continuously in the background
* Press **CTRL + C** to stop execution

---

## Folder Structure (After Running)

```text
Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Archives/

Desktop/
└── Backup/
    ├── backup_20240218_103210/
    ├── backup_20240218_104510/
```

---

## Log File

All activities are logged in:

```
automation_log.txt
```

Example log entry:

```
[2026-02-18 10:32:10] Moved resume.pdf → Documents
[2026-02-18 10:35:00] CPU: 42% | RAM: 61% | Battery: 85%
```

---

##  System Alerts

* Notification is triggered when:

  * CPU usage > 85%
  * RAM usage > 85%

---


