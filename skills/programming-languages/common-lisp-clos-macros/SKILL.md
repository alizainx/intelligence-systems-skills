---
name: common-lisp-clos-macros
description: Develop, optimize, and verify ANSI Common Lisp (SBCL) software using deftype/declare (optimize (speed 3) (safety 1)), gensym macro hygiene, CLOS multi-methods, handler-bind/restart-case condition recovery, and ASDF.
allowed-tools: execute_bash view_file write_to_file
---

# Common Lisp (ANSI / SBCL) Type Declarations, CLOS Generic Functions, Condition Restarts & Hygienic Macros

Develop, optimize, and verify ANSI Common Lisp (SBCL) software using deftype/declare (optimize (speed 3) (safety 1)), gensym macro hygiene, CLOS multi-methods, handler-bind/restart-case condition recovery, and ASDF.

## A. Identity

- **Skill Name**: `common-lisp-clos-macros`
- **Domain**: `programming-languages`
- **Language / Representation**: **Common Lisp** (`Multi-Paradigm & Symbolic Functional Programming Language`)
- **Technical Relationship**: ANSI X3.226 image-based compiled Lisp (SBCL) with the Common Lisp Object System (CLOS), condition/restart system, and unboxed native code compilation.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Common Lisp**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ANSI INCITS 226-1994 (R1999) Common Lisp Standard, SBCL User Manual (ANSI Common Lisp (SBCL 2.3 / 2.4+))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``.asd` system definitions (`:serial t` or package-inferred systems) and standalone binaries via `(sb-ext:save-lisp-and-die ... :executable t)`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Common Lisp** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Common Lisp**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Common Lisp** (`safe_sexp_reader.lisp`, ``.asd` system definitions (`:serial t` or package-inferred systems) and standalone binaries via `(sb-ext:save-lisp-and-die ... :executable t)`.`).

### Prerequisites

- Target language version (ANSI Common Lisp (SBCL 2.3 / 2.4+)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Common Lisp** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (ANSI Common Lisp (SBCL 2.3 / 2.4+)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (SBCL generational GC, `dynamic-extent` stack allocation declarations, and typed unboxed arrays (`(simple-array double-float (*))`).), type soundness limits (Dynamic typing with optional gradual static type inference and compilation notes in SBCL (`declaim (ftype (function (fixnum fixnum) fixnum) ...)`).), and concurrency hazards (`bordeaux-threads`, `lparallel` worker pools, and `sb-concurrency` lock-free queues/mailboxes.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ANSI INCITS 226-1994 (R1999) Common Lisp Standard, SBCL User Manual.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Lisp-2 namespace (`#'fn` vs variable value), lexical scope by default (`defparameter`/`defvar` earmarked `*special*`), and homoiconic S-expression macros (`defmacro`).
2. **Type System & Inference**: Dynamic typing with optional gradual static type inference and compilation notes in SBCL (`declaim (ftype (function (fixnum fixnum) fixnum) ...)`).
3. **Memory Management**: SBCL generational GC, `dynamic-extent` stack allocation declarations, and typed unboxed arrays (`(simple-array double-float (*))`).
4. **Concurrency & Async Programming**: `bordeaux-threads`, `lparallel` worker pools, and `sb-concurrency` lock-free queues/mailboxes.
5. **Standard Library & Ecosystem**: ASDF 3 build system, Quicklisp / Qlot (`qlfile.lock`), Alexandria, Serapeum, FiveAM, Coalton.
6. **Build Systems & Package Management**: `.asd` system definitions (`:serial t` or package-inferred systems) and standalone binaries via `(sb-ext:save-lisp-and-die ... :executable t)`.
7. **Compiler / Interpreter Behavior**: SBCL Python compiler emitting native machine code directly; inspect disassembly via `(disassemble #'fn)` and resolve all compiler efficiency notes.
8. **Debugging & Observability**: SLIME/SLY interactive inspector, stack frame restartable debugger, and `sb-sprof` statistical profiler.
9. **Security Hardening**: Set `*read-eval*` to `nil` (`(with-standard-io-syntax (let ((*read-eval* nil)) (read ...)))`) before reading untrusted S-expressions to prevent `#.` reader macro RCE!
10. **Performance Optimization**: Prevent variable capture in macros using `gensym` / `alexandria:with-unique-names`, declare `(type (simple-array ...))`, and avoid `(safety 0)` in production.
11. **Error Handling Discipline**: Separate mechanism from policy using Common Lisp's Condition System (`signal`, `error`, `restart-case`, `handler-bind`, `handler-case`).
12. **Testing Methodologies**: `FiveAM` / `Parachute` / `Rove` test suites run via `(asdf:test-system :my-sys)`.
13. **Interoperability & Cross-Platform ABI**: CFFI (`cffi:defcfun`, `cffi:with-foreign-object`) portable across SBCL, CCL, and ECL.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/common-lisp-clos-macros/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (ANSI Common Lisp (SBCL 2.3 / 2.4+)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Common Lisp**: Mutating quoted literal constants (`'(1 2 3)`), variable capture in `defmacro` without `gensym`, and leaving `*read-eval*` true on external inputs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
