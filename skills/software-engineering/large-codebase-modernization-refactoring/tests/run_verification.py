#!/usr/bin/env python3
"""Verifies Golden-Master Characterization Testing & Strangler-Fig Shadow Traffic Equivalence."""
import hashlib

def run_characterization_shadow_audit(legacy_fn, modern_fn, corpus: list) -> tuple[bool, list[str]]:
    diffs: list[str] = []
    for inp in corpus:
        out_leg = legacy_fn(inp)
        out_mod = modern_fn(inp)
        h_leg = hashlib.sha256(repr(out_leg).encode()).hexdigest()
        h_mod = hashlib.sha256(repr(out_mod).encode()).hexdigest()
        if h_leg != h_mod:
            diffs.append(f"Input {inp!r}: legacy={out_leg!r} != modern={out_mod!r}")
    return (len(diffs) == 0, diffs)

ok, _ = run_characterization_shadow_audit(lambda x: x * x + 2 * x + 1, lambda x: (x + 1) ** 2, range(-50, 51))
assert ok
ok_bad, diffs = run_characterization_shadow_audit(lambda x: x // 2, lambda x: int(x / 2), [-3, -1, 0, 2])
assert not ok_bad and len(diffs) == 2  # Catches Python floor-division (-3 // 2 == -2) vs C truncation towards zero (int(-3/2) == -1)!
print("LEGACY MODERNIZATION CHARACTERIZATION & SIGNED DIVISION SEMANTICS AUDIT VERIFIED")
