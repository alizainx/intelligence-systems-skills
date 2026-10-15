# Deep Engineering Reference: F# (F# 8 / .NET 8) Discriminated Unions, Units of Measure, Computation Expressions & Struct ADTs (`fsharp-dotnet-functional`)

- **Language / Representation**: **F#**
- **Taxonomic Classification**: `Functional-First Programming Language (.NET CLR)`
- **Technical Relationship**: ML-family functional-first language on the .NET CLR with Units of Measure, Computation Expressions, and `[<Struct>]` Discriminated Unions.
- **Governing Standards & Versions**: F# 8.0 Language Specification (.NET 8 CLR) (F# 7.0 / F# 8.0)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **F#** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Immutable bindings by default (`let`), significant whitespace, pipeline operator (`|>`), `.fsi` signature files, and strict file compilation order in `.fsproj`. |
| 2 | **Type System & Inference** | Hindley-Milner inference, Discriminated Unions, Record types with structural equality, and zero-cost compile-time Units of Measure (`[<Measure>] type sec`). |
| 3 | **Memory Management** | `[<Struct>]` records, tuples, and single/multi-case Discriminated Unions to avoid CLR heap allocations on hot paths. |
| 4 | **Concurrency & Async Programming** | `task { ... }` (zero-overhead .NET `Task<T>` state machine), `async { ... }` with cancellation tokens, and `MailboxProcessor<'Msg>` actors. |
| 5 | **Standard Library & Ecosystem** | `FSharp.Core`, `FsToolkit.ErrorHandling`, `Expecto`, `FsCheck`, `Giraffe`. |
| 6 | **Build Systems & Package Management** | MSBuild `.fsproj` with explicit top-down `<Compile Include="..." />` ordering and `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`. |
| 7 | **Compiler / Interpreter Behavior** | F# 8 `[<TailCall>]` attribute warning (`FS3569`) if a recursive function is not compiled as a tail call. |
| 8 | **Debugging** | `dotnet-trace`, Ionide/VS debugger, and ILSpy decompilation of generated CLR classes. |
| 9 | **Security** | Make illegal states unrepresentable via single-case union wrappers (`type EmailAddress = private EmailAddress of string`) with smart constructors. |
| 10 | **Performance Optimization** | `inline` functions with Statically Resolved Type Parameters (`^T`), `Span<'T>`, and `[<Struct>]` DUs. |
| 11 | **Error Handling** | `Result<'T, 'Error>` computation expressions (`result { let! x = ... }`) instead of exceptions for domain validation. |
| 12 | **Testing Methodologies** | Expecto + FsCheck property-based testing. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (F# 7.0 / F# 8.0); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Seamless consumption of C#/.NET libraries; guard incoming `null` references from C# with `Option.ofObj` or F# 9 nullable reference support. |
| 18 | **Common Engineering Mistakes** | Mixing physical meters and seconds without `[<Measure>]` annotations, accidental non-tail recursion without `[<TailCall>]`, and unhandled `null` from C# APIs. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/fsharp-dotnet-functional/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **F#**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``dotnet-trace`, Ionide/VS debugger, and ILSpy decompilation of generated CLR classes.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `MSBuild `.fsproj` with explicit top-down `<Compile Include="..." />` ordering and `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (`inline` functions with Statically Resolved Type Parameters (`^T`), `Span<'T>`, and `[<Struct>]` DUs.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Make illegal states unrepresentable via single-case union wrappers (`type EmailAddress = private EmailAddress of string`) with smart constructors.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Expecto + FsCheck property-based testing.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Seamless consumption of C#/.NET libraries; guard incoming `null` references from C# with `Option.ofObj` or F# 9 nullable reference support.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
