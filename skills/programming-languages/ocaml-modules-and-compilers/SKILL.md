---
name: ocaml-modules-and-compilers
description: Design, implement, and verify OCaml 5.x software and compilers using algebraic data types (ADTs), exhaustive pattern matching, module signatures (.mli), parameterized Functors, unboxed float arrays, Menhir/Sedlex compiler frontends, and Multicore Domains/Effects.
allowed-tools: execute_bash view_file write_to_file
---

# OCaml (5.1/5.2+) Algebraic Data Types, Module Functors, Hindley-Milner & Compiler Engineering

Design, implement, and verify OCaml 5.x software and compilers using algebraic data types (ADTs), exhaustive pattern matching, module signatures (.mli), parameterized Functors, unboxed float arrays, Menhir/Sedlex compiler frontends, and Multicore Domains/Effects.

## A. Identity

- **Skill Name**: `ocaml-modules-and-compilers`
- **Domain**: `programming-languages`
- **Language / Representation**: **OCaml** (`Functional & Systems Programming Language`)
- **Technical Relationship**: ML-family statically typed functional language with a fast native-code compiler (`ocamlopt`), parameterized Module Functors, and Multicore Domain/Effect concurrency (OCaml 5).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **OCaml**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: OCaml 5.1 / 5.2 Reference Manual (OCaml 4.14 LTS / OCaml 5.1 / 5.2+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``dune-project`, `dune` stanzas (`(flags (:standard -w +a-4-42-70 -warn-error +a))`), `opam` switch lockfiles.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **OCaml** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **OCaml**.

### Technical Triggers

- Files, build manifests, or prompts targeting **OCaml** (`ssa_expr_simplifier.ml`, ``dune-project`, `dune` stanzas (`(flags (:standard -w +a-4-42-70 -warn-error +a))`), `opam` switch lockfiles.`).

### Prerequisites

- Target language version (OCaml 4.14 LTS / OCaml 5.1 / 5.2+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **OCaml** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (OCaml 4.14 LTS / OCaml 5.1 / 5.2+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Immediate tagged 63-bit integers (`val << 1 | 1`, zero heap boxing!) + generational minor/major GC with very fast bump-pointer minor heap allocation.), type soundness limits (Hindley-Milner principal type inference, polymorphic variants (`` `Tag ``), GADTs, abstract types in `.mli` signatures, and first-class modules.), and concurrency hazards (OCaml 5 Multicore `Domain.spawn` parallelism + algebraic effect handlers (`Effect.Deep` / `Eio` direct-style structured concurrency) or `Lwt`/`Async`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce OCaml 5.1 / 5.2 Reference Manual.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Let-polymorphism (value restriction), exhaustive pattern matching (`match ... with`), tail-call optimization (`[@tail_mod_cons]` / `[@tailcall]`), and labeled/optional arguments.
2. **Type System & Inference**: Hindley-Milner principal type inference, polymorphic variants (`` `Tag ``), GADTs, abstract types in `.mli` signatures, and first-class modules.
3. **Memory Management**: Immediate tagged 63-bit integers (`val << 1 | 1`, zero heap boxing!) + generational minor/major GC with very fast bump-pointer minor heap allocation.
4. **Concurrency & Async Programming**: OCaml 5 Multicore `Domain.spawn` parallelism + algebraic effect handlers (`Effect.Deep` / `Eio` direct-style structured concurrency) or `Lwt`/`Async`.
5. **Standard Library & Ecosystem**: Dune build system, OPAM, `Base`/`Core`, `Eio`, `Menhir`, `Sedlex`, `Alcotest`, `QCheck`.
6. **Build Systems & Package Management**: `dune-project`, `dune` stanzas (`(flags (:standard -w +a-4-42-70 -warn-error +a))`), `opam` switch lockfiles.
7. **Compiler / Interpreter Behavior**: `ocamlopt` Flambda 2 middle-end inlining/unboxing optimizer, uniform value representation, and automatic float array unboxing.
8. **Debugging & Observability**: `ocamldebug` time-travel bytecode debugger, `landmarks`, `memtrace`, and DWARF stack traces in OCaml 5.
9. **Security Hardening**: Opaque abstract types in `.mli` interface files enforcing representation invariants; avoid `Obj.magic` completely.
10. **Performance Optimization**: Annotate recursive functions with `[@tailcall]` or `[@tail_mod_cons]`, use `Bytes`/`Bigarray` for zero-copy buffers, and avoid polymorphic comparison (`=`) on large structures.
11. **Error Handling Discipline**: `('a, 'err) result` with binding operators (`let*`, `let+`) for expected errors and exceptions for programming faults.
12. **Testing Methodologies**: `ppx_inline_test`, `ppx_expect` cram/expectation tests, `Alcotest`, and `QCheck` property testing.
13. **Interoperability & Cross-Platform ABI**: `ctypes` or C stubs with `CAMLparam*` / `CAMLlocal*` / `CAMLreturn` GC root registration macros.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/ocaml-modules-and-compilers/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (OCaml 4.14 LTS / OCaml 5.1 / 5.2+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in OCaml**: Omitting `.mli` interface files (leaking internal type constructors), non-tail-recursive `List.map` on >100k elements without `[@tail_mod_cons]`, and missing `CAMLparam` in C stubs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
