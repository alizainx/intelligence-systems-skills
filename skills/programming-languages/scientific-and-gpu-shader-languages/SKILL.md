---
name: scientific-and-gpu-shader-languages
description: Engineer and verify GPU compute kernels (CUDA C++, OpenCL), graphics/compute shaders (GLSL, HLSL), and scientific array programs (Julia, R, MATLAB, GNU Octave) enforcing warp coalescing, `+1` shared-memory bank padding, `std140`/`std430` buffer alignment, and type-stable vectorization.
allowed-tools: execute_bash view_file write_to_file
---

# CUDA, OpenCL, GLSL/HLSL Shaders & Scientific Array Languages (Julia, R, MATLAB, Octave)

Engineer and verify GPU compute kernels (CUDA C++, OpenCL), graphics/compute shaders (GLSL, HLSL), and scientific array programs (Julia, R, MATLAB, GNU Octave) enforcing warp coalescing, `+1` shared-memory bank padding, `std140`/`std430` buffer alignment, and type-stable vectorization.

## A. Identity

- **Skill Name**: `scientific-and-gpu-shader-languages`
- **Domain**: `programming-languages`
- **Specialization**: SIMT GPU Kernels, Shared-Memory Bank-Conflict Elimination, Shader Buffer Alignment & Vectorized Array Computing
- **Version**: `1.0.0`
- **Purpose**: Enforce production-grade language semantics, type soundness, memory/resource safety, ABI interoperability, and automated verification.
- **Supported Tasks**: Architecture design, implementation, memory/concurrency auditing, build/toolchain integration, debugging, and verification.
- **Required Knowledge**: NVIDIA CUDA C++ Programming Guide, Khronos OpenCL/GLSL `std140` Spec, Julia Type-Stability Guidelines
- **Dependencies**: Host compilers/interpreters (`gcc`, `g++`, `as`, `ld`, `python3`, `node`, `bash`, `perl`, `sqlite3`) and target CI toolchains.
- **Compatibility Requirements**: Model-agnostic Markdown + executable `tests/run_verification.py` harness.

## B. Activation Criteria

### When to Use

- Activate when writing, refactoring, debugging, optimizing, or auditing code in `SIMT GPU Kernels, Shared-Memory Bank-Conflict Elimination, Shader Buffer Alignment & Vectorized Array Computing`.
- Activate when verifying memory safety, concurrency invariants, build reproducibility, or FFI/ABI boundaries.

### Technical Triggers

- CUDA (`.cu`, `.cuh`), OpenCL (`.cl`), GLSL (`.vert`, `.frag`, `.comp`), HLSL (`.hlsl`), Julia (`.jl`), R (`.R`), MATLAB/Octave (`.m`).

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
5. **Identify Applicable Standards**: Enforce NVIDIA CUDA C++ Programming Guide, Khronos OpenCL/GLSL `std140` Spec, Julia Type-Stability Guidelines.
6. **Separate Known Facts from Assumptions**: Partition verified target platform facts from disclosed assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero sanitizer/memory traps, and 100% pass across nominal, boundary, and adversarial tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 12 mandatory language dimensions:

1. **Syntax & Semantics**: Distinguish SIMT GPU kernels (`__global__`, `__shared__`, `__syncthreads()`) and graphics shaders from host CPU code; pad 2D shared-memory tiles `[32][33]` to eliminate 32-way bank conflicts; preallocate arrays in MATLAB/Octave/R/Julia.
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
python3 skills/programming-languages/scientific-and-gpu-shader-languages/tests/run_verification.py
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
