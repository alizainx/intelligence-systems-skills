# Deep Engineering Reference: C# 12 & .NET 8/9 High-Performance Engineering (Span<T>, ref struct, Async & SIMD) (`csharp-dotnet-engineering`)

- **Language / Representation**: **C#**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: Primary language of the Common Language Runtime (.NET 8/9 CLR) with value-type `struct`/`ref struct`, `Span<T>`, and NativeAOT compilation.
- **Governing Standards & Versions**: ECMA-334 C# Language Specification, .NET Runtime ABI (C# 11 / C# 12 (.NET 8 LTS / .NET 9))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **C#** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `<Nullable>enable</Nullable>`, `readonly record struct`, primary constructors, `required` properties, and `using` declarations. |
| 2 | **Type System & Inference** | Value types (`struct`) vs reference types (`class`), stack-only `ref struct` (`Span<T>`), generic math (`INumber<T>`), and pattern matching. |
| 3 | **Memory Management** | Zero-heap slicing with `Span<T>`/`ReadOnlySpan<T>`, `ArrayPool<T>.Shared` pooling, `stackalloc` with small constant bounds, and `IDisposable`/`IAsyncDisposable`. |
| 4 | **Concurrency & Async Programming** | `async`/`await` with `CancellationToken` on every async API, `ValueTask<T>` for synchronous-completion hot paths, and `System.Threading.Channels`. |
| 5 | **Standard Library & Ecosystem** | ASP.NET Core, `System.IO.Pipelines`, xUnit, BenchmarkDotNet, Polly. |
| 6 | **Build Systems & Package Management** | MSBuild (`Directory.Build.props` with `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`), NuGet `packages.lock.json`, NativeAOT. |
| 7 | **Compiler / Interpreter Behavior** | Roslyn source generators (replacing runtime reflection for JSON/DI/Regex) and RyuJIT Dynamic PGO / Tiered Compilation. |
| 8 | **Debugging** | `dotnet-trace`, `dotnet-counters`, `dotnet-dump`, and Visual Studio / LLDB SOS debugging. |
| 9 | **Security** | Source-generated `[GeneratedRegex]` with explicit match timeouts (ReDoS defense) and parameterized ADO.NET/EF Core queries. |
| 10 | **Performance Optimization** | Eliminate LINQ closure allocations in hot loops, use `CollectionsMarshal.AsSpan`, and vectorize with `Vector128<T>`/`Vector256<T>`. |
| 11 | **Error Handling** | Avoid exceptions for expected control flow (`TryParse` / result pattern) and never use `async void`. |
| 12 | **Testing Methodologies** | xUnit + CsCheck/FsCheck property testing + BenchmarkDotNet `[MemoryDiagnoser]` (`0 B` allocated verification). |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (C# 11 / C# 12 (.NET 8 LTS / .NET 9)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Source-generated `[LibraryImport]` (replacing `[DllImport]`) with `UnmanagedCallersOnly` callbacks. |
| 18 | **Common Engineering Mistakes** | `async void` crashing the process, `.Result`/`.Wait()` sync-over-async thread-pool starvation, and reading a `ValueTask` more than once. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/csharp-dotnet-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **C#**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``dotnet-trace`, `dotnet-counters`, `dotnet-dump`, and Visual Studio / LLDB SOS debugging.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `MSBuild (`Directory.Build.props` with `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`), NuGet `packages.lock.json`, NativeAOT.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Eliminate LINQ closure allocations in hot loops, use `CollectionsMarshal.AsSpan`, and vectorize with `Vector128<T>`/`Vector256<T>`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Source-generated `[GeneratedRegex]` with explicit match timeouts (ReDoS defense) and parameterized ADO.NET/EF Core queries.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (xUnit + CsCheck/FsCheck property testing + BenchmarkDotNet `[MemoryDiagnoser]` (`0 B` allocated verification).).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Source-generated `[LibraryImport]` (replacing `[DllImport]`) with `UnmanagedCallersOnly` callbacks.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
