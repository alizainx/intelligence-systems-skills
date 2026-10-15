---
name: matlab-matrix-numerical-engineering
description: Develop, optimize, and verify MATLAB numerical algorithms and control/signal toolboxes using arguments validation blocks, column-major preallocation, backslash linear solvers (A\b), parfor, and MATLAB Coder (%#codegen) compliance.
allowed-tools: execute_bash view_file write_to_file
---

# MATLAB (R2022b-R2024b+) Vectorized Matrix Algebra, Arguments Validation & Coder Readiness

Develop, optimize, and verify MATLAB numerical algorithms and control/signal toolboxes using arguments validation blocks, column-major preallocation, backslash linear solvers (A\b), parfor, and MATLAB Coder (%#codegen) compliance.

## A. Identity

- **Skill Name**: `matlab-matrix-numerical-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **MATLAB** (`Numerical & Matrix Computing Language`)
- **Technical Relationship**: Proprietary numerical computing environment and matrix language with column-major storage, `arguments` validation blocks, and MEX C/C++/CUDA codegen.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **MATLAB**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: MathWorks MATLAB Language Reference (R2022b-R2024b), MAB Modeling Guidelines (MATLAB R2022b / R2023b / R2024b)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`MATLAB Projects (`.prj`), `buildtool` (`buildfile.m`), `codeIssues` static analyzer (`checkcode`).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **MATLAB** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **MATLAB**.

### Technical Triggers

- Files, build manifests, or prompts targeting **MATLAB** (`damped_least_squares.m`, `MATLAB Projects (`.prj`), `buildtool` (`buildfile.m`), `codeIssues` static analyzer (`checkcode`).`).

### Prerequisites

- Target language version (MATLAB R2022b / R2023b / R2024b), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **MATLAB** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (MATLAB R2022b / R2023b / R2024b), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Copy-on-write array sharing; preallocate outputs via `zeros(N, M, 'like', A)` before any loop.), type soundness limits (Dense `double`/`single`/fixed-point `fi`, `struct`, `table`, `timetable`, and strong classdef value vs `< handle` reference semantics.), and concurrency hazards (Parallel Computing Toolbox `parfor` (loop-variable slicing classification), `spmd`, and `gpuArray`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce MathWorks MATLAB Language Reference (R2022b-R2024b), MAB Modeling Guidelines.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: 1-based column-major arrays, implicit expansion (broadcasting), `arguments ... end` function input validation blocks, and elementwise `.*/./.^` vs matrix `*`/`/`/`^`.
2. **Type System & Inference**: Dense `double`/`single`/fixed-point `fi`, `struct`, `table`, `timetable`, and strong classdef value vs `< handle` reference semantics.
3. **Memory Management**: Copy-on-write array sharing; preallocate outputs via `zeros(N, M, 'like', A)` before any loop.
4. **Concurrency & Async Programming**: Parallel Computing Toolbox `parfor` (loop-variable slicing classification), `spmd`, and `gpuArray`.
5. **Standard Library & Ecosystem**: Control System, Signal Processing, Optimization, Simulink, MATLAB Coder (`%#codegen`), `matlab.unittest`.
6. **Build Systems & Package Management**: MATLAB Projects (`.prj`), `buildtool` (`buildfile.m`), `codeIssues` static analyzer (`checkcode`).
7. **Compiler / Interpreter Behavior**: LXE JIT accelerator + `%#codegen` static type/size inference for C/C++/HDL generation.
8. **Debugging & Observability**: `dbstop if error`, `dbstop if naninf`, Profiler (`profile on; ...; profile viewer`).
9. **Security Hardening**: Avoid `eval`/`feval` with unchecked strings and check matrix conditioning (`rcond(A)`) before solving.
10. **Performance Optimization**: Never compute `inv(A) * b` (always use `A \ b` or `decomposition(A)`), iterate column-major (row index inner, column index outer), and vectorize.
11. **Error Handling Discipline**: `MException('Component:Mnemonic', 'Message %s', detail)` with `try`/`catch ME`.
12. **Testing Methodologies**: `matlab.unittest.TestCase` (`verifyEqual(actual, expected, 'RelTol', 1e-12)`).
13. **Interoperability & Cross-Platform ABI**: MEX C/C++ API (`mexFunction`), `loadlibrary`, and Python/C++ engine interfaces.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/matlab-matrix-numerical-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (MATLAB R2022b / R2023b / R2024b), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in MATLAB**: Using `inv(A)*b` instead of `A\b`, overloading `i` or `j` as loop counters (shadowing imaginary unit; use `1i`), and growing arrays inside loops.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
