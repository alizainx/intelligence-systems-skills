---
name: swift-arc-concurrency
description: Develop, audit, and verify Swift 5.10/6.0 software using value semantics, ARC weak/unowned cycle prevention, Actor isolation, Sendable data-race checking, ~Copyable move-only types, and C/C++ interoperability.
allowed-tools: execute_bash view_file write_to_file
---

# Swift (5.10 / Swift 6) Strict Concurrency, Actors, Sendable, ARC & Noncopyable Types

Develop, audit, and verify Swift 5.10/6.0 software using value semantics, ARC weak/unowned cycle prevention, Actor isolation, Sendable data-race checking, ~Copyable move-only types, and C/C++ interoperability.

## A. Identity

- **Skill Name**: `swift-arc-concurrency`
- **Domain**: `programming-languages`
- **Language / Representation**: **Swift** (`General-Purpose & Systems Programming Language`)
- **Technical Relationship**: LLVM-compiled language with deterministic Automatic Reference Counting (ARC), value-type copy-on-write structs, and Swift 6 compile-time data-race safety.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Swift**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: The Swift Programming Language (Swift 5.10 / Swift 6.0 Strict Concurrency) (Swift 5.10 / Swift 6.0)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``swift build -Xswiftc -warnings-as-errors -Xswiftc -strict-concurrency=complete`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Swift** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Swift**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Swift** (`ActorLedger.swift`, ``swift build -Xswiftc -warnings-as-errors -Xswiftc -strict-concurrency=complete`.`).

### Prerequisites

- Target language version (Swift 5.10 / Swift 6.0), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Swift** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Swift 5.10 / Swift 6.0), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Deterministic ARC (`strong`, `weak`, `unowned`); break closure retain cycles via `[weak self]` capture lists.), type soundness limits (Protocol-oriented generics (`some Protocol` opaque vs `any Protocol` existential), `Sendable` compile-time concurrency checking, and non-optional safety.), and concurrency hazards (`actor` isolation, `@MainActor`, structured `withThrowingTaskGroup`, and cooperative task cancellation (`try Task.checkCancellation()`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce The Swift Programming Language (Swift 5.10 / Swift 6.0 Strict Concurrency).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Value-type `struct`/`enum` with Copy-on-Write (CoW), `guard let` early exits, `defer`, and `~Copyable` (`borrowing`/`consuming`) ownership.
2. **Type System & Inference**: Protocol-oriented generics (`some Protocol` opaque vs `any Protocol` existential), `Sendable` compile-time concurrency checking, and non-optional safety.
3. **Memory Management**: Deterministic ARC (`strong`, `weak`, `unowned`); break closure retain cycles via `[weak self]` capture lists.
4. **Concurrency & Async Programming**: `actor` isolation, `@MainActor`, structured `withThrowingTaskGroup`, and cooperative task cancellation (`try Task.checkCancellation()`).
5. **Standard Library & Ecosystem**: Swift Package Manager (`Package.swift`), Foundation, SwiftNIO, Swift Testing (`@Test`), XCTest.
6. **Build Systems & Package Management**: `swift build -Xswiftc -warnings-as-errors -Xswiftc -strict-concurrency=complete`.
7. **Compiler / Interpreter Behavior**: SIL (Swift Intermediate Language) ARC optimizer, generic specialization, and existential box allocation (`any P` > 3 words spills to heap).
8. **Debugging & Observability**: LLDB (`po`, `v`, `swift-healthcheck`), Thread Sanitizer (`-sanitize=thread`), Address Sanitizer, and Instruments Allocation leaks.
9. **Security Hardening**: Avoid force-unwrapping (`!`) and `UnsafePointer` without `withUnsafeBytes` scoped lifetimes.
10. **Performance Optimization**: Prefer `some Protocol` over `any Protocol` to enable static dispatch and inline stack allocation; use `ContiguousArray<T>`.
11. **Error Handling Discipline**: Typed throws (`throws(ParseError)` in Swift 6) and `Result<Success, Failure>`.
12. **Testing Methodologies**: Swift Testing (`@Test`, `#expect`) and XCTest with TSan enabled.
13. **Interoperability & Cross-Platform ABI**: Direct C (`clang` module maps) and C++ interoperability (`-cxx-interoperability-mode=default`), plus `@_cdecl` C exports.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/swift-arc-concurrency/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Swift 5.10 / Swift 6.0), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Swift**: Actor reentrancy assumptions across `await` suspension points, retain cycles in escaping closures, and existential heap boxing in hot loops.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
