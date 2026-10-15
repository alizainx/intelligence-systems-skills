#!/usr/bin/env python3
import subprocess
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "strict_log_aggregator.pl"
res = subprocess.run(["perl", "-T", str(SRC)], capture_output=True, text=True, check=True)
print(res.stdout.strip())
