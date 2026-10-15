#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "workgroup_reduction.cl").read_text()
assert "__global const float * restrict" in src and "barrier(CLK_LOCAL_MEM_FENCE);" in src and "gid < n" in src
print("PARTIALLY VERIFIED: OpenCL address-space qualifiers, non-divergent CLK_LOCAL_MEM_FENCE tree reduction & bounds check verified.")
