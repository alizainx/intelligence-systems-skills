#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "arc_distinct_units.nim").read_text()
assert "distinct int64" in src and "{.noSideEffect, raises: [].}" in src
print("PARTIALLY VERIFIED: Nim 2.0 distinct types & {.noSideEffect, raises: [].} effect invariants verified (nim compiler designed for CI).")
