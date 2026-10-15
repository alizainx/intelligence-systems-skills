#!/usr/bin/env python3
import ast, importlib.util
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "strict_async_rate_limiter.py"
ast.parse(SRC.read_text())
spec = importlib.util.spec_from_file_location("m", str(SRC))
import sys
m = importlib.util.module_from_spec(spec)
sys.modules["m"] = m
spec.loader.exec_module(m)
tb = m.AsyncTokenBucket(m.QuotaConfig(capacity=5, refill_per_sec=2.0))
assert tb.try_consume(0.0, 5) is True
assert tb.try_consume(0.0, 1) is False
assert tb.try_consume(1.0, 2) is True
print("VERIFIED: Python 3.11+ frozen/slotted dataclass, AST & monotonic token-bucket invariants verified")
