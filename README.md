CloudOps Sentinel 🚀

A compact Python-based DevOps toolkit for monitoring, alerting, packaging, and cloud automation.
Built to showcase modern DevOps practices — CI/CD, containerization, security, and cloud integration — in a lightweight, portfolio-ready project.

Architecture
+-----------+       +----------------+       +---------------+
| Flask API | --->  | Metrics (psutil| --->  | Scheduler     |
| /health   |       |  / dummy)      |       | Periodic Jobs |
+-----------+       +----------------+       +---------------+
                        |         |
                        v         v
                 +-----------+   +-----------+
                 | Alerting  |   | Log Backup|
                 | Slack/Email|  |   S3      |
                 +-----------+   +-----------+

🔹 Features

Flask API → /health & /metrics endpoints

Metrics Collector → psutil w/ CI-safe fallbacks

Alerting → Slack & email notifications

Scheduler → Automated health checks & jobs

🔹 DevOps Integrations

Containerization → Docker + Compose

CI/CD → GitHub Actions (tests, builds, Trivy scans)

Security → Automated vuln scanning

Portfolio Ready → End-to-end cloud monitoring workflow

🔹 Quick Start
          
# With Docker (recommended)
docker-compose up

# Or run locally
python app.py

🔹 Tech Stack

Python 3.x • Flask • psutil • Docker • GitHub Actions • Trivy • Slack • AWS S3

🔹 License

MIT License • Open Source


Log Backup → Uploads securely to S3
