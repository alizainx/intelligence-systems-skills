---
name: riscv-assembly-engineering
description: Write, analyze, and verify RISC-V assembly code for RV32 and RV64 targets covering the RISC-V psABI calling convention, RVWMO memory model fences, A-extension LR/SC and AMO atomics, and M/S-mode CSR trap vectors.
allowed-tools: execute_bash view_file write_to_file
---

# RISC-V Assembly (RV32I/RV64GC psABI, RVWMO Fences, LR/SC & CSRs)

Write, analyze, and verify RISC-V assembly code for RV32 and RV64 targets covering the RISC-V psABI calling convention, RVWMO memory model fences, A-extension LR/SC and AMO atomics, and M/S-mode CSR trap vectors.

## A. Identity

- **Skill Name**: `riscv-assembly-engineering`
- **Domain**: `systems-programming`
- **Language / Representation**: **Assembly (RISC-V)** (`Hardware Architecture Assembly Language`)
- **Technical Relationship**: Modular open-standard RISC ISA (`RV32IMAC`, `RV64GC`) interacting with C/Rust via the RISC-V ELF psABI.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Assembly (RISC-V)**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: The RISC-V Instruction Set Manual (Volume I: Unprivileged ISA, Volume II: Privileged Architecture), RISC-V ELF psABI (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`GCC/Clang `-march=rv64gc -mabi=lp64d -mcmodel=medany`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Assembly (RISC-V)** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Assembly (RISC-V)**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Assembly (RISC-V)** (`riscv64_atomic_cas.s`, `GCC/Clang `-march=rv64gc -mabi=lp64d -mcmodel=medany`.`).

### Prerequisites

- Target language version (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Assembly (RISC-V)** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (16-byte stack alignment (`addi sp, sp, -16`) in `lp64`/`lp64d` ABIs; save `ra` (`x1`), `s0/fp` (`x8`), and `s1-s11`.), type soundness limits (Sign-extension semantics on 32-bit operations in RV64 (`addiw`, `lwu` vs `lw`).), and concurrency hazards (RISC-V Weak Memory Ordering (RVWMO): use `fence rw, rw`, `fence r, rw` (acquire), `fence rw, w` (release), and `lr.d`/`sc.d` or `amoswap.d.aqrl`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce The RISC-V Instruction Set Manual (Volume I: Unprivileged ISA, Volume II: Privileged Architecture), RISC-V ELF psABI.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `auipc` + `addi`/`ld` PC-relative addressing, `.option norelax` around `gp` initialization, and zero hardwired `x0`/`zero` register.
2. **Type System & Inference**: Sign-extension semantics on 32-bit operations in RV64 (`addiw`, `lwu` vs `lw`).
3. **Memory Management**: 16-byte stack alignment (`addi sp, sp, -16`) in `lp64`/`lp64d` ABIs; save `ra` (`x1`), `s0/fp` (`x8`), and `s1-s11`.
4. **Concurrency & Async Programming**: RISC-V Weak Memory Ordering (RVWMO): use `fence rw, rw`, `fence r, rw` (acquire), `fence rw, w` (release), and `lr.d`/`sc.d` or `amoswap.d.aqrl`.
5. **Standard Library & Ecosystem**: `riscv64-unknown-elf-as`, LLVM/Clang RISC-V backend, Spike ISA simulator, QEMU `qemu-system-riscv64`.
6. **Build Systems & Package Management**: GCC/Clang `-march=rv64gc -mabi=lp64d -mcmodel=medany`.
7. **Compiler / Interpreter Behavior**: Linker relaxation (`R_RISCV_RELAX`) converting two-instruction `auipc+jalr` sequences into single `jal` instructions.
8. **Debugging & Observability**: OpenOCD + GDB reading `mstatus`/`sstatus`, `mepc`/`sepc`, `mcause`/`scause`, and `mtval`/`stval`.
9. **Security Hardening**: Physical Memory Protection (PMP) CSR configuration in M-mode and W^X page permissions in Sv39/Sv48 S-mode.
10. **Performance Optimization**: Compressed 16-bit instructions (`RVC`) for I-cache density and RVV 1.0 vector-length agnostic (`vsetvli`) loops.
11. **Error Handling Discipline**: Return values in `a0` (`x10`) and `a1` (`x11`); trap handlers swap `sp` with `sscratch` using `csrrw sp, sscratch, sp`.
12. **Testing Methodologies**: Validate register preservation (`s0-s11`, `fs0-fs11`), `sp % 16 == 0`, and forward-progress guarantees on `lr.d`/`sc.d` loops.
13. **Interoperability & Cross-Platform ABI**: Integer args in `a0-a7` (`x10-x17`), float args in `fa0-fa7` (`f10-f17`), thread pointer in `tp` (`x4`).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/riscv-assembly-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (RV32IMAC / RV64GC (IMAFDC_Zicsr_Zifencei) / RVV 1.0), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Assembly (RISC-V)**: Putting non-constrained instructions inside an `lr.d`/`sc.d` reservation loop, forgetting `.option norelax` when setting `gp`, and clobbering `tp`/`gp`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
