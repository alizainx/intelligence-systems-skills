# Deep Engineering Reference: Dart 3 Sound Null Safety, Sealed Exhaustiveness, Event Loop & Isolates (`dart-isolates-async`)

- **Language / Representation**: **Dart**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: Sound null-safe, ahead-of-time (AOT) and JIT compiled language powering Flutter and server runtimes with shared-nothing Actor `Isolate` concurrency.
- **Governing Standards & Versions**: Dart Programming Language Specification (Dart 3.x) (Dart 3.2 / 3.4+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Dart** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Sound null safety (`T` vs `T?`), records `(int, {String label})`, `sealed class` exhaustive `switch` expressions, and class modifiers (`final`, `interface`, `base`). |
| 2 | **Type System & Inference** | Reified generics at runtime, sound non-nullability guaranteed by compiler and AOT runtime, and pattern destructuring. |
| 3 | **Memory Management** | Generational scavenged heap per Isolate; close `StreamController`/`ReceivePort` and `NativeFinalizer` for FFI resources. |
| 4 | **Concurrency & Async Programming** | Single-threaded microtask + event queue per Isolate; offload CPU-heavy work via `Isolate.run(() => ...)` with zero shared mutable state. |
| 5 | **Standard Library & Ecosystem** | `pub` (`pubspec.yaml`), `collection`, `async`, `ffi`, `test`, `lints`. |
| 6 | **Build Systems & Package Management** | `dart analyze --fatal-infos --fatal-warnings`, `dart compile exe` (self-contained AOT binary), `dart test`. |
| 7 | **Compiler / Interpreter Behavior** | Development incremental kernel JIT (`dart run`) vs production treen-shaken machine-code AOT (`dart compile exe`). |
| 8 | **Debugging** | Dart DevTools (CPU profiler, memory heap diff, async causal stack traces). |
| 9 | **Security** | Avoid `dynamic` type escapes (`strict-casts: true`, `strict-raw-types: true` in `analysis_options.yaml`). |
| 10 | **Performance Optimization** | Use `Uint8List`/`Float64List` (`dart:typed_data`) for unboxed contiguous buffers and `Isolate.exit` for zero-copy message passing. |
| 11 | **Error Handling** | Sealed result ADTs or typed exceptions; never leave unawaited `Future` instances (`unawaited_futures` lint). |
| 12 | **Testing Methodologies** | `package:test` with fake async clock (`fake_async`) and `Isolate` stress tests. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Dart 3.2 / 3.4+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `dart:ffi` (`NativeCallable`, `Struct`, `Pointer<T>`) and `js_interop` for WebAssembly/JS targets. |
| 18 | **Common Engineering Mistakes** | Forgetting `await` on asynchronous calls, using `late` variables that throw `LateInitializationError`, and blocking the main Isolate event loop. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/dart-isolates-async/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Dart**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Dart DevTools (CPU profiler, memory heap diff, async causal stack traces).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``dart analyze --fatal-infos --fatal-warnings`, `dart compile exe` (self-contained AOT binary), `dart test`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `Uint8List`/`Float64List` (`dart:typed_data`) for unboxed contiguous buffers and `Isolate.exit` for zero-copy message passing.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Avoid `dynamic` type escapes (`strict-casts: true`, `strict-raw-types: true` in `analysis_options.yaml`).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`package:test` with fake async clock (`fake_async`) and `Isolate` stress tests.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`dart:ffi` (`NativeCallable`, `Struct`, `Pointer<T>`) and `js_interop` for WebAssembly/JS targets.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
