---
name: modern-cpp-systems
description: Design, refactor, debug, and verify modern ISO C++20/C++23 systems using strict RAII ownership, move semantics, Concepts, std::span bounds safety, constexpr evaluation, coroutines, and strong exception safety.
allowed-tools: execute_bash view_file write_to_file
---

# Modern ISO C++ (C++20/C++23) RAII, Concepts & Low-Latency Systems

Design, refactor, debug, and verify modern ISO C++20/C++23 systems using strict RAII ownership, move semantics, Concepts, std::span bounds safety, constexpr evaluation, coroutines, and strong exception safety.

## A. Identity

- **Skill Name**: `modern-cpp-systems`
- **Domain**: `systems-programming`
- **Language / Representation**: **C++** (`Systems Programming Language`)
- **Technical Relationship**: Multi-paradigm zero-overhead systems language evolving from C with C++20/C++23 Concepts, RAII, and Coroutines.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **C++**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 14882:2020 (C++20), ISO/IEC 14882:2023 (C++23), C++ Core Guidelines (C++17 / C++20 / C++23)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`CMake (`target_compile_features(tgt PUBLIC cxx_std_20)`), Conan, vcpkg, Ninja.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **C++** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **C++**.

### Technical Triggers

- Files, build manifests, or prompts targeting **C++** (`cpp20_concepts_raii.cpp`, `CMake (`target_compile_features(tgt PUBLIC cxx_std_20)`), Conan, vcpkg, Ninja.`).

### Prerequisites

- Target language version (C++17 / C++20 / C++23), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **C++** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (C++17 / C++20 / C++23), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Deterministic RAII (`std::unique_ptr`, custom deleters), `std::span<T>` non-owning views, and `std::pmr` arena allocators.), type soundness limits (Constrain templates with C++20 `concept` and `requires` clauses; eliminate SFINAE clutter and narrowing conversions (`{}` initialization).), and concurrency hazards (Use `std::jthread` with `std::stop_token`, `std::atomic_ref`, `std::latch`/`std::barrier`, and stackless C++20 coroutines (`co_await`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 14882:2020 (C++20), ISO/IEC 14882:2023 (C++23), C++ Core Guidelines.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Enforce Rule of Zero/Five, `[[nodiscard]]`, `constexpr`/`consteval`, structured bindings, and value-category (`lvalue`/`prvalue`/`xvalue`) discipline.
2. **Type System & Inference**: Constrain templates with C++20 `concept` and `requires` clauses; eliminate SFINAE clutter and narrowing conversions (`{}` initialization).
3. **Memory Management**: Deterministic RAII (`std::unique_ptr`, custom deleters), `std::span<T>` non-owning views, and `std::pmr` arena allocators.
4. **Concurrency & Async Programming**: Use `std::jthread` with `std::stop_token`, `std::atomic_ref`, `std::latch`/`std::barrier`, and stackless C++20 coroutines (`co_await`).
5. **Standard Library & Ecosystem**: STL `<ranges>`, `<format>`, `<expected>` (C++23), Boost, Abseil, fmt.
6. **Build Systems & Package Management**: CMake (`target_compile_features(tgt PUBLIC cxx_std_20)`), Conan, vcpkg, Ninja.
7. **Compiler / Interpreter Behavior**: G++/Clang template instantiation diagnostics, copy elision (RVO/NRVO), and vtable/RTTI layout (`-fno-exceptions -fno-rtti` in embedded).
8. **Debugging & Observability**: GDB pretty-printers, `clang-tidy`, AddressSanitizer/ThreadSanitizer/UBSan, and `perf` flamegraphs.
9. **Security Hardening**: Eliminate raw owning pointers, guard `std::span::subspan` bounds, and prevent iterator/reference invalidation on container reallocation.
10. **Performance Optimization**: Small-buffer optimization (SBO), `constexpr` lookup tables, cache-friendly `std::vector` flat storage, and move-only zero-copy pipelines.
11. **Error Handling Discipline**: Enforce strong exception guarantee (`noexcept` move constructors) or deterministic value-based `Expected<T, E>` / `std::expected`.
12. **Testing Methodologies**: Compile-time `static_assert` concept/constexpr proofs + runtime sanitizer test suites.
13. **Interoperability & Cross-Platform ABI**: `extern "C"` ABI boundaries catching all exceptions before crossing into C, and `std::bit_cast` for type-safe representation reinterpretation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/modern-cpp-systems/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (C++17 / C++20 / C++23), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in C++**: Dangling `std::string_view`/`std::span`, throwing destructors, missing `noexcept` on move constructors degrading `std::vector` resize to copy.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
