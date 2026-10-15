# Deep Engineering Reference: Swift (5.10 / Swift 6) Strict Concurrency, Actors, Sendable, ARC & Noncopyable Types (`swift-arc-concurrency`)

- **Language / Representation**: **Swift**
- **Taxonomic Classification**: `General-Purpose & Systems Programming Language`
- **Technical Relationship**: LLVM-compiled language with deterministic Automatic Reference Counting (ARC), value-type copy-on-write structs, and Swift 6 compile-time data-race safety.
- **Governing Standards & Versions**: The Swift Programming Language (Swift 5.10 / Swift 6.0 Strict Concurrency) (Swift 5.10 / Swift 6.0)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Swift** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Value-type `struct`/`enum` with Copy-on-Write (CoW), `guard let` early exits, `defer`, and `~Copyable` (`borrowing`/`consuming`) ownership. |
| 2 | **Type System & Inference** | Protocol-oriented generics (`some Protocol` opaque vs `any Protocol` existential), `Sendable` compile-time concurrency checking, and non-optional safety. |
| 3 | **Memory Management** | Deterministic ARC (`strong`, `weak`, `unowned`); break closure retain cycles via `[weak self]` capture lists. |
| 4 | **Concurrency & Async Programming** | `actor` isolation, `@MainActor`, structured `withThrowingTaskGroup`, and cooperative task cancellation (`try Task.checkCancellation()`). |
| 5 | **Standard Library & Ecosystem** | Swift Package Manager (`Package.swift`), Foundation, SwiftNIO, Swift Testing (`@Test`), XCTest. |
| 6 | **Build Systems & Package Management** | `swift build -Xswiftc -warnings-as-errors -Xswiftc -strict-concurrency=complete`. |
| 7 | **Compiler / Interpreter Behavior** | SIL (Swift Intermediate Language) ARC optimizer, generic specialization, and existential box allocation (`any P` > 3 words spills to heap). |
| 8 | **Debugging** | LLDB (`po`, `v`, `swift-healthcheck`), Thread Sanitizer (`-sanitize=thread`), Address Sanitizer, and Instruments Allocation leaks. |
| 9 | **Security** | Avoid force-unwrapping (`!`) and `UnsafePointer` without `withUnsafeBytes` scoped lifetimes. |
| 10 | **Performance Optimization** | Prefer `some Protocol` over `any Protocol` to enable static dispatch and inline stack allocation; use `ContiguousArray<T>`. |
| 11 | **Error Handling** | Typed throws (`throws(ParseError)` in Swift 6) and `Result<Success, Failure>`. |
| 12 | **Testing Methodologies** | Swift Testing (`@Test`, `#expect`) and XCTest with TSan enabled. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Swift 5.10 / Swift 6.0); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Direct C (`clang` module maps) and C++ interoperability (`-cxx-interoperability-mode=default`), plus `@_cdecl` C exports. |
| 18 | **Common Engineering Mistakes** | Actor reentrancy assumptions across `await` suspension points, retain cycles in escaping closures, and existential heap boxing in hot loops. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/swift-arc-concurrency/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Swift**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `LLDB (`po`, `v`, `swift-healthcheck`), Thread Sanitizer (`-sanitize=thread`), Address Sanitizer, and Instruments Allocation leaks.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``swift build -Xswiftc -warnings-as-errors -Xswiftc -strict-concurrency=complete`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Prefer `some Protocol` over `any Protocol` to enable static dispatch and inline stack allocation; use `ContiguousArray<T>`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Avoid force-unwrapping (`!`) and `UnsafePointer` without `withUnsafeBytes` scoped lifetimes.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Swift Testing (`@Test`, `#expect`) and XCTest with TSan enabled.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Direct C (`clang` module maps) and C++ interoperability (`-cxx-interoperability-mode=default`), plus `@_cdecl` C exports.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
