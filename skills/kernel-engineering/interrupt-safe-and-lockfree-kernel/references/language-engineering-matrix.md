# ISR Locking & Atomic Memory Ordering Reference

Acquiring a spinlock in process context with `spin_lock()` instead of `spin_lock_irqsave()` when the same lock is used by a hard IRQ handler causes instant single-CPU deadlock on interrupt arrival.
