#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path
SRC = Path(__file__).resolve().parents[1] / "examples" / "cpp20_concepts_raii.cpp"
with tempfile.TemporaryDirectory() as td:
    bin_p = Path(td) / "cpp_bin"
    subprocess.run(["g++", "-std=c++20", "-O2", "-Wall", "-Wextra", "-Werror", "-Wpedantic", "-fsanitize=address,undefined", str(SRC), "-o", str(bin_p)], check=True)
    res = subprocess.run([str(bin_p)], capture_output=True, text=True, check=True)
    print(res.stdout.strip())
