# Zig Explicit Allocator & errdefer Reference

Pair every `try allocator.alloc(...)` with `errdefer allocator.free(...)` before subsequent fallible operations.
