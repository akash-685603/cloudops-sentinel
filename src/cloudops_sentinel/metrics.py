"""metrics.py

Provides a small wrapper around psutil for system metrics.
Falls back to dummy values if psutil is not installed so tests and CI can run
in minimal environments.
"""
try:
    import psutil
except Exception:  # pragma: no cover - fallback when psutil unavailable
    psutil = None

def snapshot() -> dict:
    """Return a dict with basic system metrics.

    cpu_percent: float
    mem_percent: float
    """
    if psutil:
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
    else:
        # fallback dummy values so tests don't fail in minimal CI
        cpu = 0.5
        mem = 1.0
    return {
        "cpu_percent": cpu,
        "mem_percent": mem,
    }