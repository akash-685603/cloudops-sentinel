import os
import time
import json
import psutil
import requests

# === Configuration ===
REGION = "us"  # change to "eu" if your account is EU
URL = "https://metric-api.newrelic.com/metric/v1"
SLEEP_INTERVAL = 5  # seconds between metrics sends
HOST_NAME = "CloudOps Sentinel"  # custom host name

def get_insert_key():
    """Fetch API key, raise error only when needed (not at import)."""
    insert_key = os.getenv("NEW_RELIC_INSERT_KEY")
    if not insert_key:
        raise ValueError("Set NEW_RELIC_INSERT_KEY environment variable!")
    return insert_key

# === Function to gather system metrics ===
def gather_metrics():
    timestamp = int(time.time())
    return [
        {
            "common": {"attributes": {"host": HOST_NAME}},
            "metrics": [
                {
                    "name": "Custom/CPU/Percent",
                    "type": "gauge",
                    "value": psutil.cpu_percent(interval=1),
                    "timestamp": timestamp,
                },
                {
                    "name": "Custom/Memory/UsedPercent",
                    "type": "gauge",
                    "value": psutil.virtual_memory().percent,
                    "timestamp": timestamp,
                },
                {
                    "name": "Custom/Disk/UsedPercent",
                    "type": "gauge",
                    "value": psutil.disk_usage("/").percent,
                    "timestamp": timestamp,
                },
            ],
        }
    ]

# === Function to send metrics to New Relic ===
def send_metrics():
    payload = gather_metrics()
    headers = {
        "Api-Key": get_insert_key(),
        "Content-Type": "application/json",
    }
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        if response.status_code in (200, 202):
            print(f"Metrics sent successfully! Status={response.status_code}, Response={response.text}")
        else:
            print(f"Failed to send metrics: Status={response.status_code}, Response={response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending metrics: {e}")

# === Main loop ===
if __name__ == "__main__":
    print("Starting system metrics reporting to New Relic...")
    while True:
        send_metrics()
        time.sleep(SLEEP_INTERVAL)
