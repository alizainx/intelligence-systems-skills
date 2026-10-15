---
name: dart-isolates-async
description: Engineer, debug, and verify Dart 3 applications and services using sound null safety, records, sealed class pattern matching, Future/Stream event-loop concurrency, Isolate.run parallel offloading, and dart:ffi.
allowed-tools: execute_bash view_file write_to_file
---

# Dart 3 Sound Null Safety, Sealed Exhaustiveness, Event Loop & Isolates

Engineer, debug, and verify Dart 3 applications and services using sound null safety, records, sealed class pattern matching, Future/Stream event-loop concurrency, Isolate.run parallel offloading, and dart:ffi.

## A. Identity

- **Skill Name**: `dart-isolates-async`
- **Domain**: `programming-languages`
- **Language / Representation**: **Dart** (`General-Purpose Programming Language`)
- **Technical Relationship**: Sound null-safe, ahead-of-time (AOT) and JIT compiled language powering Flutter and server runtimes with shared-nothing Actor `Isolate` concurrency.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Dart**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Dart Programming Language Specification (Dart 3.x) (Dart 3.2 / 3.4+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``dart analyze --fatal-infos --fatal-warnings`, `dart compile exe` (self-contained AOT binary), `dart test`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Dart** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Dart**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Dart** (`sealed_rpc_result.dart`, ``dart analyze --fatal-infos --fatal-warnings`, `dart compile exe` (self-contained AOT binary), `dart test`.`).

### Prerequisites

- Target language version (Dart 3.2 / 3.4+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Dart** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Dart 3.2 / 3.4+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Generational scavenged heap per Isolate; close `StreamController`/`ReceivePort` and `NativeFinalizer` for FFI resources.), type soundness limits (Reified generics at runtime, sound non-nullability guaranteed by compiler and AOT runtime, and pattern destructuring.), and concurrency hazards (Single-threaded microtask + event queue per Isolate; offload CPU-heavy work via `Isolate.run(() => ...)` with zero shared mutable state.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Dart Programming Language Specification (Dart 3.x).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Sound null safety (`T` vs `T?`), records `(int, {String label})`, `sealed class` exhaustive `switch` expressions, and class modifiers (`final`, `interface`, `base`).
2. **Type System & Inference**: Reified generics at runtime, sound non-nullability guaranteed by compiler and AOT runtime, and pattern destructuring.
3. **Memory Management**: Generational scavenged heap per Isolate; close `StreamController`/`ReceivePort` and `NativeFinalizer` for FFI resources.
4. **Concurrency & Async Programming**: Single-threaded microtask + event queue per Isolate; offload CPU-heavy work via `Isolate.run(() => ...)` with zero shared mutable state.
5. **Standard Library & Ecosystem**: `pub` (`pubspec.yaml`), `collection`, `async`, `ffi`, `test`, `lints`.
6. **Build Systems & Package Management**: `dart analyze --fatal-infos --fatal-warnings`, `dart compile exe` (self-contained AOT binary), `dart test`.
7. **Compiler / Interpreter Behavior**: Development incremental kernel JIT (`dart run`) vs production treen-shaken machine-code AOT (`dart compile exe`).
8. **Debugging & Observability**: Dart DevTools (CPU profiler, memory heap diff, async causal stack traces).
9. **Security Hardening**: Avoid `dynamic` type escapes (`strict-casts: true`, `strict-raw-types: true` in `analysis_options.yaml`).
10. **Performance Optimization**: Use `Uint8List`/`Float64List` (`dart:typed_data`) for unboxed contiguous buffers and `Isolate.exit` for zero-copy message passing.
11. **Error Handling Discipline**: Sealed result ADTs or typed exceptions; never leave unawaited `Future` instances (`unawaited_futures` lint).
12. **Testing Methodologies**: `package:test` with fake async clock (`fake_async`) and `Isolate` stress tests.
13. **Interoperability & Cross-Platform ABI**: `dart:ffi` (`NativeCallable`, `Struct`, `Pointer<T>`) and `js_interop` for WebAssembly/JS targets.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/dart-isolates-async/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Dart 3.2 / 3.4+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Dart**: Forgetting `await` on asynchronous calls, using `late` variables that throw `LateInitializationError`, and blocking the main Isolate event loop.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
