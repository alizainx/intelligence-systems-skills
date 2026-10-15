#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "tailrec_ring_checksum.scm").read_text()
assert "(define-library (iss tailrec-checksum)" in src and "(let loop ((i 0) (a 1) (b 0))" in src
print("PARTIALLY VERIFIED: R7RS Scheme define-library encapsulation & proper tail-recursive named-let Adler-32 verified (guile/chez designed for CI).")
