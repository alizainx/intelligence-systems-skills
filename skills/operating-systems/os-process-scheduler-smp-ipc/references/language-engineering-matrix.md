# OS Context Switch & Proportional-Share Scheduler Reference

Never hold a runqueue spinlock across a blocking I/O wait; release locks after context-switch completion.
