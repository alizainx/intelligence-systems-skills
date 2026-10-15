# Multi-Architecture Kernel Compiler & Linker Reference

Omitting `-mno-red-zone` in an `x86_64` kernel causes silent stack corruption whenever an interrupt fires while the kernel is executing a leaf function.
