# Deep Engineering Reference: ARM & AArch64 Assembly (AAPCS64, Load-Acquire/Store-Release, NEON/SVE & EL1) (`arm-aarch64-assembly-engineering`)

- **Language / Representation**: **Assembly (ARM/AArch64)**
- **Taxonomic Classification**: `Hardware Architecture Assembly Language`
- **Technical Relationship**: ISA-level assembly target for ARMv8-A/v9-A (`AArch64`) and ARMv7-M (`Thumb-2`); governed by AAPCS64.
- **Governing Standards & Versions**: ARM Architecture Reference Manual (ARMv8-A / ARMv9-A), Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64) (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Assembly (ARM/AArch64)** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Load/store RISC architecture (`ldp`, `stp`, `adrp` + `add` PC-relative addressing); 64-bit `x0-x30` and 32-bit `w0-w30` registers. |
| 2 | **Type System & Inference** | Fixed 32-bit instruction encoding; `v0-v31` 128-bit NEON registers with explicit lane qualifiers (`v0.4s`, `v0.2d`). |
| 3 | **Memory Management** | Hardware enforces 16-byte alignment whenever `sp` is used as a base register (`stp x29, x30, [sp, #-16]!`); zero red zone in AAPCS64. |
| 4 | **Concurrency & Async Programming** | Weakly ordered memory model: use `ldar`/`stlr` (one-way acquire/release barriers), `ldaxr`/`stlxr` exclusives, or ARMv8.1 LSE `cas`/`ldadd`. |
| 5 | **Standard Library & Ecosystem** | `aarch64-linux-gnu-as`, Clang/LLVM integrated assembler, QEMU `qemu-aarch64`. |
| 6 | **Build Systems & Package Management** | Cross-compilation via `gcc -target aarch64-linux-gnu` or CMake toolchain files. |
| 7 | **Compiler / Interpreter Behavior** | Literal pool placement, branch range limits (`+-128MB` for `b`/`bl`), and Pointer Authentication (`paciasp`/`autiasp`). |
| 8 | **Debugging** | `gdb-multiarch` with QEMU user/system gdbstub, inspecting `NZCV`, `ESR_EL1`, `FAR_EL1`, and `ELR_EL1`. |
| 9 | **Security** | Enable Branch Target Identification (`bti c`) and Pointer Authentication (`paciasp`) to mitigate ROP/JOP attacks. |
| 10 | **Performance Optimization** | Pair loads/stores (`ldp`/`stp`), preload caches (`prfm`), and vectorize via 128-bit NEON / scalable SVE. |
| 11 | **Error Handling** | Return status codes in `x0` and preserve frame pointer `x29` + link register `x30` for deterministic unwinding. |
| 12 | **Testing Methodologies** | Verify AAPCS64 register save/restore invariants (`x19-x28`, `d8-d15` callee-saved) and `sp % 16 == 0` alignment. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Args in `x0-x7` and `v0-v7`; indirect result location in `x8`; `x18` reserved as platform register on Darwin/Windows/Android. |
| 18 | **Common Engineering Mistakes** | Sub-16-byte `sp` modification causing hardware alignment fault, omitting `dsb ish; isb` after page-table/sysreg writes, and clobbering `x19-x28`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/arm-aarch64-assembly-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Assembly (ARM/AArch64)**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``gdb-multiarch` with QEMU user/system gdbstub, inspecting `NZCV`, `ESR_EL1`, `FAR_EL1`, and `ELR_EL1`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Cross-compilation via `gcc -target aarch64-linux-gnu` or CMake toolchain files.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Pair loads/stores (`ldp`/`stp`), preload caches (`prfm`), and vectorize via 128-bit NEON / scalable SVE.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Enable Branch Target Identification (`bti c`) and Pointer Authentication (`paciasp`) to mitigate ROP/JOP attacks.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Verify AAPCS64 register save/restore invariants (`x19-x28`, `d8-d15` callee-saved) and `sp % 16 == 0` alignment.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Args in `x0-x7` and `v0-v7`; indirect result location in `x8`; `x18` reserved as platform register on Darwin/Windows/Android.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
