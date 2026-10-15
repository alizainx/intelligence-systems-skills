# Deep Engineering Reference: RISC-V Assembly (RV32I/RV64GC psABI, RVWMO Fences, LR/SC & CSRs) (`riscv-assembly-engineering`)

- **Language / Representation**: **Assembly (RISC-V)**
- **Taxonomic Classification**: `Hardware Architecture Assembly Language`
- **Technical Relationship**: Modular open-standard RISC ISA (`RV32IMAC`, `RV64GC`) interacting with C/Rust via the RISC-V ELF psABI.
- **Governing Standards & Versions**: The RISC-V Instruction Set Manual (Volume I: Unprivileged ISA, Volume II: Privileged Architecture), RISC-V ELF psABI (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Assembly (RISC-V)** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `auipc` + `addi`/`ld` PC-relative addressing, `.option norelax` around `gp` initialization, and zero hardwired `x0`/`zero` register. |
| 2 | **Type System & Inference** | Sign-extension semantics on 32-bit operations in RV64 (`addiw`, `lwu` vs `lw`). |
| 3 | **Memory Management** | 16-byte stack alignment (`addi sp, sp, -16`) in `lp64`/`lp64d` ABIs; save `ra` (`x1`), `s0/fp` (`x8`), and `s1-s11`. |
| 4 | **Concurrency & Async Programming** | RISC-V Weak Memory Ordering (RVWMO): use `fence rw, rw`, `fence r, rw` (acquire), `fence rw, w` (release), and `lr.d`/`sc.d` or `amoswap.d.aqrl`. |
| 5 | **Standard Library & Ecosystem** | `riscv64-unknown-elf-as`, LLVM/Clang RISC-V backend, Spike ISA simulator, QEMU `qemu-system-riscv64`. |
| 6 | **Build Systems & Package Management** | GCC/Clang `-march=rv64gc -mabi=lp64d -mcmodel=medany`. |
| 7 | **Compiler / Interpreter Behavior** | Linker relaxation (`R_RISCV_RELAX`) converting two-instruction `auipc+jalr` sequences into single `jal` instructions. |
| 8 | **Debugging** | OpenOCD + GDB reading `mstatus`/`sstatus`, `mepc`/`sepc`, `mcause`/`scause`, and `mtval`/`stval`. |
| 9 | **Security** | Physical Memory Protection (PMP) CSR configuration in M-mode and W^X page permissions in Sv39/Sv48 S-mode. |
| 10 | **Performance Optimization** | Compressed 16-bit instructions (`RVC`) for I-cache density and RVV 1.0 vector-length agnostic (`vsetvli`) loops. |
| 11 | **Error Handling** | Return values in `a0` (`x10`) and `a1` (`x11`); trap handlers swap `sp` with `sscratch` using `csrrw sp, sscratch, sp`. |
| 12 | **Testing Methodologies** | Validate register preservation (`s0-s11`, `fs0-fs11`), `sp % 16 == 0`, and forward-progress guarantees on `lr.d`/`sc.d` loops. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Integer args in `a0-a7` (`x10-x17`), float args in `fa0-fa7` (`f10-f17`), thread pointer in `tp` (`x4`). |
| 18 | **Common Engineering Mistakes** | Putting non-constrained instructions inside an `lr.d`/`sc.d` reservation loop, forgetting `.option norelax` when setting `gp`, and clobbering `tp`/`gp`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/riscv-assembly-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Assembly (RISC-V)**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `OpenOCD + GDB reading `mstatus`/`sstatus`, `mepc`/`sepc`, `mcause`/`scause`, and `mtval`/`stval`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `GCC/Clang `-march=rv64gc -mabi=lp64d -mcmodel=medany`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Compressed 16-bit instructions (`RVC`) for I-cache density and RVV 1.0 vector-length agnostic (`vsetvli`) loops.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Physical Memory Protection (PMP) CSR configuration in M-mode and W^X page permissions in Sv39/Sv48 S-mode.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Validate register preservation (`s0-s11`, `fs0-fs11`), `sp % 16 == 0`, and forward-progress guarantees on `lr.d`/`sc.d` loops.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Integer args in `a0-a7` (`x10-x17`), float args in `fa0-fa7` (`f10-f17`), thread pointer in `tp` (`x4`).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
