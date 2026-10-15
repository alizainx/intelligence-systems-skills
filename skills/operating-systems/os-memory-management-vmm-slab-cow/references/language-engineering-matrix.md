# Buddy, Slab, CoW & TLB Shootdown Invariants Reference

Marking a PTE Read-Only for `fork()` CoW without flushing the TLB allows stale writable TLB entries to silently corrupt the shared parent/child frame!
