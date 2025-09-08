"""alerts.py

Helpers to send Slack or email alerts. Minimal and easy to extend.
Secrets are read from environment variables in .env or the OS environment.
"""
import os
import logging

_logger = logging.getLogger(__name__)

def slack_alert(text: str):
    import requests
    webhook = os.getenv('SLACK_WEBHOOK')
    if not webhook:
        _logger.info('SLACK_WEBHOOK not set; skipping slack alert')
        return
    try:
        requests.post(webhook, json={'text': text}, timeout=5)
    except Exception as e:
        _logger.exception('Failed to send slack alert: %s', e)

def email_alert(subject: str, body: str):
    import smtplib
    from email.mime.text import MIMEText

    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')
    mail_from = os.getenv('MAIL_FROM')
    mail_to = os.getenv('MAIL_TO')

    if not all([smtp_host, smtp_user, smtp_pass, mail_from, mail_to]):
        _logger.info('SMTP details incomplete; skipping email alert')
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to

    with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as s:
        s.starttls()
        s.login(smtp_user, smtp_pass)
        s.send_message(msg)