"""
SMART AUTOMATION ASSISTANT
Author: Kamalika.S
Description:
A standalone Python automation assistant that:
- Organizes files automatically
- Monitors system health
- Sends desktop notifications
- Creates backups
- Runs continuously in background
"""

import os
import shutil
import time
import psutil
from datetime import datetime
from plyer import notification

# ================= CONFIGURATION ================= #

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
BACKUP_PATH = os.path.expanduser("~/Desktop/Backup")
LOG_FILE = "automation_log.txt"

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# ================= LOGGING ================= #

def log_activity(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ================= NOTIFICATIONS ================= #

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

# ================= FILE ORGANIZER ================= #

def organize_downloads():
    if not os.path.exists(DOWNLOADS_PATH):
        return

    for file in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    folder_path = os.path.join(DOWNLOADS_PATH, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    log_activity(f"Moved {file} → {folder}")
                    break

# ================= SYSTEM MONITOR ================= #

def monitor_system():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()

    status = f"CPU: {cpu}% | RAM: {ram}%"

    if battery:
        status += f" | Battery: {battery.percent}%"

    log_activity(status)

    if cpu > 85 or ram > 85:
        notify("System Alert", "High system usage detected!")

# ================= BACKUP SYSTEM ================= #

def backup_folder(source):
    if not os.path.exists(source):
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_PATH, f"backup_{timestamp}")
    shutil.copytree(source, dest)
    log_activity(f"Backup created: {dest}")
    notify("Backup Complete", "Your files are safely backed up")

# ================= MAIN AUTOMATION LOOP ================= #

def automation_loop():
    notify("Automation Started", "Smart Assistant is running")
    log_activity("Automation Assistant Started")

    while True:
        try:
            organize_downloads()
            monitor_system()

            # Backup Documents every cycle
            documents_path = os.path.expanduser("~/Documents")
            backup_folder(documents_path)

            time.sleep(300)  # runs every 5 minutes

        except Exception as e:
            log_activity(f"Error: {e}")
            time.sleep(60)

# ================= ENTRY POINT ================= #

if __name__ == "__main__":
    print("SMART AUTOMATION ASSISTANT RUNNING...")
    print("Press CTRL + C to stop\n")
    automation_loop()
