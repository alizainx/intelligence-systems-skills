#![no_std]
#![forbid(unsafe_code)]

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct GenHandle { pub idx: usize, pub gen: u64 }

pub fn checked_ring_index(head: usize, count: usize, cap: usize) -> Option<usize> {
    if cap == 0 || count >= cap { return None; }
    head.checked_add(count).map(|s| s % cap)
}
