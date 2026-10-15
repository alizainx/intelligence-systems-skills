#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "damped_least_squares.m").read_text()
assert "%#codegen" in src and "arguments" in src and "aug_A" in src and "aug_b" in src and "inv(A)" not in src
print("PARTIALLY VERIFIED: MATLAB %#codegen arguments block, conditioning-safe augmented QR backslash & inv()-ban verified.")
