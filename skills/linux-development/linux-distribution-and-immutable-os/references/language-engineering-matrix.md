# Linux Distribution & Immutable A/B Update Reference

Never mutate `/usr` in place during a live update; stage the new deployment tree and atomically swap the bootloader entry.
