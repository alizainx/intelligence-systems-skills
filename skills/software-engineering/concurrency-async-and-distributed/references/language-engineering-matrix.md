# Lock Hierarchy & Backpressure Reference

Always wait on condition variables inside a predicate `while (!ready)` loop to guard against spurious wakeups.
