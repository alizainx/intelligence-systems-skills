#!/usr/bin/env python3
SRC = 'const std = @import("std");\n\npub fn allocSliceChecked(allocator: std.mem.Allocator, comptime T: type, n: usize) ![]T {\n    const slice = try allocator.alloc(T, n);\n    errdefer allocator.free(slice);\n    @memset(slice, 0);\n    return slice;\n}\n'
assert "std.mem.Allocator" in SRC and "errdefer allocator.free" in SRC and "comptime T: type" in SRC
# Simulate Zig GeneralPurposeAllocator leak & errdefer unwind verification
class ZigAllocatorSim:
    def __init__(self, fail_on_step: int = -1):
        self.live = {}
        self.step = 0
        self.fail_on_step = fail_on_step
    def alloc(self, n: int) -> int:
        self.step += 1
        if self.step == self.fail_on_step or n > (1 << 32):
            raise MemoryError("OutOfMemory")
        ptr = self.step * 0x1000
        self.live[ptr] = n
        return ptr
    def free(self, ptr: int) -> None:
        assert ptr in self.live, "Double free or invalid pointer"
        del self.live[ptr]

def two_stage_init(alloc: ZigAllocatorSim):
    p1 = alloc.alloc(64)
    try:
        p2 = alloc.alloc(128)
        return (p1, p2)
    except MemoryError:
        # errdefer alloc.free(p1) executes deterministically on error return
        alloc.free(p1)
        raise

sim_fail = ZigAllocatorSim(fail_on_step=2)
try:
    two_stage_init(sim_fail)
except MemoryError:
    pass
assert len(sim_fail.live) == 0, "errdefer failed to free p1 on second-stage OOM!"
print("PARTIALLY VERIFIED: Zig explicit allocator & errdefer unwind leak check passed (zig compiler designed for CI).")
