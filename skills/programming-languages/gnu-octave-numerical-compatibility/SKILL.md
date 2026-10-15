---
name: gnu-octave-numerical-compatibility
description: Write, port, and verify numerical GNU Octave 8.x/9.x scripts and functions maintaining dual Octave/MATLAB portability, strict end-keyword discipline, vectorized BLAS/LAPACK execution, and %!test embedded unit suites.
allowed-tools: execute_bash view_file write_to_file
---

# GNU Octave (8.x/9.x) Portable M-File Engineering, Vectorization & MATLAB Compatibility

Write, port, and verify numerical GNU Octave 8.x/9.x scripts and functions maintaining dual Octave/MATLAB portability, strict end-keyword discipline, vectorized BLAS/LAPACK execution, and %!test embedded unit suites.

## A. Identity

- **Skill Name**: `gnu-octave-numerical-compatibility`
- **Domain**: `programming-languages`
- **Language / Representation**: **GNU Octave** (`Scientific & Numerical Computing Language`)
- **Technical Relationship**: Open-source numerical matrix computing language largely syntax-compatible with MATLAB while adding GNU Octave extensions and `.oct` C++ bindings.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **GNU Octave**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: GNU Octave 8 / 9 Manual, Portable M-File Subset (GNU Octave 8.4 / 9.1+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``pkg` package manager (`DESCRIPTION`, `INDEX`) and `mkoctfile` for native C++/Fortran extensions.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **GNU Octave** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **GNU Octave**.

### Technical Triggers

- Files, build manifests, or prompts targeting **GNU Octave** (`portable_rk4_step.m`, ``pkg` package manager (`DESCRIPTION`, `INDEX`) and `mkoctfile` for native C++/Fortran extensions.`).

### Prerequisites

- Target language version (GNU Octave 8.4 / 9.1+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **GNU Octave** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (GNU Octave 8.4 / 9.1+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Reference-counted copy-on-write `octave_value` containers; preallocate with `zeros`/`NaN`.), type soundness limits (Dense IEEE 754 matrices, sparse CSC matrices (`sparse`), cell arrays, and struct arrays.), and concurrency hazards (`parcellfun` / `pararrayfun` (`parallel` Forge package) and multi-threaded OpenBLAS.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce GNU Octave 8 / 9 Manual, Portable M-File Subset.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Maintain portable `end` (rather than Octave-only `endif`/`endfunction`) and `'...'` single-quoted strings when dual MATLAB compatibility is required.
2. **Type System & Inference**: Dense IEEE 754 matrices, sparse CSC matrices (`sparse`), cell arrays, and struct arrays.
3. **Memory Management**: Reference-counted copy-on-write `octave_value` containers; preallocate with `zeros`/`NaN`.
4. **Concurrency & Async Programming**: `parcellfun` / `pararrayfun` (`parallel` Forge package) and multi-threaded OpenBLAS.
5. **Standard Library & Ecosystem**: Octave Forge (`pkg install -forge control signal optim`), OpenBLAS, SuiteSparse.
6. **Build Systems & Package Management**: `pkg` package manager (`DESCRIPTION`, `INDEX`) and `mkoctfile` for native C++/Fortran extensions.
7. **Compiler / Interpreter Behavior**: AST tree-walker interpreter; vectorization into underlying C++/Fortran BLAS/LAPACK routines is critical because scalar loops are not JIT-compiled.
8. **Debugging & Observability**: `dbstop`, `profile on`, `whos` memory inspection.
9. **Security Hardening**: Validate matrix dimensions (`ismatrix`, `isvector`, ` rows(A) == rows(b)`) and avoid `eval`.
10. **Performance Optimization**: Use `bsxfun` / implicit broadcasting, `accumarray`, and sparse matrices (`speye`, `spdiags`) to avoid scalar `for` loops.
11. **Error Handling Discipline**: `error('id:msg', ...)` and `unwind_protect ... unwind_protect_cleanup ... end_unwind_protect` (or portable `onCleanup`).
12. **Testing Methodologies**: Embedded `%!test` and `%!assert(actual, expected, tol)` blocks executed via `test filename.m`.
13. **Interoperability & Cross-Platform ABI**: `mkoctfile` (`.oct` native C++ API) and `.mex` compatibility API.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/gnu-octave-numerical-compatibility/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (GNU Octave 8.4 / 9.1+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in GNU Octave**: Writing unvectorized scalar loops in Octave, using `+=` or `"double quotes"` in files meant to run in both Octave and MATLAB without checking.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
