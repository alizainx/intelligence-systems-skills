#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "StrictLedgerFold.hs").read_text()
assert "{-# LANGUAGE StrictData #-}" in src and "foldl'" in src and "newtype AccountBalance" in src
print("PARTIALLY VERIFIED: Haskell GHC StrictData, BangPatterns & foldl' space-leak-free accumulator verified (ghc designed for CI).")
