---
name: scala-functional-jvm
description: Design, implement, and verify Scala 3 functional and distributed JVM systems using ADTs (enum), opaque types, given/using context parameters, union/intersection types, tailrec, and ZIO/Cats Effect.
allowed-tools: execute_bash view_file write_to_file
---

# Scala 3 (Dotty) Type-Level Engineering, Opaque Types, Given/Using & Effect Systems

Design, implement, and verify Scala 3 functional and distributed JVM systems using ADTs (enum), opaque types, given/using context parameters, union/intersection types, tailrec, and ZIO/Cats Effect.

## A. Identity

- **Skill Name**: `scala-functional-jvm`
- **Domain**: `programming-languages`
- **Language / Representation**: **Scala** (`General-Purpose & Functional Programming Language`)
- **Technical Relationship**: Type-safe functional and object-oriented language on the JVM/Native founded on Dependent Object Types (DOT calculus) in Scala 3.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Scala**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Scala 3 Language Reference (DOT Calculus) (Scala 2.13 / Scala 3.3 LTS / 3.4+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``sbt` (`build.sbt`), Mill, Scala CLI with `-Werror -Wunused:all -Wvalue-discard`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Scala** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Scala**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Scala** (`OpaqueDomainModel.scala`, ``sbt` (`build.sbt`), Mill, Scala CLI with `-Werror -Wunused:all -Wvalue-discard`.`).

### Prerequisites

- Target language version (Scala 2.13 / Scala 3.3 LTS / 3.4+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Scala** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Scala 2.13 / Scala 3.3 LTS / 3.4+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (`opaque type` and `AnyVal` avoiding JVM wrapper allocations; structural sharing in immutable `Vector`/`Map`.), type soundness limits (Union (`A | B`) and intersection (`A & B`) types, match types, higher-kinded types (`F[_]`), and explicit nulls (`-Yexplicit-nulls`).), and concurrency hazards (Fiber-based functional effect systems (Cats Effect `IO`, ZIO) with resource-safe `Resource.make` / `ZIO.acquireRelease`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Scala 3 Language Reference (DOT Calculus).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Scala 3 `enum` ADTs, `opaque type` zero-cost abstractions, `given`/`using` canonical typeclasses, and `@tailrec` verification.
2. **Type System & Inference**: Union (`A | B`) and intersection (`A & B`) types, match types, higher-kinded types (`F[_]`), and explicit nulls (`-Yexplicit-nulls`).
3. **Memory Management**: `opaque type` and `AnyVal` avoiding JVM wrapper allocations; structural sharing in immutable `Vector`/`Map`.
4. **Concurrency & Async Programming**: Fiber-based functional effect systems (Cats Effect `IO`, ZIO) with resource-safe `Resource.make` / `ZIO.acquireRelease`.
5. **Standard Library & Ecosystem**: Cats, Cats Effect, ZIO, FS2, Http4s, Circe, ScalaTest, MUnit, ScalaCheck.
6. **Build Systems & Package Management**: `sbt` (`build.sbt`), Mill, Scala CLI with `-Werror -Wunused:all -Wvalue-discard`.
7. **Compiler / Interpreter Behavior**: TASTy intermediate representation enabling binary compatibility across Scala 3 minor releases; specialization and tail-call elimination.
8. **Debugging & Observability**: Fiber dumps in Cats Effect / ZIO, JFR profiling, and `-Xprint:typer` phase inspection.
9. **Security Hardening**: Enforce total pattern matching (`-Werror` on non-exhaustive match) and refined/opaque validation at serialization boundaries.
10. **Performance Optimization**: Use `@tailrec` for stack-safe recursion, `IArray` for immutable unboxed arrays, and avoid closure allocations in hot loops.
11. **Error Handling Discipline**: Typed error channels (`Either[Err, A]`, `ZIO[R, E, A]`, `ValidatedNec[Err, A]`); ban `.get` on `Option`/`Try`.
12. **Testing Methodologies**: MUnit / ScalaTest + ScalaCheck property-based law verification.
13. **Interoperability & Cross-Platform ABI**: `scala.jdk.CollectionConverters` and `@static` methods for zero-friction Java interop.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/scala-functional-jvm/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Scala 2.13 / Scala 3.3 LTS / 3.4+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Scala**: Calling `Option.get` or `Await.result` blocking thread pools, implicit ambiguity in Scala 2, and accidental boxing in generic collections.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
