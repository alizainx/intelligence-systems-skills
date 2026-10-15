---
name: scheme-continuations-hygienic-macros
description: Write, analyze, and verify R6RS/R7RS Scheme programs using proper tail recursion, syntax-rules/syntax-case hygienic macros, dynamic-wind resource safety, SRFI libraries, and Chez/Guile optimization.
allowed-tools: execute_bash view_file write_to_file
---

# Scheme (R6RS/R7RS / Chez / Guile) Proper Tail Calls, Hygienic Macros & Delimited Continuations

Write, analyze, and verify R6RS/R7RS Scheme programs using proper tail recursion, syntax-rules/syntax-case hygienic macros, dynamic-wind resource safety, SRFI libraries, and Chez/Guile optimization.

## A. Identity

- **Skill Name**: `scheme-continuations-hygienic-macros`
- **Domain**: `programming-languages`
- **Language / Representation**: **Scheme** (`Functional Programming Language`)
- **Technical Relationship**: Minimalist lexical-scoped Lisp dialect (R6RS / R7RS-small / Chez Scheme / Guile) guaranteeing proper tail recursion and hygienic `syntax-rules` / `syntax-case` macros.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Scheme**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: IEEE Std 1178, R6RS, R7RS-small, SRFI Specifications (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`R7RS `(define-library ... (import (scheme base)) (export ...))` or R6RS `(library ...)`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Scheme** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Scheme**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Scheme** (`tailrec_ring_checksum.scm`, `R7RS `(define-library ... (import (scheme base)) (export ...))` or R6RS `(library ...)`.`).

### Prerequisites

- Target language version (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Scheme** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Generational copying GC (Chez Scheme) / BDW or precise GC; use `bytevector` for unboxed binary data.), type soundness limits (Latent dynamic types with disjoint predicates (`pair?`, `vector?`, `bytevector?`, `procedure?`) and numerical tower (`exact` rationals/bignums vs `inexact` floats).), and concurrency hazards (Fibers (Guile delimited continuations `call-with-prompt`), SRFI-18 threads, and Chez SMP threads.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce IEEE Std 1178, R6RS, R7RS-small, SRFI Specifications.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Lisp-1 single namespace, mandatory proper tail-call optimization (TCO), named `let` iteration, and `define-record-type` (SRFI-9 / R7RS).
2. **Type System & Inference**: Latent dynamic types with disjoint predicates (`pair?`, `vector?`, `bytevector?`, `procedure?`) and numerical tower (`exact` rationals/bignums vs `inexact` floats).
3. **Memory Management**: Generational copying GC (Chez Scheme) / BDW or precise GC; use `bytevector` for unboxed binary data.
4. **Concurrency & Async Programming**: Fibers (Guile delimited continuations `call-with-prompt`), SRFI-18 threads, and Chez SMP threads.
5. **Standard Library & Ecosystem**: SRFIs (`srfi-1` lists, `srfi-64` testing, `srfi-145` assumptions), Akku.scm / Guild.
6. **Build Systems & Package Management**: R7RS `(define-library ... (import (scheme base)) (export ...))` or R6RS `(library ...)`.
7. **Compiler / Interpreter Behavior**: Chez Scheme nanopass compiler framework (50+ fine-grained intermediate IR passes) and Call-with-Current-Continuation (`call/cc`) stack segment copying.
8. **Debugging & Observability**: Chez `debug-on-exception`, trace macros (`trace-lambda`), and Guile `,bt` / `,locals` REPL meta-commands.
9. **Security Hardening**: Use `dynamic-wind` (in, body, out thunks) so resource cleanup runs even when continuations jump out of a dynamic extent.
10. **Performance Optimization**: Prefer delimited prompts or tail-recursive accumulator passing over full `call/cc` capture, and use fixnum/flonum operations (`fx+`, `fl+` in R6RS/Chez).
11. **Error Handling Discipline**: R6RS/R7RS `guard` and `with-exception-handler` condition hierarchies.
12. **Testing Methodologies**: SRFI-64 (`test-begin`, `test-equal`, `test-error`, `test-end`) portable test suites.
13. **Interoperability & Cross-Platform ABI**: Chez `foreign-procedure` and Guile `(system foreign)` C FFI.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/scheme-continuations-hygienic-macros/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Scheme**: Using `set-car!`/`set-cdr!` on quoted literal lists, capturing full `call/cc` continuations inside C FFI callbacks, and non-tail recursion.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
