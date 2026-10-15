---
name: fortran-scientific-systems
description: Develop, modernize, and verify modern Fortran 2008/2018/2023 numerical kernels using implicit none, iso_fortran_env kinds, pure/elemental procedures, column-major stride optimization, Coarray SPMD, and iso_c_binding.
allowed-tools: execute_bash view_file write_to_file
---

# Modern Fortran (2008/2018/2023) Array Computing, Coarrays, OpenMP & ISO_C_BINDING

Develop, modernize, and verify modern Fortran 2008/2018/2023 numerical kernels using implicit none, iso_fortran_env kinds, pure/elemental procedures, column-major stride optimization, Coarray SPMD, and iso_c_binding.

## A. Identity

- **Skill Name**: `fortran-scientific-systems`
- **Domain**: `systems-programming`
- **Language / Representation**: **Fortran** (`Scientific & High-Performance Systems Language`)
- **Technical Relationship**: High-performance numerical and array-computing language (Fortran 2008/2018/2023) with native column-major multidimensional arrays, Coarrays, and `iso_c_binding`.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Fortran**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 1539-1:2018 (Fortran 2018), ISO/IEC 1539-1:2023 (Fortran 2023) (Fortran 2008 / 2018 / 2023)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Fortran Package Manager (`fpm.toml`), CMake, `gfortran -std=f2018 -Wall -Wextra -Werror -fcheck=all -fimplicit-none`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Fortran** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Fortran**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Fortran** (`col_major_spmv.f90`, `Fortran Package Manager (`fpm.toml`), CMake, `gfortran -std=f2018 -Wall -Wextra -Werror -fcheck=all -fimplicit-none`.`).

### Prerequisites

- Target language version (Fortran 2008 / 2018 / 2023), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Fortran** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Fortran 2008 / 2018 / 2023), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Automatic deallocation of local `allocatable` arrays on scope exit (unlike raw `pointer` attributes which leak) and `contiguous` pointer/array guarantees.), type soundness limits (Portable precision via `use, intrinsic :: iso_fortran_env, only: real64, int64`; never use non-portable `REAL*8` or default single precision.), and concurrency hazards (`do concurrent` loop parallelism, native Fortran 2018 Coarrays (`x[i]`, `sync all`), OpenMP, and MPI (`mpi_f08`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 1539-1:2018 (Fortran 2018), ISO/IEC 1539-1:2023 (Fortran 2023).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Free-form `.f90`/`.f08` source, mandatory `implicit none (type, external)`, explicit `intent(in|out|inout)` on all dummy arguments, and `pure`/`elemental` procedures.
2. **Type System & Inference**: Portable precision via `use, intrinsic :: iso_fortran_env, only: real64, int64`; never use non-portable `REAL*8` or default single precision.
3. **Memory Management**: Automatic deallocation of local `allocatable` arrays on scope exit (unlike raw `pointer` attributes which leak) and `contiguous` pointer/array guarantees.
4. **Concurrency & Async Programming**: `do concurrent` loop parallelism, native Fortran 2018 Coarrays (`x[i]`, `sync all`), OpenMP, and MPI (`mpi_f08`).
5. **Standard Library & Ecosystem**: BLAS, LAPACK, FFTW, NetCDF, HDF5, `stdlib` (`fortran-lang`).
6. **Build Systems & Package Management**: Fortran Package Manager (`fpm.toml`), CMake, `gfortran -std=f2018 -Wall -Wextra -Werror -fcheck=all -fimplicit-none`.
7. **Compiler / Interpreter Behavior**: Fortran assumes dummy arguments do not alias, enabling aggressive auto-vectorization without `restrict` keywords.
8. **Debugging & Observability**: `-fcheck=bounds,do,mem,pointer,recursion`, `-ffpe-trap=invalid,zero,overflow`, and GDB array slice inspection.
9. **Security Hardening**: Prevent out-of-bounds array indexing via assumed-shape arrays (`real(real64), intent(in) :: a(:, :)`) instead of legacy assumed-size `a(*)`.
10. **Performance Optimization**: Iterate leftmost index (`i`) in the innermost loop (`A(i, j)`) to match Fortran column-major memory layout (`stride-1`).
11. **Error Handling Discipline**: Inspect `stat=` and `errmsg=` on `allocate`/`deallocate` and check IEEE floating-point exceptions via `ieee_arithmetic`.
12. **Testing Methodologies**: `test-drive` or `pfUnit` assertion suites checking relative `real64` tolerances.
13. **Interoperability & Cross-Platform ABI**: `use, intrinsic :: iso_c_binding` with `bind(C, name="...")` and awareness of transposed C row-major vs Fortran column-major indexing.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/fortran-scientific-systems/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Fortran 2008 / 2018 / 2023), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Fortran**: Initializing module/local variables at declaration (`integer :: n = 0` implicitly adds `save` attribute!), row-major inner loops thrashing L1 cache, and omitting `implicit none`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
