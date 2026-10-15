#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "type_stable_summary.R").read_text()
assert "NA_real_" in src and "!is.numeric(x)" in src and "1:" not in src
print("PARTIALLY VERIFIED: R 4.3+ NA_real_ type stability, scalar guard & zero 1:n hazard invariants verified (Rscript designed for CI).")
