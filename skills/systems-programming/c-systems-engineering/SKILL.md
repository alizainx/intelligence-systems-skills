---
name: c-systems-engineering
description: Engineer, audit, debug, and verify ISO C11/C17/C23 systems software with strict pointer provenance, effective-type aliasing compliance, alignment, C11 atomics, ABI stability, and GCC -fanalyzer + ASan/UBSan verification.
allowed-tools: execute_bash view_file write_to_file
---

# ISO C (C11/C17/C23) Systems Engineering & Memory Safety

Engineer, audit, debug, and verify ISO C11/C17/C23 systems software with strict pointer provenance, effective-type aliasing compliance, alignment, C11 atomics, ABI stability, and GCC -fanalyzer + ASan/UBSan verification.

## A. Identity

- **Skill Name**: `c-systems-engineering`
- **Domain**: `systems-programming`
- **Language / Representation**: **C** (`Systems Programming Language`)
- **Technical Relationship**: Foundational ISO systems language and universal native ABI substrate (`extern "C"`).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **C**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 9899:2011 (C11), ISO/IEC 9899:2018 (C17), ISO/IEC 9899:2024 (C23), CERT C (C99 / C11 / C17 / C23)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`CMake, Meson, GNU Make (`CFLAGS=-std=c11 -O2 -Wall -Wextra -Werror -Wpedantic -Wconversion`).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **C** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **C**.

### Technical Triggers

- Files, build manifests, or prompts targeting **C** (`c11_provenance_arena.c`, `CMake, Meson, GNU Make (`CFLAGS=-std=c11 -O2 -Wall -Wextra -Werror -Wpedantic -Wconversion`).`).

### Prerequisites

- Target language version (C99 / C11 / C17 / C23), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **C** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (C99 / C11 / C17 / C23), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Track object storage duration, pointer provenance (`PNVI-ae-udi`), `_Alignof` alignment, and multiplication overflow (`count > SIZE_MAX / sizeof(T)`) before allocation.), type soundness limits (Honor effective-type strict aliasing (`6.5p7`); inspect raw bytes only via `unsigned char *` or `memcpy`, and use `_Generic` for type-safe macros.), and concurrency hazards (Use `<stdatomic.h>` (`_Atomic`, `memory_order_acquire`/`release`) and `<threads.h>`/POSIX pthreads with strict lock-hierarchy ordering.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 9899:2011 (C11), ISO/IEC 9899:2018 (C17), ISO/IEC 9899:2024 (C23), CERT C.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Enforce sequence-point determinism, explicit integer promotions, and C11/C17/C23 feature gates (`_Static_assert`, `_Alignas`, `nullptr`, `<stdbit.h>`).
2. **Type System & Inference**: Honor effective-type strict aliasing (`6.5p7`); inspect raw bytes only via `unsigned char *` or `memcpy`, and use `_Generic` for type-safe macros.
3. **Memory Management**: Track object storage duration, pointer provenance (`PNVI-ae-udi`), `_Alignof` alignment, and multiplication overflow (`count > SIZE_MAX / sizeof(T)`) before allocation.
4. **Concurrency & Async Programming**: Use `<stdatomic.h>` (`_Atomic`, `memory_order_acquire`/`release`) and `<threads.h>`/POSIX pthreads with strict lock-hierarchy ordering.
5. **Standard Library & Ecosystem**: POSIX.1-2017, libc (`glibc`, `musl`), `pkg-config`, and freestanding `<stdint.h>`/`<stddef.h>` headers.
6. **Build Systems & Package Management**: CMake, Meson, GNU Make (`CFLAGS=-std=c11 -O2 -Wall -Wextra -Werror -Wpedantic -Wconversion`).
7. **Compiler / Interpreter Behavior**: GCC/Clang dead-store elimination (`memset_s`/`explicit_bzero` required for secrets) and UB-driven branch elision.
8. **Debugging & Observability**: GDB hardware watchpoints, `valgrind --track-origins=yes`, `gcc -fanalyzer`, and `-fsanitize=address,undefined`.
9. **Security Hardening**: Prevent buffer overflows (CWE-120), integer wraparound (CWE-190), format-string bugs, and use-after-free (CWE-416).
10. **Performance Optimization**: Cache-line alignment (`_Alignas(64)`), `restrict`-qualified non-aliasing pointers, and arena/slab allocation.
11. **Error Handling Discipline**: Return explicit `enum` status codes (`[[nodiscard]]`), single-exit `goto cleanup` unwind ladders, and errno preservation.
12. **Testing Methodologies**: Deterministic assertion suites, boundary (`0`, `NULL`, `SIZE_MAX`) tests, and LibFuzzer/AFL++ harnesses.
13. **Interoperability & Cross-Platform ABI**: System V AMD64 / AAPCS64 C ABI stability, fixed-width types (`uint32_t`), and opaque struct pointers across shared libraries.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/c-systems-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (C99 / C11 / C17 / C23), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in C**: Signed overflow UB, strict-aliasing punning via `(uint32_t*)ptr`, `sizeof` decay on array parameters, and unchecked `realloc` assignment.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
