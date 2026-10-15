from __future__ import annotations
import ast
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True, slots=True)
class BoundedTokenBucket:
    capacity: float
    refill_rate_per_sec: float

    def __post_init__(self) -> None:
        if self.capacity <= 0.0 or self.refill_rate_per_sec <= 0.0:
            raise ValueError("capacity and refill_rate_per_sec must be > 0")

    def step(self, current_tokens: float, elapsed_sec: float, requested: float) -> tuple[bool, float]:
        if elapsed_sec < 0.0 or requested < 0.0:
            raise ValueError("elapsed_sec and requested must be >= 0")
        available = min(self.capacity, current_tokens + elapsed_sec * self.refill_rate_per_sec)
        if requested <= available:
            return (True, available - requested)
        return (False, available)
