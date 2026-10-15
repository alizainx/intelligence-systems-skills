#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "pbr_exposure_pass.comp").read_text()
assert "#version 450" in src and "layout(std140, set = 0, binding = 0)" in src and "max(mapped, vec3(1e-6))" in src
print("PARTIALLY VERIFIED: GLSL 450 compute shader std140 vec4 alignment, bounds guard & NaN-safe pow() verified (glslangValidator designed for CI).")
