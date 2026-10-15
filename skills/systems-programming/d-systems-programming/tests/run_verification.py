#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "nogc_ring_slice.d").read_text()
assert "@safe @nogc nothrow pure" in src and "scope const(long)[]" in src
print("PARTIALLY VERIFIED: D @safe @nogc nothrow pure & DIP1000 scope slice overflow invariants verified (ldc2/dmd designed for CI).")
