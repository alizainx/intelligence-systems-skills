---
name: os-memory-management-vmm-slab-cow
description: Engineer and verify OS physical and virtual memory subsystems including power-of-two buddy allocators, slab caches, 4-level page tables (`W^X`), Copy-on-Write (`CoW`) fork page-fault handlers, and SMP `invlpg`/IPI TLB shootdowns.
allowed-tools: execute_bash view_file write_to_file
---

# OS Memory Management: Buddy, Slab, Page Tables, TLB & Copy-on-Write (CoW)

Engineer and verify OS physical and virtual memory subsystems including power-of-two buddy allocators, slab caches, 4-level page tables (`W^X`), Copy-on-Write (`CoW`) fork page-fault handlers, and SMP `invlpg`/IPI TLB shootdowns.

## A. Identity

- **Skill Name**: `os-memory-management-vmm-slab-cow`
- **Domain**: `operating-systems`
- **Specialization**: Physical Buddy/Slab Allocators, 4-Level Paging, Copy-on-Write Faults & TLB Shootdowns
- **Version**: `1.0.0`
- **Purpose**: Enforce production-grade language semantics, type soundness, memory/resource safety, ABI interoperability, and automated verification.
- **Supported Tasks**: Architecture design, implementation, memory/concurrency auditing, build/toolchain integration, debugging, and verification.
- **Required Knowledge**: x86_64 / ARMv8-A / RISC-V Sv39/Sv48 Paging Architectures
- **Dependencies**: Host compilers/interpreters (`gcc`, `g++`, `as`, `ld`, `python3`, `node`, `bash`, `perl`, `sqlite3`) and target CI toolchains.
- **Compatibility Requirements**: Model-agnostic Markdown + executable `tests/run_verification.py` harness.

## B. Activation Criteria

### When to Use

- Activate when writing, refactoring, debugging, optimizing, or auditing code in `Physical Buddy/Slab Allocators, 4-Level Paging, Copy-on-Write Faults & TLB Shootdowns`.
- Activate when verifying memory safety, concurrency invariants, build reproducibility, or FFI/ABI boundaries.

### Technical Triggers

- Buddy allocator, slab allocator, `CR3`, page fault (`#PF`), Copy-on-Write (`CoW`), TLB shootdown, MMIO `ioremap`.

### Prerequisites

- Target OS, CPU architecture (`x86_64`, `AArch64`, `RISC-V`, `wasm32`), and runtime mode (hosted vs. freestanding).

### When NOT to Use

- Do not conflate full programming languages with hardware description languages (HDLs), query languages, or compiler IRs; route each to its exact specialization.

## C. Problem Understanding

Execute this 8-step intake protocol before generating code:

1. **Identify the Engineering Problem**: Define the exact functional, latency, and resource requirements.
2. **Extract Explicit Requirements**: Record language version, API signatures, and error-handling contracts.
3. **Identify Hidden Technical Constraints**: Surface integer overflow, aliasing, lifetime/GC pressure, nullability, and concurrency hazards.
4. **Determine Environmental Limitations**: Probe whether the native compiler/runtime is installed in the sandbox or requires target-toolchain verification.
5. **Identify Applicable Standards**: Enforce x86_64 / ARMv8-A / RISC-V Sv39/Sv48 Paging Architectures.
6. **Separate Known Facts from Assumptions**: Partition verified target platform facts from disclosed assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero sanitizer/memory traps, and 100% pass across nominal, boundary, and adversarial tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 12 mandatory language dimensions:

1. **Syntax & Semantics**: Decrement shared physical frame reference counts atomically during CoW fault handling, reuse the existing frame in-place when `refcount == 1`, and issue `invlpg` + remote TLB shootdown IPIs whenever downgrading PTE permissions from RW to RO.
2. **Type System**: Enforce strict static typing, exhaustive pattern/union matching, or runtime schema guards.
3. **Memory & Resource Management**: Guarantee deterministic cleanup (RAII, `defer`/`errdefer`, ownership borrow checking, or context managers).
4. **Standard Library Discipline**: Prefer bounds-checked, allocation-explicit standard containers.
5. **Build & Package Management**: Lock dependency hashes and enforce reproducible compiler flags.
6. **Compiler / Interpreter Invocation**: Enable maximum warning and static-analysis gates (`-Wall -Wextra -Werror -Wpedantic -fanalyzer`).
7. **Debugging**: Preserve frame pointers (`-fno-omit-frame-pointer`) and symbol tables (`-g`) for deterministic stack traces.
8. **Testing**: Exercise positive, zero/empty boundary, overflow, and malformed input paths.
9. **Performance Optimization**: Optimize data layout (contiguous arrays/slices) and algorithmic complexity before micro-tuning.
10. **Security Hardening**: Prevent buffer overflows, injection (SQL/shell), and timing side-channels.
11. **Interoperability (FFI / ABI)**: Enforce C ABI layout (`#[repr(C)]` / `extern "C"`), alignment, and panic/exception containment across FFI boundaries.
12. **Production Engineering Practices**: Document operational invariants, complexity bounds, and verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`).

## E. Verification Protocol

### Verification Methods and Test Requirements

Run the automated language verification harness:

```bash
python3 skills/operating-systems/os-memory-management-vmm-slab-cow/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any compiler error, warning under `-Werror`, sanitizer fault, memory leak, or failed unit assertion.
- **Boundary Cases**: Empty/zero-size inputs, maximum type limits (`SIZE_MAX`, `INT64_MAX`, `NaN`), and resource exhaustion.
- **Numerical & Semantic Tolerances**: Exact integer/state equivalence (`0` tolerance) and IEEE 754 relative bounds where applicable.
- **Safety and Performance Criteria**: Deterministic time and space complexity.
- **Reproducibility Requirements**: Log exact tool versions and distinguish native host execution from target-toolchain CI checks in `validation.md`.

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm language version, ABI, and API contracts.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetimes, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile/execute nominal tests.
4. **Stage 4 (Edge-Case Verification)**: Stress-test boundary, overflow, and malformed inputs.
5. **Stage 5 (Independent Review)**: Run orthogonal static analysis (`-fanalyzer` / AST audit) or sanitizer checks (`ASan`/`UBSan`).
6. **Stage 6 (Final Validation)**: Classify as `VERIFIED` (when native compiler/runtime executed) or `PARTIALLY VERIFIED` (when target compiler is absent in VM and verified via AST/behavioral model).

## Gotchas and Error Detection

Report all language defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Silent Integer Overflow & Truncation**: Always guard size multiplications (`count > SIZE_MAX / sizeof(T)`) and narrowing casts.
- **Unchecked FFI Boundary Unwinding**: Never allow exceptions or panics to unwind across an `extern "C"` ABI boundary.
