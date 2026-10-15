#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "c11_provenance_arena.c"
with tempfile.TemporaryDirectory() as td:
    bin_p = Path(td) / "test_bin"
    subprocess.run(["gcc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", "-Wpedantic", "-fanalyzer", "-fsanitize=address,undefined", str(SRC), "-o", str(bin_p)], check=True)
    res = subprocess.run([str(bin_p)], capture_output=True, text=True, check=True)
    print(res.stdout.strip())
