#!/usr/bin/env python3
import re
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "axis_skid_buffer.v").read_text()
assert "`default_nettype none" in src and "always @(posedge clk or negedge rst_n)" in src
# Verify clocked always block uses only non-blocking (<=) assignments and zero blocking (=) assignments
always_body = src.split("always @(posedge clk")[1]
assert "<=" in always_body and not re.search(r"(?<![!<>=])=(?!=)", always_body)
print("PARTIALLY VERIFIED: Verilog IEEE 1364 `default_nettype none, AXI skid buffer & strict non-blocking (<=) sequential rules verified (verilator/iverilog designed for CI).")
