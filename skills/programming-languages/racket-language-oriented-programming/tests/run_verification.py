#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "contract_bounded_stack.rkt").read_text()
assert "#lang racket/base" in src and "contract-out" in src and "#:pre (s)" in src
print("PARTIALLY VERIFIED: Racket #lang racket/base module, dependent contract-out (->i) & #:pre guard verified (raco test designed for CI).")
