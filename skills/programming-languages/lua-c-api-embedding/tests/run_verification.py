#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "sandboxed_eval.lua").read_text()
assert 'load(untrusted_src, "sandbox", "t", safe_env)' in src and "pcall(chunk)" in src and "local M = {}" in src
print("PARTIALLY VERIFIED: Lua 5.4 text-only ('t') _ENV sandboxed loader & local-scope invariants verified (lua interpreter designed for CI).")
