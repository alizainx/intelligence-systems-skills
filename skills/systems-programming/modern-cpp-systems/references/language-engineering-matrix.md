# Deep Engineering Reference: Modern ISO C++ (C++20/C++23) RAII, Concepts & Low-Latency Systems (`modern-cpp-systems`)

- **Language / Representation**: **C++**
- **Taxonomic Classification**: `Systems Programming Language`
- **Technical Relationship**: Multi-paradigm zero-overhead systems language evolving from C with C++20/C++23 Concepts, RAII, and Coroutines.
- **Governing Standards & Versions**: ISO/IEC 14882:2020 (C++20), ISO/IEC 14882:2023 (C++23), C++ Core Guidelines (C++17 / C++20 / C++23)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **C++** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Enforce Rule of Zero/Five, `[[nodiscard]]`, `constexpr`/`consteval`, structured bindings, and value-category (`lvalue`/`prvalue`/`xvalue`) discipline. |
| 2 | **Type System & Inference** | Constrain templates with C++20 `concept` and `requires` clauses; eliminate SFINAE clutter and narrowing conversions (`{}` initialization). |
| 3 | **Memory Management** | Deterministic RAII (`std::unique_ptr`, custom deleters), `std::span<T>` non-owning views, and `std::pmr` arena allocators. |
| 4 | **Concurrency & Async Programming** | Use `std::jthread` with `std::stop_token`, `std::atomic_ref`, `std::latch`/`std::barrier`, and stackless C++20 coroutines (`co_await`). |
| 5 | **Standard Library & Ecosystem** | STL `<ranges>`, `<format>`, `<expected>` (C++23), Boost, Abseil, fmt. |
| 6 | **Build Systems & Package Management** | CMake (`target_compile_features(tgt PUBLIC cxx_std_20)`), Conan, vcpkg, Ninja. |
| 7 | **Compiler / Interpreter Behavior** | G++/Clang template instantiation diagnostics, copy elision (RVO/NRVO), and vtable/RTTI layout (`-fno-exceptions -fno-rtti` in embedded). |
| 8 | **Debugging** | GDB pretty-printers, `clang-tidy`, AddressSanitizer/ThreadSanitizer/UBSan, and `perf` flamegraphs. |
| 9 | **Security** | Eliminate raw owning pointers, guard `std::span::subspan` bounds, and prevent iterator/reference invalidation on container reallocation. |
| 10 | **Performance Optimization** | Small-buffer optimization (SBO), `constexpr` lookup tables, cache-friendly `std::vector` flat storage, and move-only zero-copy pipelines. |
| 11 | **Error Handling** | Enforce strong exception guarantee (`noexcept` move constructors) or deterministic value-based `Expected<T, E>` / `std::expected`. |
| 12 | **Testing Methodologies** | Compile-time `static_assert` concept/constexpr proofs + runtime sanitizer test suites. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (C++17 / C++20 / C++23); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `extern "C"` ABI boundaries catching all exceptions before crossing into C, and `std::bit_cast` for type-safe representation reinterpretation. |
| 18 | **Common Engineering Mistakes** | Dangling `std::string_view`/`std::span`, throwing destructors, missing `noexcept` on move constructors degrading `std::vector` resize to copy. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/modern-cpp-systems/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **C++**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GDB pretty-printers, `clang-tidy`, AddressSanitizer/ThreadSanitizer/UBSan, and `perf` flamegraphs.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `CMake (`target_compile_features(tgt PUBLIC cxx_std_20)`), Conan, vcpkg, Ninja.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Small-buffer optimization (SBO), `constexpr` lookup tables, cache-friendly `std::vector` flat storage, and move-only zero-copy pipelines.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Eliminate raw owning pointers, guard `std::span::subspan` bounds, and prevent iterator/reference invalidation on container reallocation.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Compile-time `static_assert` concept/constexpr proofs + runtime sanitizer test suites.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`extern "C"` ABI boundaries catching all exceptions before crossing into C, and `std::bit_cast` for type-safe representation reinterpretation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
