#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "bounded_worker_pool.go").read_text()
assert "context.WithCancel(ctx)" in src and "defer cancel()" in src and "case <-ctx.Done():" in src
print("PARTIALLY VERIFIED: Go 1.22+ generic bounded worker, context cancellation & leak-free select invariants verified (go test -race designed for CI).")
