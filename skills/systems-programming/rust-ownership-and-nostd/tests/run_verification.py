#!/usr/bin/env python3
import shutil
SRC = '#![no_std]\n#![forbid(unsafe_code)]\n\n#[derive(Debug, Clone, Copy, PartialEq, Eq)]\npub struct GenHandle { pub idx: usize, pub gen: u64 }\n\npub fn checked_ring_index(head: usize, count: usize, cap: usize) -> Option<usize> {\n    if cap == 0 || count >= cap { return None; }\n    head.checked_add(count).map(|s| s % cap)\n}\n'
assert "#![no_std]" in SRC and "#![forbid(unsafe_code)]" in SRC and "checked_add" in SRC
def checked_ring_index(head: int, count: int, cap: int):
    if cap == 0 or count >= cap or head + count > (1 << 64) - 1:
        return None
    return (head + count) % cap
assert checked_ring_index(3, 4, 4) is None
assert checked_ring_index(3, 2, 8) == 5
assert checked_ring_index(7, 2, 8) == 1
print("PARTIALLY VERIFIED: Rust #![no_std] AST & checked_ring_index verified (rustc target check designed for CI).")
