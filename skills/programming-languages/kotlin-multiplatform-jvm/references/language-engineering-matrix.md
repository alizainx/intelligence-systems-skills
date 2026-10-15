# Deep Engineering Reference: Kotlin (K2 / 2.0+) Null Safety, Structured Coroutines, Flows & Multiplatform (`kotlin-multiplatform-jvm`)

- **Language / Representation**: **Kotlin**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: Statically typed language targeting JVM, Android, Kotlin/Native (LLVM), and JS/Wasm with built-in null safety and structured coroutines.
- **Governing Standards & Versions**: Kotlin Language Specification (Kotlin 1.9 / 2.0 K2 Compiler) (Kotlin 1.9 / 2.0+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Kotlin** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Null-safe types (`T` vs `T?`), smart casts, `sealed interface`/`data class`, `@JvmInline value class`, and extension functions. |
| 2 | **Type System & Inference** | Declaration-site variance (`in T`, `out T`), reified type parameters on `inline fun <reified T>`, and non-nullable platform-type boundary guards. |
| 3 | **Memory Management** | Escape analysis on JVM, `@JvmInline value class` avoiding heap boxing, and Kotlin/Native new memory manager. |
| 4 | **Concurrency & Async Programming** | Structured concurrency via `coroutineScope` / `supervisorScope`, `Dispatcher` isolation, `Mutex` (non-blocking), and cold `Flow` vs hot `StateFlow`. |
| 5 | **Standard Library & Ecosystem** | `kotlinx.coroutines`, `kotlinx.serialization`, `ktor`, `detekt`, `ktlint`, MockK. |
| 6 | **Build Systems & Package Management** | Gradle Kotlin DSL (`build.gradle.kts`), KMP source sets (`commonMain`, `jvmMain`, `nativeMain`), `allWarningsAsErrors = true`. |
| 7 | **Compiler / Interpreter Behavior** | K2 frontend FIR pipeline, `suspend` CPS state-machine continuation lowering, and `inline` lambda inlining (zero `FunctionN` allocation). |
| 8 | **Debugging** | IntelliJ/JDWP coroutine dump (`DebugProbes`), stacktrace recovery (`kotlinx-coroutines-debug`). |
| 9 | **Security** | Never apply the not-null assertion operator `!!` on external or Java platform values (`T!`); validate at the boundary. |
| 10 | **Performance Optimization** | Use `Sequence` (`asSequence()`) or `inline` higher-order functions to eliminate intermediate list allocations in collection chains. |
| 11 | **Error Handling** | Rethrow `CancellationException` in `runCatching` / `try-catch` inside `suspend` functions so structured cancellation is never broken! |
| 12 | **Testing Methodologies** | `kotlinx-coroutines-test` (`runTest` virtual time scheduler) and Turbine for `Flow` assertion testing. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Kotlin 1.9 / 2.0+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `@JvmStatic`, `@JvmOverloads`, `@Throws` for idiomatic Java interop, and CInterop for Kotlin/Native. |
| 18 | **Common Engineering Mistakes** | Swallowing `CancellationException` inside `runCatching {}`, launching orphaned coroutines on `GlobalScope`, and capturing mutable state across dispatchers. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/kotlin-multiplatform-jvm/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Kotlin**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `IntelliJ/JDWP coroutine dump (`DebugProbes`), stacktrace recovery (`kotlinx-coroutines-debug`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Gradle Kotlin DSL (`build.gradle.kts`), KMP source sets (`commonMain`, `jvmMain`, `nativeMain`), `allWarningsAsErrors = true`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `Sequence` (`asSequence()`) or `inline` higher-order functions to eliminate intermediate list allocations in collection chains.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Never apply the not-null assertion operator `!!` on external or Java platform values (`T!`); validate at the boundary.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`kotlinx-coroutines-test` (`runTest` virtual time scheduler) and Turbine for `Flow` assertion testing.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`@JvmStatic`, `@JvmOverloads`, `@Throws` for idiomatic Java interop, and CInterop for Kotlin/Native.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
