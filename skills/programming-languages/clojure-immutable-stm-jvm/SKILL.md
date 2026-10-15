---
name: clojure-immutable-stm-jvm
description: Engineer, optimize, and verify Clojure JVM systems using persistent immutable vectors/maps, transducers, Atoms/Refs/Agents concurrency, clojure.spec/Malli data validation, and zero-reflection type hints.
allowed-tools: execute_bash view_file write_to_file
---

# Clojure (1.11/1.12+) Persistent Data Structures, Transducers, STM Refs/Atoms & Spec

Engineer, optimize, and verify Clojure JVM systems using persistent immutable vectors/maps, transducers, Atoms/Refs/Agents concurrency, clojure.spec/Malli data validation, and zero-reflection type hints.

## A. Identity

- **Skill Name**: `clojure-immutable-stm-jvm`
- **Domain**: `programming-languages`
- **Language / Representation**: **Clojure** (`Functional Lisp on the JVM`)
- **Technical Relationship**: Dynamic functional Lisp hosted on the JVM (and JS via ClojureScript) built around Persistent HAMT Data Structures, Software Transactional Memory (STM), and `core.async`.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Clojure**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Clojure 1.11 / 1.12 Reference & clojure.spec Guide (Clojure 1.11 / 1.12 (JVM 17 / 21 LTS))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``deps.edn`, `tools.build` (`uber` JAR compilation with AOT main), `clj-kondo` static linter.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Clojure** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Clojure**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Clojure** (`transducer_stm_ledger.clj`, ``deps.edn`, `tools.build` (`uber` JAR compilation with AOT main), `clj-kondo` static linter.`).

### Prerequisites

- Target language version (Clojure 1.11 / 1.12 (JVM 17 / 21 LTS)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Clojure** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Clojure 1.11 / 1.12 (JVM 17 / 21 LTS)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (32-way branching Persistent Hash Array Mapped Tries (HAMT) with structural sharing + `transient`/`persistent!` batch mutation optimization.), type soundness limits (Dynamic data schemas validated via `malli` or `clojure.spec.alpha` (`s/def`, `s/valid?`, `s/conform`) + compile-time JVM reflection warnings (`(set! *warn-on-reflection* true)`).), and concurrency hazards (Unshared synchronous state via `atom` (`swap!`), coordinated synchronous state via STM `ref` (`dosync`, `alter`, `commute`), asynchronous `agent`, and `core.async` channels.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Clojure 1.11 / 1.12 Reference & clojure.spec Guide.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Data-oriented EDN literals (`{:k v}`, `[1 2]`, `#{:a}`), `loop`/`recur` explicit tail recursion, destructuring, and namespace-qualified keywords (`::order/id`).
2. **Type System & Inference**: Dynamic data schemas validated via `malli` or `clojure.spec.alpha` (`s/def`, `s/valid?`, `s/conform`) + compile-time JVM reflection warnings (`(set! *warn-on-reflection* true)`).
3. **Memory Management**: 32-way branching Persistent Hash Array Mapped Tries (HAMT) with structural sharing + `transient`/`persistent!` batch mutation optimization.
4. **Concurrency & Async Programming**: Unshared synchronous state via `atom` (`swap!`), coordinated synchronous state via STM `ref` (`dosync`, `alter`, `commute`), asynchronous `agent`, and `core.async` channels.
5. **Standard Library & Ecosystem**: `deps.edn` (Tools.deps), Leiningen, Ring, Reitit, Next.jdbc, Malli, Integrant, `clojure.test`, `test.check`.
6. **Build Systems & Package Management**: `deps.edn`, `tools.build` (`uber` JAR compilation with AOT main), `clj-kondo` static linter.
7. **Compiler / Interpreter Behavior**: Direct JVM bytecode compiler (no interpreter); lazy sequence chunking (32 elements at a time) and reflection fallback (~50x slower if unhinted).
8. **Debugging & Observability**: CIDER / Calva REPL inspection, `clj-async-profiler`, and `portal` data navigator.
9. **Security Hardening**: Always use `clojure.edn/read-string` instead of `clojure.core/read-string` on external input (`clojure.core/read-string` can execute arbitrary Java constructors via `#=(...)`!).
10. **Performance Optimization**: Eliminate reflection with `^String` / `^long` type hints, use Transducers (`(transduce (comp (filter odd?) (map inc)) + 0 coll)`) to avoid lazy-seq allocation, and `reduce-kv`.
11. **Error Handling Discipline**: `ex-info` / `ex-data` structured map exceptions or anomaly maps (`:cognitect.anomalies/category`).
12. **Testing Methodologies**: `clojure.test` (`deftest`, `is`, `testing`) + `clojure.test.check` generative property tests.
13. **Interoperability & Cross-Platform ABI**: Direct Java method/constructor interop (`(.method ^TargetType obj arg)`, `reify`, `proxy`) and Java 21 Virtual Threads.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/clojure-immutable-stm-jvm/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Clojure 1.11 / 1.12 (JVM 17 / 21 LTS)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Clojure**: Side effects inside `swap!` or `dosync` (which may retry multiple times under contention!), holding onto the head of a large lazy sequence, and using `clojure.core/read-string` on untrusted text.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
