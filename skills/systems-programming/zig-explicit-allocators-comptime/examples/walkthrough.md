# Nontrivial Implementation & Multi-File Engineering Walkthrough: `zig-explicit-allocators-comptime`

- **Target File**: `examples/comptime_matrix_arena.zig`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
const std = @import("std");

pub fn RingQueue(comptime T: type) type {
    return struct {
        const Self = @This();
        items: []T,
        allocator: std.mem.Allocator,
        head: usize = 0,
        tail: usize = 0,
        count: usize = 0,

        pub fn init(allocator: std.mem.Allocator, capacity: usize) !Self {
            if (capacity == 0) return error.InvalidCapacity;
            const buf = try allocator.alloc(T, capacity);
            errdefer allocator.free(buf);
            return Self{ .items = buf, .allocator = allocator };
        }

        pub fn deinit(self: *Self) void {
            self.allocator.free(self.items);
            self.* = undefined;
        }
    };
}

```
