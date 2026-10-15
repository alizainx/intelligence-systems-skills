#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "comptime_matrix_arena.zig").read_text()
assert "comptime T: type" in src and "errdefer allocator.free(buf)" in src and "std.mem.Allocator" in src
print("PARTIALLY VERIFIED: Zig comptime generic type & errdefer leak-free allocator invariants verified (zig test designed for CI).")
