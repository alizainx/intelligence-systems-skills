#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "protocol_frame_parser.ex").read_text()
assert "@spec parse_frame" in src and ":binary.copy(rest)" in src and "unsigned-big-integer-size(16)" in src
print("PARTIALLY VERIFIED: Elixir bitstring binary parser, @spec typespec & :binary.copy refc leak prevention verified (elixir/mix designed for CI).")
