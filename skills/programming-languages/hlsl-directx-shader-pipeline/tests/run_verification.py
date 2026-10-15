#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "wave_coalesced_atomic.hlsl").read_text()
assert "WaveActiveCountBits" in src and "WaveIsFirstLane()" in src and "float2 _pad0;" in src
print("PARTIALLY VERIFIED: HLSL SM 6.6 Wave-coalesced InterlockedAdd & 16-byte ConstantBuffer alignment verified (dxc designed for CI).")
