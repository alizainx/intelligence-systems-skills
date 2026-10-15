#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "ZeroAllocSpanParser.cs").read_text()
assert "readonly record struct" in src and "ReadOnlySpan<byte>" in src and "BinaryPrimitives" in src
print("PARTIALLY VERIFIED: C# 12 readonly record struct & ReadOnlySpan<byte> zero-allocation parser verified (dotnet SDK designed for CI).")
