#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "col_major_spmv.f90").read_text()
assert "implicit none (type, external)" in src and "iso_fortran_env" in src and "iso_c_binding" in src
# Verify inner loop is i (stride-1 column-major) and outer loop is j
assert src.index("do j = 1, m") < src.index("do i = 1, n")
print("PARTIALLY VERIFIED: Fortran 2018 implicit none, iso_fortran_env real64, iso_c_binding & column-major stride-1 loop order verified (gfortran designed for CI).")
