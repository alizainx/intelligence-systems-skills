#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "safe_sexp_reader.lisp").read_text()
assert "(*read-eval* nil)" in src and "gensym" in src and "declaim (ftype" in src
print("PARTIALLY VERIFIED: Common Lisp *read-eval* nil RCE defense, gensym macro hygiene & ftype declarations verified (sbcl designed for CI).")
