# Nontrivial Implementation & Multi-File Engineering Walkthrough: `rust-ownership-and-nostd`

- **Target File**: `examples/nostd_pinned_ring.rs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
#![no_std]
#![deny(unsafe_op_in_unsafe_fn)]

pub struct CheckedSliceRing<'a, T> {
    buf: &'a mut [T],
    head: usize,
    tail: usize,
    len: usize,
}

impl<'a, T: Copy> CheckedSliceRing<'a, T> {
    pub fn new(buf: &'a mut [T]) -> Option<Self> {
        if buf.is_empty() { return None; }
        Some(Self { buf, head: 0, tail: 0, len: 0 })
    }

    pub fn push(&mut self, item: T) -> Result<(), T> {
        if self.len == self.buf.len() { return Err(item); }
        self.buf[self.head] = item;
        self.head = (self.head + 1) % self.buf.len();
        self.len += 1;
        Ok(())
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.len == 0 { return None; }
        let item = self.buf[self.tail];
        self.tail = (self.tail + 1) % self.buf.len();
        self.len -= 1;
        Some(item)
    }
}

```
