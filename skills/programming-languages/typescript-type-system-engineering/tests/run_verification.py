#!/usr/bin/env python3
import subprocess
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "branded_type_guard.mjs"
res = subprocess.run(["node", str(SRC)], capture_output=True, text=True, check=True)
print(res.stdout.strip())
