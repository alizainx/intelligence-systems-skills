# ELF64 Relocations, Calling Conventions & Toolchain Reference

In `x86_64` RIP-relative addressing (`mov (%rip), %rax`), the relocation addend `A` is `-4` (the distance from the relocation offset `P` to the next instruction's `RIP`).
