---
name: julia-multiple-dispatch-hpc
description: Develop, profile, and verify high-performance Julia 1.10+ scientific computing software with strict type stability (@code_warntype), symmetric multiple dispatch, @views zero-copy array slicing, column-major loop order, and Project.toml reproducibility.
allowed-tools: execute_bash view_file write_to_file
---

# Julia (1.10 LTS+) Multiple Dispatch, Type Stability (@code_warntype), @views & SIMD

Develop, profile, and verify high-performance Julia 1.10+ scientific computing software with strict type stability (@code_warntype), symmetric multiple dispatch, @views zero-copy array slicing, column-major loop order, and Project.toml reproducibility.

## A. Identity

- **Skill Name**: `julia-multiple-dispatch-hpc`
- **Domain**: `programming-languages`
- **Language / Representation**: **Julia** (`Scientific & High-Performance Numerical Programming Language`)
- **Technical Relationship**: LLVM JIT-compiled scientific language organized around symmetric Multiple Dispatch, parametric type stability, and column-major multidimensional arrays.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Julia**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Julia 1.10 LTS Documentation, SciML Style Guide (Julia 1.10 LTS / 1.11+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``julia --project=. -e 'using Pkg; Pkg.instantiate(); Pkg.test()'`, `PackageCompiler.jl` sysimages.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Julia** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Julia**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Julia** (`type_stable_stencil.jl`, ``julia --project=. -e 'using Pkg; Pkg.instantiate(); Pkg.test()'`, `PackageCompiler.jl` sysimages.`).

### Prerequisites

- Target language version (Julia 1.10 LTS / 1.11+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Julia** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Julia 1.10 LTS / 1.11+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Generational mark-sweep GC; preallocate output arrays with `mul!(Y, A, B)` / `.=` in-place broadcasting to achieve 0-byte loop allocations.), type soundness limits (Concrete types are final (only abstract types can be subtyped); never use abstract field types (`x::Real`) inside structs (boxes every field access on the heap!).), and concurrency hazards (`Threads.@threads`, `Threads.@spawn` work-stealing tasks, `FLoops.jl`, and `CUDA.jl` / `AMDGPU.jl` / `KernelAbstractions.jl`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Julia 1.10 LTS Documentation, SciML Style Guide.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: 1-based column-major indexing, dot-broadcasting fusion (`y .= a .* x .+ b`), `@views` zero-allocation array slicing, and parametric structs (`struct Mesh{T<:AbstractFloat}`).
2. **Type System & Inference**: Concrete types are final (only abstract types can be subtyped); never use abstract field types (`x::Real`) inside structs (boxes every field access on the heap!).
3. **Memory Management**: Generational mark-sweep GC; preallocate output arrays with `mul!(Y, A, B)` / `.=` in-place broadcasting to achieve 0-byte loop allocations.
4. **Concurrency & Async Programming**: `Threads.@threads`, `Threads.@spawn` work-stealing tasks, `FLoops.jl`, and `CUDA.jl` / `AMDGPU.jl` / `KernelAbstractions.jl`.
5. **Standard Library & Ecosystem**: `Pkg` (`Project.toml`, `Manifest.toml`), `LinearAlgebra`, `StaticArrays.jl`, `BenchmarkTools.jl`, `Test`, `JET.jl`, `Aqua.jl`.
6. **Build Systems & Package Management**: `julia --project=. -e 'using Pkg; Pkg.instantiate(); Pkg.test()'`, `PackageCompiler.jl` sysimages.
7. **Compiler / Interpreter Behavior**: Method specialization per concrete argument tuple; dynamic dispatch fallback occurs if return types depend on runtime values (`@code_warntype` red `Any`/`Union`).
8. **Debugging & Observability**: `@code_warntype`, `JET.@report_opt` static type-instability analyzer, `Debugger.jl`, and `@profview`.
9. **Security Hardening**: Avoid `@eval` on external strings and validate dimensions before `@inbounds`.
10. **Performance Optimization**: Never access non-`const` global variables inside hot functions; iterate column-major (`for j in axes(A,2), i in axes(A,1)`), and use `SVector` (`StaticArrays`) for small fixed vectors.
11. **Error Handling Discipline**: `DomainError`, `DimensionMismatch`, `BoundsError` with `@boundscheck` propagation (`Base.@propagate_inbounds`).
12. **Testing Methodologies**: `using Test` (`@testset`, `@test`, `@test_throws`, `@inferred` return-type stability assertion!).
13. **Interoperability & Cross-Platform ABI**: Zero-overhead `@ccall` / `ccall((:func, "lib"), Cdouble, (Cdouble,), x)` C/Fortran FFI.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/julia-multiple-dispatch-hpc/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Julia 1.10 LTS / 1.11+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Julia**: Abstractly typed struct fields (`struct Bad; x::AbstractFloat; end`), row-major inner loops, slicing arrays without `@views`, and omitting `@inferred` in tests.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
