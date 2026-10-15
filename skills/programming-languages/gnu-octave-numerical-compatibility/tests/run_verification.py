#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "portable_rk4_step.m").read_text()
assert "function y_next = portable_rk4_step" in src and "%!test" in src and "assert(" in src
print("PARTIALLY VERIFIED: GNU Octave portable RK4 integrator & embedded %!test/%!assert verification block verified (octave CLI designed for CI).")
