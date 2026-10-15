# Deep Engineering Reference: Rust (2021/2024) Ownership, Lifetimes, Unsafe Invariants, Async & no_std (`rust-ownership-and-nostd`)

- **Language / Representation**: **Rust**
- **Taxonomic Classification**: `Systems Programming Language`
- **Technical Relationship**: Affine-typed memory-safe systems language supporting hosted (`std`) and bare-metal (`#![no_std]`) targets.
- **Governing Standards & Versions**: The Rust Reference (2021/2024 Editions), Rustonomicon, Unsafe Code Guidelines (Rust 1.75+ (2021 / 2024 Edition))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Rust** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Affine move semantics, exhaustive pattern matching, `?` carrier propagation, and explicit lifetime variance (`'a`, HRTB `for<'a>`). |
| 2 | **Type System & Inference** | Algebraic enums, trait objects (`dyn Trait`) vs monomorphized generics (`impl Trait`), associated types, and `Send`/`Sync` auto-traits. |
| 3 | **Memory Management** | Compile-time borrow checker (`&T` aliasing XOR `&mut T` exclusivity), `Pin<&mut T>` for self-referential async futures, and `MaybeUninit<T>`. |
| 4 | **Concurrency & Async Programming** | Fearless concurrency via `Send`/`Sync`, lock-free `core::sync::atomic`, and structured async (`tokio` work-stealing or `#![no_std]` `embassy`). |
| 5 | **Standard Library & Ecosystem** | `core`, `alloc`, `std`, `serde`, `thiserror`, `tracing`, `syn`/`quote` (procedural macros). |
| 6 | **Build Systems & Package Management** | Cargo workspaces (`Cargo.toml`, `Cargo.lock`, `resolver = "2"`), `build.rs`, `clippy -D warnings`, `cargo miri test`. |
| 7 | **Compiler / Interpreter Behavior** | `rustc` MIR borrowck (Polonius/NLL), LLVM backend optimization passes, and `#[inline]`/`#[cold]` codegen hints. |
| 8 | **Debugging** | `rust-gdb`/`rust-lldb`, `RUST_BACKTRACE=1`, `cargo miri` (Stacked/Tree Borrows UB detection), and `tokio-console`. |
| 9 | **Security** | Forbid `unsafe` via `#![deny(unsafe_op_in_unsafe_fn)]` unless accompanied by a formal `// SAFETY:` proof; audit `extern "C"` panic unwinding. |
| 10 | **Performance Optimization** | Zero-cost iterators, slice bounds-check elision, `SmallVec`/arena allocation, and cache-aligned `#[repr(C, align(64))]` structs. |
| 11 | **Error Handling** | Typed `Result<T, E>` with `#[must_use]`, zero `unwrap()`/`expect()` in library/kernel paths, and `panic = "abort"` in freestanding builds. |
| 12 | **Testing Methodologies** | Unit tests (`#[cfg(test)]`), doc-tests, integration suites (`tests/`), `proptest` property testing, and `cargo fuzz`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Rust 1.75+ (2021 / 2024 Edition)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `#[repr(C)]` layout, `extern "C-unwind"` vs `extern "C"` with `catch_unwind`, and `bindgen`/`cbindgen` header generation. |
| 18 | **Common Engineering Mistakes** | Holding `std::sync::MutexGuard` across `.await` points, creating unaligned/aliasing references from raw pointers in `unsafe`, and blocking async executor threads. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/rust-ownership-and-nostd/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Rust**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``rust-gdb`/`rust-lldb`, `RUST_BACKTRACE=1`, `cargo miri` (Stacked/Tree Borrows UB detection), and `tokio-console`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Cargo workspaces (`Cargo.toml`, `Cargo.lock`, `resolver = "2"`), `build.rs`, `clippy -D warnings`, `cargo miri test`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Zero-cost iterators, slice bounds-check elision, `SmallVec`/arena allocation, and cache-aligned `#[repr(C, align(64))]` structs.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Forbid `unsafe` via `#![deny(unsafe_op_in_unsafe_fn)]` unless accompanied by a formal `// SAFETY:` proof; audit `extern "C"` panic unwinding.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Unit tests (`#[cfg(test)]`), doc-tests, integration suites (`tests/`), `proptest` property testing, and `cargo fuzz`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`#[repr(C)]` layout, `extern "C-unwind"` vs `extern "C"` with `catch_unwind`, and `bindgen`/`cbindgen` header generation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
