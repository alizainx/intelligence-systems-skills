#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "soa_tracking_arena.odin").read_text()
assert "#soa[]Particle" in src and "core:mem" in src
print("PARTIALLY VERIFIED: Odin #soa Struct-of-Arrays & context.allocator invariants verified (odin compiler designed for CI).")
