---
name: racket-language-oriented-programming
description: Design, implement, and verify Racket applications and domain-specific languages (#lang) using syntax/parse macro specifications, define/contract higher-order blame tracking, custodians for resource management, and Typed Racket.
allowed-tools: execute_bash view_file write_to_file
---

# Racket (8.12+) #lang DSLs, syntax/parse Macros, Higher-Order Contracts & Typed Racket

Design, implement, and verify Racket applications and domain-specific languages (#lang) using syntax/parse macro specifications, define/contract higher-order blame tracking, custodians for resource management, and Typed Racket.

## A. Identity

- **Skill Name**: `racket-language-oriented-programming`
- **Domain**: `programming-languages`
- **Language / Representation**: **Racket** (`Language-Oriented & Functional Programming Language`)
- **Technical Relationship**: Descendant of Scheme Built on Chez Scheme runtime, pioneering Language-Oriented Programming (`#lang`), syntax objects with lexical scope sets, and Higher-Order Contracts.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Racket**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: The Racket Reference & Guide (Racket CS 8.12+) (Racket 8.10 / 8.12+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``info.rkt` package metadata, `raco setup`, `raco test`, `raco exe`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Racket** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Racket**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Racket** (`contract_bounded_stack.rkt`, ``info.rkt` package metadata, `raco setup`, `raco test`, `raco exe`.`).

### Prerequisites

- Target language version (Racket 8.10 / 8.12+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Racket** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Racket 8.10 / 8.12+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Chez Scheme generational GC + Racket **Custodians** (`make-custodian`, `custodian-shutdown-all`) guaranteeing deterministic cleanup of ports, threads, and sockets.), type soundness limits (Higher-order runtime contracts (`->i`, `and/c`, `listof`) with precise blame assignment across module boundaries, plus static occurrence typing in `#lang typed/racket`.), and concurrency hazards (Green threads, CML-style synchronizable events (`sync`, `choice-evt`, `handle-evt`, channels, alarms), and OS-level `place` / `future` parallelism.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce The Racket Reference & Guide (Racket CS 8.12+).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit `#lang racket/base` or `#lang typed/racket/base` module header, immutable cons pairs by default (`cons` is immutable; `mcons` is mutable), and `for/fold` comprehensions.
2. **Type System & Inference**: Higher-order runtime contracts (`->i`, `and/c`, `listof`) with precise blame assignment across module boundaries, plus static occurrence typing in `#lang typed/racket`.
3. **Memory Management**: Chez Scheme generational GC + Racket **Custodians** (`make-custodian`, `custodian-shutdown-all`) guaranteeing deterministic cleanup of ports, threads, and sockets.
4. **Concurrency & Async Programming**: Green threads, CML-style synchronizable events (`sync`, `choice-evt`, `handle-evt`, channels, alarms), and OS-level `place` / `future` parallelism.
5. **Standard Library & Ecosystem**: `raco pkg`, `rackunit`, `syntax/parse`, `scribble`, `redex` (operational semantics modeling).
6. **Build Systems & Package Management**: `info.rkt` package metadata, `raco setup`, `raco test`, `raco exe`.
7. **Compiler / Interpreter Behavior**: Set-of-scopes hygiene model (`syntax-parse` syntax classes with automatic error reporting) compiled through Racket's Chez Scheme backend.
8. **Debugging & Observability**: Errortrace source-location stacktraces (`racket -l errortrace -t ...`), Macro Stepper, and Contract profiler (`contract-profile`).
9. **Security Hardening**: Enforce `make-security-guard` and memory-limited custodians (`custodian-limit-memory`) when evaluating untrusted `#lang` modules.
10. **Performance Optimization**: Prefer `#lang racket/base` over full `#lang racket` for fast startup, and avoid high-frequency Typed/Untyped boundary crossings (which wrap values in runtime contract chaperones).
11. **Error Handling Discipline**: `with-handlers` structured exception matching (`exn:fail:contract?`, `exn:fail:filesystem?`).
12. **Testing Methodologies**: `module+ test` submodules with `rackunit` (`check-equal?`, `check-exn`) executed automatically by `raco test`.
13. **Interoperability & Cross-Platform ABI**: `ffi/unsafe` C FFI (`define-cstruct`, `_fun`).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/racket-language-oriented-programming/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Racket 8.10 / 8.12+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Racket**: Crossing Typed Racket <-> Untyped Racket boundaries inside tight inner loops (chaperone overhead), and using legacy `syntax-rules` without `syntax/parse` validation.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
