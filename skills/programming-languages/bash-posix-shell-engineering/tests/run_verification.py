#!/usr/bin/env python3
import subprocess
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "atomic_config_writer.sh"
subprocess.run(["bash", "-n", str(SRC)], check=True)
res = subprocess.run(["bash", str(SRC)], capture_output=True, text=True, check=True)
print(res.stdout.strip())
