# CloudOps Sentinel

A compact Python-based DevOps toolkit demonstrating monitoring, alerting, packaging, and cloud automation.
This repo is purpose-built to be a GitHub portfolio project and LinkedIn demo.

## What's included
- Flask API exposing `/health` and `/metrics`
- `metrics` wrapper using psutil (falls back to dummy values for CI)
- Slack & email alerts helpers
- Scheduler to run periodic checks
- S3 upload helper for log backups
- Dockerfile + docker-compose example
- GitHub Actions CI with pytest + Trivy security scan

## Quickstart (local dev)
```bash
# create venv and install
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run the API
python -m cloudops_sentinel.api
# open http://localhost:5000/metrics
```

## Docker
```bash
docker build -t cloudops-sentinel:local .
docker run -p 5000:5000 cloudops-sentinel:local
```

## Running the scheduler locally
```bash
python -c "from cloudops_sentinel import scheduler; scheduler.run_loop(60)"
```

## Notes for presenters
- Show `/metrics` output (curl) as demo of monitoring.
- Show GitHub Actions run + Trivy scan results for security story.
- Add a short recording/GIF to your LinkedIn post: show alert firing, S3 upload, and CI pipeline.