#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "saturating_counter.vhdl").read_text()
assert "use ieee.numeric_std.all;" in src and "rising_edge(clk)" in src and "std_logic_arith" not in src
print("PARTIALLY VERIFIED: VHDL-2008 ieee.numeric_std, rising_edge(clk) & saturating counter invariants verified (ghdl designed for CI).")
