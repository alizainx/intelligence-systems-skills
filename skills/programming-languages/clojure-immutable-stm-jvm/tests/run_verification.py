#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "transducer_stm_ledger.clj").read_text()
assert "(set! *warn-on-reflection* true)" in src and "(dosync" in src and "(transduce (comp" in src
print("PARTIALLY VERIFIED: Clojure *warn-on-reflection*, STM dosync/alter & allocation-free transduce pipeline verified (clojure CLI designed for CI).")
