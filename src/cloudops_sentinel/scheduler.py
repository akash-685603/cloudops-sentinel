"""scheduler.py

Simple scheduler that checks metrics periodically and fires alerts.
Uses schedule (lightweight) for demonstration.
"""
import os, time
from .metrics import snapshot
from .alerts import slack_alert, email_alert

CPU_THRESHOLD = float(os.getenv('CPU_ALERT_THRESHOLD', '85'))
MEM_THRESHOLD = float(os.getenv('MEM_ALERT_THRESHOLD', '90'))

def check_and_alert():
    m = snapshot()
    cpu = m.get('cpu_percent', 0)
    mem = m.get('mem_percent', 0)
    msg_parts = []
    if cpu > CPU_THRESHOLD:
        msg_parts.append(f'CPU high: {cpu}% > {CPU_THRESHOLD}%')
    if mem > MEM_THRESHOLD:
        msg_parts.append(f'MEM high: {mem}% > {MEM_THRESHOLD}%')
    if msg_parts:
        msg = ' | '.join(msg_parts)
        slack_alert(':warning: ' + msg)
        if os.getenv('ENABLE_EMAIL', 'false').lower() in ('1', 'true', 'yes'):
            email_alert('CloudOps Sentinel Alert', msg)

def run_loop(poll_seconds: int = 60):
    try:
        import schedule
    except Exception:
        raise RuntimeError('schedule library not installed. pip install schedule')
    schedule.every(poll_seconds).seconds.do(check_and_alert)
    while True:
        schedule.run_pending()
        time.sleep(1)