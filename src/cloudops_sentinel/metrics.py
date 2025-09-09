"""
metrics.py

Provides a small wrapper around psutil for system metrics.
Falls back to dummy values if psutil is not installed so tests and CI can run
in minimal environments.
Also integrates with New Relic (optional) for custom metrics reporting.
"""

import os
import time

try:
    import psutil
except Exception:  # pragma: no cover - fallback when psutil unavailable
    psutil = None

# Optional New Relic integration
harvester = None
try:
    from newrelic_telemetry_sdk import Harvester, GaugeMetric
    harvester = Harvester()
except ImportError:
    harvester = None

def snapshot() -> dict:
    """Return a dict with basic system metrics and optionally push to New Relic."""
    if psutil:
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
    else:
        cpu = 0.5
        mem = 1.0

    metrics = {"cpu_percent": cpu, "mem_percent": mem}

    # Push to New Relic if enabled
    if harvester:
        try:
            cpu_metric = GaugeMetric("cloudops.cpu.percent", cpu)
            mem_metric = GaugeMetric("cloudops.mem.percent", mem)
            harvester.add(cpu_metric)
            harvester.add(mem_metric)
            # Here is where we pass the key
            harvester.harvest(api_key=os.getenv("NEW_RELIC_INSERT_KEY"))
        except Exception as e:
            print(f"[WARN] New Relic push failed: {e}")

    return metrics

import time

if __name__ == "__main__":
    while True:
        print(snapshot())
        time.sleep(10)  # push every 10 seconds
