---
name: rust-ownership-and-nostd
description: Architect, implement, debug, and verify Rust systems software across ownership, borrow checking, lifetimes, unsafe SAFETY invariants, Cargo workspaces, procedural macros, Tokio/embassy async runtimes, #![no_std], and C FFI.
allowed-tools: execute_bash view_file write_to_file
---

# Rust (2021/2024) Ownership, Lifetimes, Unsafe Invariants, Async & no_std

Architect, implement, debug, and verify Rust systems software across ownership, borrow checking, lifetimes, unsafe SAFETY invariants, Cargo workspaces, procedural macros, Tokio/embassy async runtimes, #![no_std], and C FFI.

## A. Identity

- **Skill Name**: `rust-ownership-and-nostd`
- **Domain**: `systems-programming`
- **Language / Representation**: **Rust** (`Systems Programming Language`)
- **Technical Relationship**: Affine-typed memory-safe systems language supporting hosted (`std`) and bare-metal (`#![no_std]`) targets.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Rust**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: The Rust Reference (2021/2024 Editions), Rustonomicon, Unsafe Code Guidelines (Rust 1.75+ (2021 / 2024 Edition))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Cargo workspaces (`Cargo.toml`, `Cargo.lock`, `resolver = "2"`), `build.rs`, `clippy -D warnings`, `cargo miri test`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Rust** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Rust**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Rust** (`nostd_pinned_ring.rs`, `Cargo workspaces (`Cargo.toml`, `Cargo.lock`, `resolver = "2"`), `build.rs`, `clippy -D warnings`, `cargo miri test`.`).

### Prerequisites

- Target language version (Rust 1.75+ (2021 / 2024 Edition)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Rust** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Rust 1.75+ (2021 / 2024 Edition)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Compile-time borrow checker (`&T` aliasing XOR `&mut T` exclusivity), `Pin<&mut T>` for self-referential async futures, and `MaybeUninit<T>`.), type soundness limits (Algebraic enums, trait objects (`dyn Trait`) vs monomorphized generics (`impl Trait`), associated types, and `Send`/`Sync` auto-traits.), and concurrency hazards (Fearless concurrency via `Send`/`Sync`, lock-free `core::sync::atomic`, and structured async (`tokio` work-stealing or `#![no_std]` `embassy`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce The Rust Reference (2021/2024 Editions), Rustonomicon, Unsafe Code Guidelines.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Affine move semantics, exhaustive pattern matching, `?` carrier propagation, and explicit lifetime variance (`'a`, HRTB `for<'a>`).
2. **Type System & Inference**: Algebraic enums, trait objects (`dyn Trait`) vs monomorphized generics (`impl Trait`), associated types, and `Send`/`Sync` auto-traits.
3. **Memory Management**: Compile-time borrow checker (`&T` aliasing XOR `&mut T` exclusivity), `Pin<&mut T>` for self-referential async futures, and `MaybeUninit<T>`.
4. **Concurrency & Async Programming**: Fearless concurrency via `Send`/`Sync`, lock-free `core::sync::atomic`, and structured async (`tokio` work-stealing or `#![no_std]` `embassy`).
5. **Standard Library & Ecosystem**: `core`, `alloc`, `std`, `serde`, `thiserror`, `tracing`, `syn`/`quote` (procedural macros).
6. **Build Systems & Package Management**: Cargo workspaces (`Cargo.toml`, `Cargo.lock`, `resolver = "2"`), `build.rs`, `clippy -D warnings`, `cargo miri test`.
7. **Compiler / Interpreter Behavior**: `rustc` MIR borrowck (Polonius/NLL), LLVM backend optimization passes, and `#[inline]`/`#[cold]` codegen hints.
8. **Debugging & Observability**: `rust-gdb`/`rust-lldb`, `RUST_BACKTRACE=1`, `cargo miri` (Stacked/Tree Borrows UB detection), and `tokio-console`.
9. **Security Hardening**: Forbid `unsafe` via `#![deny(unsafe_op_in_unsafe_fn)]` unless accompanied by a formal `// SAFETY:` proof; audit `extern "C"` panic unwinding.
10. **Performance Optimization**: Zero-cost iterators, slice bounds-check elision, `SmallVec`/arena allocation, and cache-aligned `#[repr(C, align(64))]` structs.
11. **Error Handling Discipline**: Typed `Result<T, E>` with `#[must_use]`, zero `unwrap()`/`expect()` in library/kernel paths, and `panic = "abort"` in freestanding builds.
12. **Testing Methodologies**: Unit tests (`#[cfg(test)]`), doc-tests, integration suites (`tests/`), `proptest` property testing, and `cargo fuzz`.
13. **Interoperability & Cross-Platform ABI**: `#[repr(C)]` layout, `extern "C-unwind"` vs `extern "C"` with `catch_unwind`, and `bindgen`/`cbindgen` header generation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/rust-ownership-and-nostd/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Rust 1.75+ (2021 / 2024 Edition)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Rust**: Holding `std::sync::MutexGuard` across `.await` points, creating unaligned/aliasing references from raw pointers in `unsafe`, and blocking async executor threads.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
