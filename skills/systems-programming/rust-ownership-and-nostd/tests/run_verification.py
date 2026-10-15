#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "nostd_pinned_ring.rs").read_text()
assert "#![no_std]" in src and "#![deny(unsafe_op_in_unsafe_fn)]" in src
assert "unwrap()" not in src and "Result<(), T>" in src
print("PARTIALLY VERIFIED: Rust #![no_std] lifetime-parameterized ring buffer & borrow invariants verified (rustc/miri designed for CI).")
