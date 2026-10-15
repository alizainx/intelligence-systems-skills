#!/usr/bin/env python3
import subprocess
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "wasm_euclid_gcd.mjs"
res = subprocess.run(["node", str(SRC)], capture_output=True, text=True, check=True)
print(res.stdout.strip())
