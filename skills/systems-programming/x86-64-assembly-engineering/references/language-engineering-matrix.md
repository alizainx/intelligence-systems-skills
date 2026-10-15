# Deep Engineering Reference: x86/x86-64 Assembly (System V AMD64 ABI, AVX2/SIMD & Kernel Entry) (`x86-64-assembly-engineering`)

- **Language / Representation**: **Assembly (x86/x86-64)**
- **Taxonomic Classification**: `Hardware Architecture Assembly Language`
- **Technical Relationship**: ISA-level assembly target for x86/x86-64 processors; interoperates directly with C/C++/Rust via System V AMD64 and Win64 ABIs.
- **Governing Standards & Versions**: System V Application Binary Interface AMD64 Architecture Processor Supplement, Intel 64 & IA-32 Architectures SDM (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Assembly (x86/x86-64)** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Explicit operand-size suffixes in AT&T (`movq`, `addl`, `imulq`) or `qword ptr` in Intel syntax; RIP-relative addressing `sym(%rip)` for PIC. |
| 2 | **Type System & Inference** | Register-width & vector-lane discipline (`%rax` 64-bit, `%eax` zero-extends upper 32 bits of `%rax`, `%xmm0` 128-bit, `%ymm0` 256-bit). |
| 3 | **Memory Management** | Maintain `(%rsp + 8) % 16 == 0` at function entry (`%rsp % 16 == 0` before `callq`); respect 128-byte user-space red zone (`-mno-red-zone` in kernel/ISR). |
| 4 | **Concurrency & Async Programming** | `lock cmpxchgq`, `lock xaddq`, `lfence`/`sfence`/`mfence` total-store-order (TSO) hardware memory model. |
| 5 | **Standard Library & Ecosystem** | GNU Assembler (`as`), NASM, YASM, LLVM MC, `objdump -d -M intel`, `readelf -S`. |
| 6 | **Build Systems & Package Management** | GCC/Clang driver (`gcc -c file.s`), CMake `enable_language(ASM)`. |
| 7 | **Compiler / Interpreter Behavior** | Assembler relaxation of short/near branches, `.align 16` loop padding, and `.cfi_startproc`/`.cfi_endproc` DWARF unwind emission. |
| 8 | **Debugging** | GDB `layout asm`, `info registers`, `stepi`/`nexti`, and DWARF `.eh_frame` unwind verification. |
| 9 | **Security** | Always emit `.section .note.GNU-stack,"",@progbits` to prevent executable stacks (`RWE` `PT_GNU_STACK`), and support `endbr64` for Intel CET. |
| 10 | **Performance Optimization** | Break false register dependencies (`xorl %eax, %eax`), issue `vzeroupper` after 256-bit AVX2 routines, and align hot inner loops. |
| 11 | **Error Handling** | Propagate status via `%rax` or carry/zero flags (`jc`/`jz`) across internal asm helpers. |
| 12 | **Testing Methodologies** | Link directly against C11 test harnesses verifying callee-saved register preservation (`%rbx`, `%rbp`, `%r12-%r15`). |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | System V AMD64 integer args in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`; float args in `%xmm0-%xmm7`; return in `%rax:%rdx`. |
| 18 | **Common Engineering Mistakes** | Calling C functions with an unaligned 8-byte `%rsp` (crashing `movaps`), clobbering `%rbx`/`%r12-%r15`, and omitting `.note.GNU-stack`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/x86-64-assembly-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Assembly (x86/x86-64)**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GDB `layout asm`, `info registers`, `stepi`/`nexti`, and DWARF `.eh_frame` unwind verification.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `GCC/Clang driver (`gcc -c file.s`), CMake `enable_language(ASM)`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Break false register dependencies (`xorl %eax, %eax`), issue `vzeroupper` after 256-bit AVX2 routines, and align hot inner loops.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Always emit `.section .note.GNU-stack,"",@progbits` to prevent executable stacks (`RWE` `PT_GNU_STACK`), and support `endbr64` for Intel CET.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Link directly against C11 test harnesses verifying callee-saved register preservation (`%rbx`, `%rbp`, `%r12-%r15`).).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (System V AMD64 integer args in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`; float args in `%xmm0-%xmm7`; return in `%rax:%rdx`.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
