#!/usr/bin/env python3
import ast
SRC = 'from __future__ import annotations\nimport ast\nfrom dataclasses import dataclass\nfrom typing import Final\n\n@dataclass(frozen=True, slots=True)\nclass BoundedTokenBucket:\n    capacity: float\n    refill_rate_per_sec: float\n\n    def __post_init__(self) -> None:\n        if self.capacity <= 0.0 or self.refill_rate_per_sec <= 0.0:\n            raise ValueError("capacity and refill_rate_per_sec must be > 0")\n\n    def step(self, current_tokens: float, elapsed_sec: float, requested: float) -> tuple[bool, float]:\n        if elapsed_sec < 0.0 or requested < 0.0:\n            raise ValueError("elapsed_sec and requested must be >= 0")\n        available = min(self.capacity, current_tokens + elapsed_sec * self.refill_rate_per_sec)\n        if requested <= available:\n            return (True, available - requested)\n        return (False, available)\n'
tree = ast.parse(SRC)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        assert node.returns is not None, f"Missing return annotation on {node.name}"
ns = {}
exec(SRC, ns)
tb = ns["BoundedTokenBucket"](capacity=10.0, refill_rate_per_sec=2.0)
ok, rem = tb.step(5.0, 2.0, 8.0)
assert ok and abs(rem - 1.0) < 1e-12
ok2, rem2 = tb.step(rem, 0.5, 5.0)
assert not ok2 and abs(rem2 - 2.0) < 1e-12
print("PYTHON 3.11 PRODUCTION ENGINEERING AST & TOKEN BUCKET VERIFIED")
