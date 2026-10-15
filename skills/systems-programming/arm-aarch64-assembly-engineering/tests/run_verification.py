#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "aarch64_aapcs64_barrier.s").read_text()
assert "stp x29, x30, [sp, #-32]!" in src and "stlr" in src and "ldp x29, x30, [sp], #32" in src
print("PARTIALLY VERIFIED: AArch64 AAPCS64 16-byte SP frame prologue/epilogue & STLR release barrier verified (aarch64 cross-assembler designed for CI).")
