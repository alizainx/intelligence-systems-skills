---
name: fsharp-dotnet-functional
description: Engineer and verify F# 8 functional domain models and financial/scientific systems on .NET 8 using Discriminated Unions, [<Measure>] dimensional analysis, Computation Expressions (task/async/result), and [<TailCall>] verification.
allowed-tools: execute_bash view_file write_to_file
---

# F# (F# 8 / .NET 8) Discriminated Unions, Units of Measure, Computation Expressions & Struct ADTs

Engineer and verify F# 8 functional domain models and financial/scientific systems on .NET 8 using Discriminated Unions, [<Measure>] dimensional analysis, Computation Expressions (task/async/result), and [<TailCall>] verification.

## A. Identity

- **Skill Name**: `fsharp-dotnet-functional`
- **Domain**: `programming-languages`
- **Language / Representation**: **F#** (`Functional-First Programming Language (.NET CLR)`)
- **Technical Relationship**: ML-family functional-first language on the .NET CLR with Units of Measure, Computation Expressions, and `[<Struct>]` Discriminated Unions.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **F#**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: F# 8.0 Language Specification (.NET 8 CLR) (F# 7.0 / F# 8.0)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`MSBuild `.fsproj` with explicit top-down `<Compile Include="..." />` ordering and `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **F#** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **F#**.

### Technical Triggers

- Files, build manifests, or prompts targeting **F#** (`UnitsOfMeasureKinematics.fs`, `MSBuild `.fsproj` with explicit top-down `<Compile Include="..." />` ordering and `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.`).

### Prerequisites

- Target language version (F# 7.0 / F# 8.0), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **F#** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (F# 7.0 / F# 8.0), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (`[<Struct>]` records, tuples, and single/multi-case Discriminated Unions to avoid CLR heap allocations on hot paths.), type soundness limits (Hindley-Milner inference, Discriminated Unions, Record types with structural equality, and zero-cost compile-time Units of Measure (`[<Measure>] type sec`).), and concurrency hazards (`task { ... }` (zero-overhead .NET `Task<T>` state machine), `async { ... }` with cancellation tokens, and `MailboxProcessor<'Msg>` actors.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce F# 8.0 Language Specification (.NET 8 CLR).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Immutable bindings by default (`let`), significant whitespace, pipeline operator (`|>`), `.fsi` signature files, and strict file compilation order in `.fsproj`.
2. **Type System & Inference**: Hindley-Milner inference, Discriminated Unions, Record types with structural equality, and zero-cost compile-time Units of Measure (`[<Measure>] type sec`).
3. **Memory Management**: `[<Struct>]` records, tuples, and single/multi-case Discriminated Unions to avoid CLR heap allocations on hot paths.
4. **Concurrency & Async Programming**: `task { ... }` (zero-overhead .NET `Task<T>` state machine), `async { ... }` with cancellation tokens, and `MailboxProcessor<'Msg>` actors.
5. **Standard Library & Ecosystem**: `FSharp.Core`, `FsToolkit.ErrorHandling`, `Expecto`, `FsCheck`, `Giraffe`.
6. **Build Systems & Package Management**: MSBuild `.fsproj` with explicit top-down `<Compile Include="..." />` ordering and `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.
7. **Compiler / Interpreter Behavior**: F# 8 `[<TailCall>]` attribute warning (`FS3569`) if a recursive function is not compiled as a tail call.
8. **Debugging & Observability**: `dotnet-trace`, Ionide/VS debugger, and ILSpy decompilation of generated CLR classes.
9. **Security Hardening**: Make illegal states unrepresentable via single-case union wrappers (`type EmailAddress = private EmailAddress of string`) with smart constructors.
10. **Performance Optimization**: `inline` functions with Statically Resolved Type Parameters (`^T`), `Span<'T>`, and `[<Struct>]` DUs.
11. **Error Handling Discipline**: `Result<'T, 'Error>` computation expressions (`result { let! x = ... }`) instead of exceptions for domain validation.
12. **Testing Methodologies**: Expecto + FsCheck property-based testing.
13. **Interoperability & Cross-Platform ABI**: Seamless consumption of C#/.NET libraries; guard incoming `null` references from C# with `Option.ofObj` or F# 9 nullable reference support.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/fsharp-dotnet-functional/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (F# 7.0 / F# 8.0), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in F#**: Mixing physical meters and seconds without `[<Measure>]` annotations, accidental non-tail recursion without `[<TailCall>]`, and unhandled `null` from C# APIs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
