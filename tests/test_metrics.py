from cloudops_sentinel.metrics import snapshot

def test_snapshot_keys():
    s = snapshot()
    assert 'cpu_percent' in s and 'mem_percent' in s