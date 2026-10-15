---
name: arm-aarch64-assembly-engineering
description: Engineer and verify ARM/AArch64 assembly routines adhering to Procedure Call Standard AAPCS64, 16-byte SP alignment, weakly ordered LDAR/STLR atomics, ISB/DSB barriers, NEON/SVE SIMD, and exception-level EL0-EL3 transitions.
allowed-tools: execute_bash view_file write_to_file
---

# ARM & AArch64 Assembly (AAPCS64, Load-Acquire/Store-Release, NEON/SVE & EL1)

Engineer and verify ARM/AArch64 assembly routines adhering to Procedure Call Standard AAPCS64, 16-byte SP alignment, weakly ordered LDAR/STLR atomics, ISB/DSB barriers, NEON/SVE SIMD, and exception-level EL0-EL3 transitions.

## A. Identity

- **Skill Name**: `arm-aarch64-assembly-engineering`
- **Domain**: `systems-programming`
- **Language / Representation**: **Assembly (ARM/AArch64)** (`Hardware Architecture Assembly Language`)
- **Technical Relationship**: ISA-level assembly target for ARMv8-A/v9-A (`AArch64`) and ARMv7-M (`Thumb-2`); governed by AAPCS64.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Assembly (ARM/AArch64)**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ARM Architecture Reference Manual (ARMv8-A / ARMv9-A), Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64) (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Cross-compilation via `gcc -target aarch64-linux-gnu` or CMake toolchain files.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Assembly (ARM/AArch64)** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Assembly (ARM/AArch64)**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Assembly (ARM/AArch64)** (`aarch64_aapcs64_barrier.s`, `Cross-compilation via `gcc -target aarch64-linux-gnu` or CMake toolchain files.`).

### Prerequisites

- Target language version (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Assembly (ARM/AArch64)** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Hardware enforces 16-byte alignment whenever `sp` is used as a base register (`stp x29, x30, [sp, #-16]!`); zero red zone in AAPCS64.), type soundness limits (Fixed 32-bit instruction encoding; `v0-v31` 128-bit NEON registers with explicit lane qualifiers (`v0.4s`, `v0.2d`).), and concurrency hazards (Weakly ordered memory model: use `ldar`/`stlr` (one-way acquire/release barriers), `ldaxr`/`stlxr` exclusives, or ARMv8.1 LSE `cas`/`ldadd`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ARM Architecture Reference Manual (ARMv8-A / ARMv9-A), Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Load/store RISC architecture (`ldp`, `stp`, `adrp` + `add` PC-relative addressing); 64-bit `x0-x30` and 32-bit `w0-w30` registers.
2. **Type System & Inference**: Fixed 32-bit instruction encoding; `v0-v31` 128-bit NEON registers with explicit lane qualifiers (`v0.4s`, `v0.2d`).
3. **Memory Management**: Hardware enforces 16-byte alignment whenever `sp` is used as a base register (`stp x29, x30, [sp, #-16]!`); zero red zone in AAPCS64.
4. **Concurrency & Async Programming**: Weakly ordered memory model: use `ldar`/`stlr` (one-way acquire/release barriers), `ldaxr`/`stlxr` exclusives, or ARMv8.1 LSE `cas`/`ldadd`.
5. **Standard Library & Ecosystem**: `aarch64-linux-gnu-as`, Clang/LLVM integrated assembler, QEMU `qemu-aarch64`.
6. **Build Systems & Package Management**: Cross-compilation via `gcc -target aarch64-linux-gnu` or CMake toolchain files.
7. **Compiler / Interpreter Behavior**: Literal pool placement, branch range limits (`+-128MB` for `b`/`bl`), and Pointer Authentication (`paciasp`/`autiasp`).
8. **Debugging & Observability**: `gdb-multiarch` with QEMU user/system gdbstub, inspecting `NZCV`, `ESR_EL1`, `FAR_EL1`, and `ELR_EL1`.
9. **Security Hardening**: Enable Branch Target Identification (`bti c`) and Pointer Authentication (`paciasp`) to mitigate ROP/JOP attacks.
10. **Performance Optimization**: Pair loads/stores (`ldp`/`stp`), preload caches (`prfm`), and vectorize via 128-bit NEON / scalable SVE.
11. **Error Handling Discipline**: Return status codes in `x0` and preserve frame pointer `x29` + link register `x30` for deterministic unwinding.
12. **Testing Methodologies**: Verify AAPCS64 register save/restore invariants (`x19-x28`, `d8-d15` callee-saved) and `sp % 16 == 0` alignment.
13. **Interoperability & Cross-Platform ABI**: Args in `x0-x7` and `v0-v7`; indirect result location in `x8`; `x18` reserved as platform register on Darwin/Windows/Android.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/arm-aarch64-assembly-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (ARMv8.0-A / ARMv8.2-A (LSE Atomics) / ARMv9-A (SVE2, PAC/BTI)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Assembly (ARM/AArch64)**: Sub-16-byte `sp` modification causing hardware alignment fault, omitting `dsb ish; isb` after page-table/sysreg writes, and clobbering `x19-x28`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
