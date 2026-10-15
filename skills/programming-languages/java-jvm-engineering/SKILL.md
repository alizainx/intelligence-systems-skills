---
name: java-jvm-engineering
description: Architect, optimize, debug, and verify Java 17/21+ enterprise and low-latency systems using records, sealed hierarchies, Project Loom virtual threads, Java Memory Model happens-before guarantees, ZGC/G1GC tuning, and Project Panama FFM API.
allowed-tools: execute_bash view_file write_to_file
---

# Java (Java 17/21 LTS) JVM Internals, JMM Concurrency, Virtual Threads & Panama FFI

Architect, optimize, debug, and verify Java 17/21+ enterprise and low-latency systems using records, sealed hierarchies, Project Loom virtual threads, Java Memory Model happens-before guarantees, ZGC/G1GC tuning, and Project Panama FFM API.

## A. Identity

- **Skill Name**: `java-jvm-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **Java** (`General-Purpose Programming Language`)
- **Technical Relationship**: Primary managed language of the Java Virtual Machine (JVM) governed by the Java Language Specification (JLS) and Java Memory Model (JMM).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Java**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Java Language Specification (JLS SE 21), JVM Specification (JVMS SE 21) (Java 17 LTS / Java 21 LTS)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Maven (`pom.xml` with Enforcer plugin) and Gradle (`build.gradle.kts` with version catalogs and reproducible lockfiles).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Java** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Java**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Java** (`SealedOrderState.java`, `Maven (`pom.xml` with Enforcer plugin) and Gradle (`build.gradle.kts` with version catalogs and reproducible lockfiles).`).

### Prerequisites

- Target language version (Java 17 LTS / Java 21 LTS), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Java** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Java 17 LTS / Java 21 LTS), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (JVM heap generations, Escape Analysis scalar replacement, off-heap `Arena` (`java.lang.foreign.MemorySegment`), and low-pause ZGC/G1GC.), type soundness limits (Reified arrays vs type-erased generics (`List<T>`), bounded wildcards (`? extends T` PECS), and `@NullMarked` (JSpecify) nullness annotations.), and concurrency hazards (Java Memory Model (`volatile` acquire/release, `VarHandle`), `CompletableFuture`, `StructuredTaskScope`, and Virtual Threads (`Executors.newVirtualThreadPerTaskExecutor()`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Java Language Specification (JLS SE 21), JVM Specification (JVMS SE 21).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Immutable `record` types, `sealed interface` with exhaustive `switch` pattern matching, and `try-with-resources` (`AutoCloseable`).
2. **Type System & Inference**: Reified arrays vs type-erased generics (`List<T>`), bounded wildcards (`? extends T` PECS), and `@NullMarked` (JSpecify) nullness annotations.
3. **Memory Management**: JVM heap generations, Escape Analysis scalar replacement, off-heap `Arena` (`java.lang.foreign.MemorySegment`), and low-pause ZGC/G1GC.
4. **Concurrency & Async Programming**: Java Memory Model (`volatile` acquire/release, `VarHandle`), `CompletableFuture`, `StructuredTaskScope`, and Virtual Threads (`Executors.newVirtualThreadPerTaskExecutor()`).
5. **Standard Library & Ecosystem**: JDK standard library (`java.util.concurrent`, `java.nio`), JUnit 5, JMH (Java Microbenchmark Harness), Jackson, Netty.
6. **Build Systems & Package Management**: Maven (`pom.xml` with Enforcer plugin) and Gradle (`build.gradle.kts` with version catalogs and reproducible lockfiles).
7. **Compiler / Interpreter Behavior**: `javac -Xlint:all -Werror` bytecode emission followed by HotSpot C1/C2 tiered JIT compilation (`-XX:+PrintCompilation`, inline thresholds).
8. **Debugging & Observability**: JDK Flight Recorder (`jfr`), `jcmd`, `jstack`, Async-Profiler flamegraphs, and JDWP debugger.
9. **Security Hardening**: Prevent JNDI/deserialization RCE (`ObjectInputFilter`), SQL injection (`PreparedStatement`), and XXE in XML parsers.
10. **Performance Optimization**: Avoid autoboxing in hot paths (`IntStream`, primitive collections), prevent Virtual Thread pinning inside `synchronized` blocks (use `ReentrantLock`), and benchmark with JMH.
11. **Error Handling Discipline**: Checked exceptions for recoverable protocol faults, unchecked domain exceptions with context, never swallow `InterruptedException` (restore `Thread.currentThread().interrupt()`).
12. **Testing Methodologies**: JUnit 5 parameterized tests, `jqwik` property tests, and Testcontainers integration harnesses.
13. **Interoperability & Cross-Platform ABI**: Project Panama Foreign Function & Memory (FFM) API (`Linker.nativeLinker()`, `MemorySegment`) replacing unsafe JNI.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/java-jvm-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Java 17 LTS / Java 21 LTS), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Java**: Broken `equals`/`hashCode` contracts on mutable keys, double-checked locking without `volatile`, and pinning carrier threads in Virtual Threads.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
