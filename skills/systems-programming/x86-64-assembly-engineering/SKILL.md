---
name: x86-64-assembly-engineering
description: Write, audit, debug, and verify x86 and x86-64 assembly routines using AT&T and Intel syntax, System V AMD64 calling conventions, 16-byte stack alignment, red-zone discipline, SSE/AVX2 SIMD, and non-executable stack markings.
allowed-tools: execute_bash view_file write_to_file
---

# x86/x86-64 Assembly (System V AMD64 ABI, AVX2/SIMD & Kernel Entry)

Write, audit, debug, and verify x86 and x86-64 assembly routines using AT&T and Intel syntax, System V AMD64 calling conventions, 16-byte stack alignment, red-zone discipline, SSE/AVX2 SIMD, and non-executable stack markings.

## A. Identity

- **Skill Name**: `x86-64-assembly-engineering`
- **Domain**: `systems-programming`
- **Language / Representation**: **Assembly (x86/x86-64)** (`Hardware Architecture Assembly Language`)
- **Technical Relationship**: ISA-level assembly target for x86/x86-64 processors; interoperates directly with C/C++/Rust via System V AMD64 and Win64 ABIs.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Assembly (x86/x86-64)**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: System V Application Binary Interface AMD64 Architecture Processor Supplement, Intel 64 & IA-32 Architectures SDM (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`GCC/Clang driver (`gcc -c file.s`), CMake `enable_language(ASM)`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Assembly (x86/x86-64)** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Assembly (x86/x86-64)**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Assembly (x86/x86-64)** (`x86_64_sysv_fnv1a.c`, `GCC/Clang driver (`gcc -c file.s`), CMake `enable_language(ASM)`.`).

### Prerequisites

- Target language version (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Assembly (x86/x86-64)** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Maintain `(%rsp + 8) % 16 == 0` at function entry (`%rsp % 16 == 0` before `callq`); respect 128-byte user-space red zone (`-mno-red-zone` in kernel/ISR).), type soundness limits (Register-width & vector-lane discipline (`%rax` 64-bit, `%eax` zero-extends upper 32 bits of `%rax`, `%xmm0` 128-bit, `%ymm0` 256-bit).), and concurrency hazards (`lock cmpxchgq`, `lock xaddq`, `lfence`/`sfence`/`mfence` total-store-order (TSO) hardware memory model.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce System V Application Binary Interface AMD64 Architecture Processor Supplement, Intel 64 & IA-32 Architectures SDM.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit operand-size suffixes in AT&T (`movq`, `addl`, `imulq`) or `qword ptr` in Intel syntax; RIP-relative addressing `sym(%rip)` for PIC.
2. **Type System & Inference**: Register-width & vector-lane discipline (`%rax` 64-bit, `%eax` zero-extends upper 32 bits of `%rax`, `%xmm0` 128-bit, `%ymm0` 256-bit).
3. **Memory Management**: Maintain `(%rsp + 8) % 16 == 0` at function entry (`%rsp % 16 == 0` before `callq`); respect 128-byte user-space red zone (`-mno-red-zone` in kernel/ISR).
4. **Concurrency & Async Programming**: `lock cmpxchgq`, `lock xaddq`, `lfence`/`sfence`/`mfence` total-store-order (TSO) hardware memory model.
5. **Standard Library & Ecosystem**: GNU Assembler (`as`), NASM, YASM, LLVM MC, `objdump -d -M intel`, `readelf -S`.
6. **Build Systems & Package Management**: GCC/Clang driver (`gcc -c file.s`), CMake `enable_language(ASM)`.
7. **Compiler / Interpreter Behavior**: Assembler relaxation of short/near branches, `.align 16` loop padding, and `.cfi_startproc`/`.cfi_endproc` DWARF unwind emission.
8. **Debugging & Observability**: GDB `layout asm`, `info registers`, `stepi`/`nexti`, and DWARF `.eh_frame` unwind verification.
9. **Security Hardening**: Always emit `.section .note.GNU-stack,"",@progbits` to prevent executable stacks (`RWE` `PT_GNU_STACK`), and support `endbr64` for Intel CET.
10. **Performance Optimization**: Break false register dependencies (`xorl %eax, %eax`), issue `vzeroupper` after 256-bit AVX2 routines, and align hot inner loops.
11. **Error Handling Discipline**: Propagate status via `%rax` or carry/zero flags (`jc`/`jz`) across internal asm helpers.
12. **Testing Methodologies**: Link directly against C11 test harnesses verifying callee-saved register preservation (`%rbx`, `%rbp`, `%r12-%r15`).
13. **Interoperability & Cross-Platform ABI**: System V AMD64 integer args in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`; float args in `%xmm0-%xmm7`; return in `%rax:%rdx`.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/x86-64-assembly-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (x86-64-v1 / v2 / v3 (AVX2, BMI2) / v4 (AVX-512)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Assembly (x86/x86-64)**: Calling C functions with an unaligned 8-byte `%rsp` (crashing `movaps`), clobbering `%rbx`/`%r12-%r15`, and omitting `.note.GNU-stack`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
