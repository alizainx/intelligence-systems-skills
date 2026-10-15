---
name: kotlin-multiplatform-jvm
description: Develop, refactor, debug, and verify Kotlin 2.0+ JVM and Multiplatform systems using strict null-safety, sealed classes, value classes, structured CoroutineScope cancellation, StateFlow/SharedFlow, and @JvmInline zero-allocation wrappers.
allowed-tools: execute_bash view_file write_to_file
---

# Kotlin (K2 / 2.0+) Null Safety, Structured Coroutines, Flows & Multiplatform

Develop, refactor, debug, and verify Kotlin 2.0+ JVM and Multiplatform systems using strict null-safety, sealed classes, value classes, structured CoroutineScope cancellation, StateFlow/SharedFlow, and @JvmInline zero-allocation wrappers.

## A. Identity

- **Skill Name**: `kotlin-multiplatform-jvm`
- **Domain**: `programming-languages`
- **Language / Representation**: **Kotlin** (`General-Purpose Programming Language`)
- **Technical Relationship**: Statically typed language targeting JVM, Android, Kotlin/Native (LLVM), and JS/Wasm with built-in null safety and structured coroutines.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Kotlin**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Kotlin Language Specification (Kotlin 1.9 / 2.0 K2 Compiler) (Kotlin 1.9 / 2.0+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Gradle Kotlin DSL (`build.gradle.kts`), KMP source sets (`commonMain`, `jvmMain`, `nativeMain`), `allWarningsAsErrors = true`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Kotlin** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Kotlin**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Kotlin** (`StructuredFlowWorker.kt`, `Gradle Kotlin DSL (`build.gradle.kts`), KMP source sets (`commonMain`, `jvmMain`, `nativeMain`), `allWarningsAsErrors = true`.`).

### Prerequisites

- Target language version (Kotlin 1.9 / 2.0+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Kotlin** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Kotlin 1.9 / 2.0+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Escape analysis on JVM, `@JvmInline value class` avoiding heap boxing, and Kotlin/Native new memory manager.), type soundness limits (Declaration-site variance (`in T`, `out T`), reified type parameters on `inline fun <reified T>`, and non-nullable platform-type boundary guards.), and concurrency hazards (Structured concurrency via `coroutineScope` / `supervisorScope`, `Dispatcher` isolation, `Mutex` (non-blocking), and cold `Flow` vs hot `StateFlow`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Kotlin Language Specification (Kotlin 1.9 / 2.0 K2 Compiler).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Null-safe types (`T` vs `T?`), smart casts, `sealed interface`/`data class`, `@JvmInline value class`, and extension functions.
2. **Type System & Inference**: Declaration-site variance (`in T`, `out T`), reified type parameters on `inline fun <reified T>`, and non-nullable platform-type boundary guards.
3. **Memory Management**: Escape analysis on JVM, `@JvmInline value class` avoiding heap boxing, and Kotlin/Native new memory manager.
4. **Concurrency & Async Programming**: Structured concurrency via `coroutineScope` / `supervisorScope`, `Dispatcher` isolation, `Mutex` (non-blocking), and cold `Flow` vs hot `StateFlow`.
5. **Standard Library & Ecosystem**: `kotlinx.coroutines`, `kotlinx.serialization`, `ktor`, `detekt`, `ktlint`, MockK.
6. **Build Systems & Package Management**: Gradle Kotlin DSL (`build.gradle.kts`), KMP source sets (`commonMain`, `jvmMain`, `nativeMain`), `allWarningsAsErrors = true`.
7. **Compiler / Interpreter Behavior**: K2 frontend FIR pipeline, `suspend` CPS state-machine continuation lowering, and `inline` lambda inlining (zero `FunctionN` allocation).
8. **Debugging & Observability**: IntelliJ/JDWP coroutine dump (`DebugProbes`), stacktrace recovery (`kotlinx-coroutines-debug`).
9. **Security Hardening**: Never apply the not-null assertion operator `!!` on external or Java platform values (`T!`); validate at the boundary.
10. **Performance Optimization**: Use `Sequence` (`asSequence()`) or `inline` higher-order functions to eliminate intermediate list allocations in collection chains.
11. **Error Handling Discipline**: Rethrow `CancellationException` in `runCatching` / `try-catch` inside `suspend` functions so structured cancellation is never broken!
12. **Testing Methodologies**: `kotlinx-coroutines-test` (`runTest` virtual time scheduler) and Turbine for `Flow` assertion testing.
13. **Interoperability & Cross-Platform ABI**: `@JvmStatic`, `@JvmOverloads`, `@Throws` for idiomatic Java interop, and CInterop for Kotlin/Native.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/kotlin-multiplatform-jvm/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Kotlin 1.9 / 2.0+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Kotlin**: Swallowing `CancellationException` inside `runCatching {}`, launching orphaned coroutines on `GlobalScope`, and capturing mutable state across dispatchers.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
