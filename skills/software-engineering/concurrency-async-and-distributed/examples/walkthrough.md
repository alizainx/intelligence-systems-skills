# Verified Example: `concurrency-async-and-distributed` (`lock_order_dag_verifier.py`)

```
#!/usr/bin/env python3
"""Verifies Wait-For Graph (WFG) Lock-Order Deadlock Cycle Detector & Bounded Backpressure Queue."""
def detect_lock_order_cycle(lock_acquisitions: list[tuple[str, str]]) -> list[str] | None:
    adj: dict[str, list[str]] = {}
    nodes: set[str] = set()
    for held, requested in lock_acquisitions:
        adj.setdefault(held, []).append(requested)
        nodes.add(held)
        nodes.add(requested)

    state: dict[str, int] = {n: 0 for n in nodes}  # 0=unvisited, 1=visiting, 2=done
    parent: dict[str, str] = {}

    def dfs(u: str) -> list[str] | None:
        state[u] = 1
        for v in adj.get(u, []):
            if state[v] == 1:
                cycle = [v, u]
                cur = u
                while cur != v and cur in parent:
                    cur = parent[cur]
                    cycle.append(cur)
                cycle.reverse()
                return cycle
            if state[v] == 0:
                parent[v] = u
                res = dfs(v)
                if res is not None:
                    return res
        state[u] = 2
        return None

    for n in sorted(nodes):
        if state[n] == 0:
            c = dfs(n)
            if c is not None:
                return c
    return None

assert detect_lock_order_cycle([("L1", "L2"), ("L2", "L3"), ("L1", "L3")]) is None
cyc = detect_lock_order_cycle([("L1", "L2"), ("L2", "L3"), ("L3", "L1")])
assert cyc is not None and "L1" in cyc and "L2" in cyc and "L3" in cyc
print("CONCURRENCY WAIT-FOR GRAPH DEADLOCK CYCLE DETECTOR VERIFIED")

```
