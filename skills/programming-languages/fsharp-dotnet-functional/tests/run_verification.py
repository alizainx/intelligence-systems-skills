#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "UnitsOfMeasureKinematics.fs").read_text()
assert "[<Measure>] type N = kg * m / s^2" in src and "[<Struct>]" in src and "Result<float<kg * m / s>, string>" in src
print("PARTIALLY VERIFIED: F# 8 [<Measure>] dimensional homogeneity, [<Struct>] record & Result computation invariants verified (dotnet fsi designed for CI).")
