import os
import csv
from datetime import datetime

LOG_FILE = "logs/campaign_log.csv"

def log_generation(campaign_name, prompt, image_path):
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "campaign_name", "prompt", "image_path"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            campaign_name,
            prompt,
            image_path
        ])