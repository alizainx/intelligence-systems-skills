# Verified Example: `zig-explicit-allocators-comptime` (`zig_allocator_errdefer.zig`)

```
const std = @import("std");

pub fn allocSliceChecked(allocator: std.mem.Allocator, comptime T: type, n: usize) ![]T {
    const slice = try allocator.alloc(T, n);
    errdefer allocator.free(slice);
    @memset(slice, 0);
    return slice;
}

```
