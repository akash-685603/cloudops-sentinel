import os
import psutil
import requests
import time

# Get Insert Key from env
insert_key = os.getenv("NEW_RELIC_INSERT_KEY")

url = "https://metric-api.newrelic.com/metric/v1"
headers = {
    "Api-Key": insert_key,
    "Content-Type": "application/json"
}

while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    payload = [
        {
            "metrics": [
                {
                    "name": "Custom/CPU/Percent",
                    "type": "gauge",
                    "value": cpu,
                    "timestamp": int(time.time())
                },
                {
                    "name": "Custom/Memory/Percent",
                    "type": "gauge",
                    "value": mem,
                    "timestamp": int(time.time())
                }
            ]
        }
    ]
    response = requests.post(url, headers=headers, json=payload)
    print(f"Sent metrics: CPU={cpu}, MEM={mem}, status={response.status_code}")
    time.sleep(5)
