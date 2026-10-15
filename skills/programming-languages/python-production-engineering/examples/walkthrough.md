# Nontrivial Implementation & Multi-File Engineering Walkthrough: `python-production-engineering`

- **Target File**: `examples/strict_async_rate_limiter.py`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
from __future__ import annotations
import asyncio
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True, slots=True)
class QuotaConfig:
    capacity: int
    refill_per_sec: float
    def __post_init__(self) -> None:
        if self.capacity <= 0 or self.refill_per_sec <= 0.0:
            raise ValueError("capacity and refill_per_sec must be positive")

class AsyncTokenBucket:
    def __init__(self, config: QuotaConfig) -> None:
        self._cfg: Final[QuotaConfig] = config
        self._tokens: float = float(config.capacity)
        self._last_ts: float = 0.0

    def try_consume(self, now: float, requested: int = 1) -> bool:
        if requested <= 0 or requested > self._cfg.capacity:
            raise ValueError("invalid token request")
        if now < self._last_ts:
            raise ValueError("non-monotonic clock")
        elapsed = now - self._last_ts
        self._last_ts = now
        self._tokens = min(float(self._cfg.capacity), self._tokens + elapsed * self._cfg.refill_per_sec)
        if self._tokens >= float(requested):
            self._tokens -= float(requested)
            return True
        return False

```
