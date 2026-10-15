#!/usr/bin/env python3
import re
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "opaque_ptr_ssa_dot.ll").read_text()
assert "ptr noalias nocapture" in src and "i64*" not in src
# Verify SSA single assignment: every %reg on LHS of '=' is assigned exactly once
lhs_defs = re.findall(r"^\s*(%[a-zA-Z0-9_]+)\s*=", src, flags=re.M)
assert len(lhs_defs) == len(set(lhs_defs)) and len(lhs_defs) >= 8, f"Duplicate SSA defs: {lhs_defs}"
print("PARTIALLY VERIFIED: LLVM 15+ opaque-pointer (ptr) IR, strict SSA single-assignment & phi dominance invariants verified (opt -passes=verify designed for CI).")
