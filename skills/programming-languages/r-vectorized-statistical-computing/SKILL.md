---
name: r-vectorized-statistical-computing
description: Engineer, profile, and verify reproducible R 4.3+ statistical and data-science packages using vectorized operations, type-stable vapply, explicit NA/NaN handling, copy-on-modify awareness, renv lockfiles, and testthat.
allowed-tools: execute_bash view_file write_to_file
---

# R (4.3/4.4+) Vectorization, Type-Stable vapply, Copy-on-Modify, Rcpp & renv

Engineer, profile, and verify reproducible R 4.3+ statistical and data-science packages using vectorized operations, type-stable vapply, explicit NA/NaN handling, copy-on-modify awareness, renv lockfiles, and testthat.

## A. Identity

- **Skill Name**: `r-vectorized-statistical-computing`
- **Domain**: `programming-languages`
- **Language / Representation**: **R** (`Statistical & Scientific Computing Language`)
- **Technical Relationship**: Functional array/vector language with copy-on-modify SEXP semantics, S3/S4/R7 object systems, and C/C++ (`Rcpp`/`cpp11`) native interfaces.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **R**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: R Language Definition (R 4.3 / 4.4), CRAN Repository Policy, Tidyverse Design Guide (R 4.2 / 4.3 / 4.4+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``DESCRIPTION` + `NAMESPACE` (`R CMD build`, `R CMD check --as-cran`), `renv.lock` reproducibility.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **R** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **R**.

### Technical Triggers

- Files, build manifests, or prompts targeting **R** (`type_stable_summary.R`, ``DESCRIPTION` + `NAMESPACE` (`R CMD build`, `R CMD check --as-cran`), `renv.lock` reproducibility.`).

### Prerequisites

- Target language version (R 4.2 / 4.3 / 4.4+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **R** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (R 4.2 / 4.3 / 4.4+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Copy-on-modify `SEXP` reference tracking (`lobstr::obj_addr`); preallocate vectors (`numeric(n)`, `vector("list", n)`) instead of growing via `c(x, val)` in loops.), type soundness limits (Atomic vectors (`logical`, `integer`, `double`, `character`, `raw`), S3/S4/R7 classes, and `vctrs` strict type/size stability.), and concurrency hazards (`future` / `furrr` / `parallel::mclapply` process pools and OpenMP inside `Rcpp` / `data.table`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce R Language Definition (R 4.3 / 4.4), CRAN Repository Policy, Tidyverse Design Guide.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: 1-based indexing, native pipe `|>`, `seq_len(n)` / `seq_along(x)` (never `1:length(x)` which yields `c(1, 0)` when empty!), and `TRUE`/`FALSE` (never `T`/`F`).
2. **Type System & Inference**: Atomic vectors (`logical`, `integer`, `double`, `character`, `raw`), S3/S4/R7 classes, and `vctrs` strict type/size stability.
3. **Memory Management**: Copy-on-modify `SEXP` reference tracking (`lobstr::obj_addr`); preallocate vectors (`numeric(n)`, `vector("list", n)`) instead of growing via `c(x, val)` in loops.
4. **Concurrency & Async Programming**: `future` / `furrr` / `parallel::mclapply` process pools and OpenMP inside `Rcpp` / `data.table`.
5. **Standard Library & Ecosystem**: `data.table`, `vctrs`, `rlang`, `Rcpp`/`cpp11`, `testthat`, `renv`, `lintr`, `roxygen2`.
6. **Build Systems & Package Management**: `DESCRIPTION` + `NAMESPACE` (`R CMD build`, `R CMD check --as-cran`), `renv.lock` reproducibility.
7. **Compiler / Interpreter Behavior**: Bytecode compiler (`compiler::cmpfun` enabled by default) and ALTREP compact lazy representations.
8. **Debugging & Observability**: `traceback()`, `browser()`, `options(error = recover)`, `profvis`, and `R -d valgrind` for C/Rcpp extensions.
9. **Security Hardening**: Avoid `eval(parse(text = ...))` on external strings and set `stringsAsFactors = FALSE` / explicit `colClasses`.
10. **Performance Optimization**: Replace `sapply` with type-checked `vapply(X, FUN, FUN.VALUE)`, use matrix algebra (`crossprod(X, y)` instead of `t(X) %*% y`), and `data.table` reference semantics (`:=`).
11. **Error Handling Discipline**: Structured condition signaling via `rlang::abort(message, class = "...")` and `tryCatch()`.
12. **Testing Methodologies**: `testthat` Edition 3 (`expect_identical`, `expect_s3_class`, `expect_error(..., class = ...)`).
13. **Interoperability & Cross-Platform ABI**: `.Call` C interface and `cpp11` / `Rcpp` C++ bindings.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/r-vectorized-statistical-computing/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (R 4.2 / 4.3 / 4.4+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in R**: Using `1:nrow(df)` when `nrow(df) == 0`, using `sapply` (silently returns `list` or `matrix` depending on data), and `df[, cols]` dropping dimensions without `drop = FALSE`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
