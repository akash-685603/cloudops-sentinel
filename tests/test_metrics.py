import os
from cloudops_sentinel import metrics

def test_gather_metrics_structure(monkeypatch):
    # Patch API key for test
    monkeypatch.setenv("NEW_RELIC_INSERT_KEY", "dummy-key")

    result = metrics.gather_metrics()
    assert isinstance(result, list)
    assert "metrics" in result[0]
