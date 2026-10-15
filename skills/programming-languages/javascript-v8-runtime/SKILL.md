---
name: javascript-v8-runtime
description: Write, audit, profile, and verify production JavaScript (ES2023+ / Node.js v18/v20+) systems with V8 hidden-class stability, microtask/event-loop scheduling, AbortController cancellation, prototype-pollution defense, and native execution tests.
allowed-tools: execute_bash view_file write_to_file
---

# JavaScript (ES2023+) V8 Hidden Classes, Event Loop, Async Streams & Prototype Security

Write, audit, profile, and verify production JavaScript (ES2023+ / Node.js v18/v20+) systems with V8 hidden-class stability, microtask/event-loop scheduling, AbortController cancellation, prototype-pollution defense, and native execution tests.

## A. Identity

- **Skill Name**: `javascript-v8-runtime`
- **Domain**: `programming-languages`
- **Language / Representation**: **JavaScript** (`General-Purpose & Runtime Scripting Language`)
- **Technical Relationship**: ECMA-262 dynamic language executed by JIT engines (V8, JavaScriptCore, SpiderMonkey) in Node.js, Deno, Bun, and browsers.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **JavaScript**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ECMA-262 (ECMAScript 2023 / 2024), WHATWG Streams & AbortController (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``package.json` (`"type": "module"`, `"engines"`), `npm ci --ignore-scripts`, lockfile integrity (`package-lock.json`).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **JavaScript** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **JavaScript**.

### Technical Triggers

- Files, build manifests, or prompts targeting **JavaScript** (`safe_json_merge.mjs`, ``package.json` (`"type": "module"`, `"engines"`), `npm ci --ignore-scripts`, lockfile integrity (`package-lock.json`).`).

### Prerequisites

- Target language version (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **JavaScript** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (V8 Orinoco generational GC, `WeakMap`/`WeakRef`/`FinalizationRegistry`, and explicit listener/timer cleanup (`AbortSignal`) to prevent closure leaks.), type soundness limits (Dynamic IEEE 754 `Number` vs arbitrary-precision `BigInt`; validate runtime schemas at every I/O boundary and document JSDoc `@ts-check` annotations.), and concurrency hazards (Single-threaded call stack + microtask queue (`Promise.then`/`queueMicrotask`) + libuv macrotask phases; use `worker_threads` with `SharedArrayBuffer`/`Atomics` for CPU work.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ECMA-262 (ECMAScript 2023 / 2024), WHATWG Streams & AbortController.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Strict mode (`'use strict'` / ES Modules `.mjs`), lexical `const`/`let`, private class fields (`#field`), `Object.hasOwn`, and `null`/`undefined` coalescing (`??`).
2. **Type System & Inference**: Dynamic IEEE 754 `Number` vs arbitrary-precision `BigInt`; validate runtime schemas at every I/O boundary and document JSDoc `@ts-check` annotations.
3. **Memory Management**: V8 Orinoco generational GC, `WeakMap`/`WeakRef`/`FinalizationRegistry`, and explicit listener/timer cleanup (`AbortSignal`) to prevent closure leaks.
4. **Concurrency & Async Programming**: Single-threaded call stack + microtask queue (`Promise.then`/`queueMicrotask`) + libuv macrotask phases; use `worker_threads` with `SharedArrayBuffer`/`Atomics` for CPU work.
5. **Standard Library & Ecosystem**: Node.js built-ins (`node:test`, `node:stream/promises`, `node:crypto`), ESLint, Prettier.
6. **Build Systems & Package Management**: `package.json` (`"type": "module"`, `"engines"`), `npm ci --ignore-scripts`, lockfile integrity (`package-lock.json`).
7. **Compiler / Interpreter Behavior**: V8 Ignition bytecode -> Sparkplug -> Maglev -> TurboFan optimizing JIT; maintain monomorphic object shapes (hidden classes/Maps) by initializing all fields in constructors.
8. **Debugging & Observability**: `node --inspect`, Chrome DevTools Heap Snapshots, `--trace-gc`, and `--prof` CPU ticks.
9. **Security Hardening**: Block prototype pollution (`__proto__`, `constructor.prototype`) using `Object.create(null)` or `Map`, use `crypto.timingSafeEqual`, and avoid `eval`/`new Function`.
10. **Performance Optimization**: Keep arrays packed (`PACKED_SMI_ELEMENTS` / `Float64Array`), avoid `delete obj.prop` (transitions to slow dictionary mode), and stream backpressure via `pipeline()`.
11. **Error Handling Discipline**: Wrap errors with `{ cause: err }`, attach `unhandledRejection` fail-fast handlers, and pass `AbortSignal` to all async I/O.
12. **Testing Methodologies**: Native `node --test` runner with `assert/strict` executed directly in V8.
13. **Interoperability & Cross-Platform ABI**: Node-API (`N-API`) ABI-stable native C/C++/Rust addons and `WebAssembly` instantiation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/javascript-v8-runtime/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in JavaScript**: Floating unawaited Promises, IEEE 754 `0.1 + 0.2 !== 0.3` in financial math, and ReDoS catastrophic backtracking.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
