---
name: csharp-dotnet-engineering
description: Engineer, profile, and verify high-performance C# 12 / .NET 8+ systems using nullable reference types, readonly record struct, Span<T>/Memory<T> zero-allocation slicing, ValueTask, System.Threading.Channels, and LibraryImport P/Invoke.
allowed-tools: execute_bash view_file write_to_file
---

# C# 12 & .NET 8/9 High-Performance Engineering (Span<T>, ref struct, Async & SIMD)

Engineer, profile, and verify high-performance C# 12 / .NET 8+ systems using nullable reference types, readonly record struct, Span<T>/Memory<T> zero-allocation slicing, ValueTask, System.Threading.Channels, and LibraryImport P/Invoke.

## A. Identity

- **Skill Name**: `csharp-dotnet-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **C#** (`General-Purpose Programming Language`)
- **Technical Relationship**: Primary language of the Common Language Runtime (.NET 8/9 CLR) with value-type `struct`/`ref struct`, `Span<T>`, and NativeAOT compilation.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **C#**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ECMA-334 C# Language Specification, .NET Runtime ABI (C# 11 / C# 12 (.NET 8 LTS / .NET 9))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`MSBuild (`Directory.Build.props` with `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`), NuGet `packages.lock.json`, NativeAOT.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **C#** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **C#**.

### Technical Triggers

- Files, build manifests, or prompts targeting **C#** (`ZeroAllocSpanParser.cs`, `MSBuild (`Directory.Build.props` with `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`), NuGet `packages.lock.json`, NativeAOT.`).

### Prerequisites

- Target language version (C# 11 / C# 12 (.NET 8 LTS / .NET 9)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **C#** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (C# 11 / C# 12 (.NET 8 LTS / .NET 9)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Zero-heap slicing with `Span<T>`/`ReadOnlySpan<T>`, `ArrayPool<T>.Shared` pooling, `stackalloc` with small constant bounds, and `IDisposable`/`IAsyncDisposable`.), type soundness limits (Value types (`struct`) vs reference types (`class`), stack-only `ref struct` (`Span<T>`), generic math (`INumber<T>`), and pattern matching.), and concurrency hazards (`async`/`await` with `CancellationToken` on every async API, `ValueTask<T>` for synchronous-completion hot paths, and `System.Threading.Channels`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ECMA-334 C# Language Specification, .NET Runtime ABI.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `<Nullable>enable</Nullable>`, `readonly record struct`, primary constructors, `required` properties, and `using` declarations.
2. **Type System & Inference**: Value types (`struct`) vs reference types (`class`), stack-only `ref struct` (`Span<T>`), generic math (`INumber<T>`), and pattern matching.
3. **Memory Management**: Zero-heap slicing with `Span<T>`/`ReadOnlySpan<T>`, `ArrayPool<T>.Shared` pooling, `stackalloc` with small constant bounds, and `IDisposable`/`IAsyncDisposable`.
4. **Concurrency & Async Programming**: `async`/`await` with `CancellationToken` on every async API, `ValueTask<T>` for synchronous-completion hot paths, and `System.Threading.Channels`.
5. **Standard Library & Ecosystem**: ASP.NET Core, `System.IO.Pipelines`, xUnit, BenchmarkDotNet, Polly.
6. **Build Systems & Package Management**: MSBuild (`Directory.Build.props` with `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`), NuGet `packages.lock.json`, NativeAOT.
7. **Compiler / Interpreter Behavior**: Roslyn source generators (replacing runtime reflection for JSON/DI/Regex) and RyuJIT Dynamic PGO / Tiered Compilation.
8. **Debugging & Observability**: `dotnet-trace`, `dotnet-counters`, `dotnet-dump`, and Visual Studio / LLDB SOS debugging.
9. **Security Hardening**: Source-generated `[GeneratedRegex]` with explicit match timeouts (ReDoS defense) and parameterized ADO.NET/EF Core queries.
10. **Performance Optimization**: Eliminate LINQ closure allocations in hot loops, use `CollectionsMarshal.AsSpan`, and vectorize with `Vector128<T>`/`Vector256<T>`.
11. **Error Handling Discipline**: Avoid exceptions for expected control flow (`TryParse` / result pattern) and never use `async void`.
12. **Testing Methodologies**: xUnit + CsCheck/FsCheck property testing + BenchmarkDotNet `[MemoryDiagnoser]` (`0 B` allocated verification).
13. **Interoperability & Cross-Platform ABI**: Source-generated `[LibraryImport]` (replacing `[DllImport]`) with `UnmanagedCallersOnly` callbacks.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/csharp-dotnet-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (C# 11 / C# 12 (.NET 8 LTS / .NET 9)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in C#**: `async void` crashing the process, `.Result`/`.Wait()` sync-over-async thread-pool starvation, and reading a `ValueTask` more than once.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
