# Deep Engineering Reference: JavaScript (ES2023+) V8 Hidden Classes, Event Loop, Async Streams & Prototype Security (`javascript-v8-runtime`)

- **Language / Representation**: **JavaScript**
- **Taxonomic Classification**: `General-Purpose & Runtime Scripting Language`
- **Technical Relationship**: ECMA-262 dynamic language executed by JIT engines (V8, JavaScriptCore, SpiderMonkey) in Node.js, Deno, Bun, and browsers.
- **Governing Standards & Versions**: ECMA-262 (ECMAScript 2023 / 2024), WHATWG Streams & AbortController (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **JavaScript** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Strict mode (`'use strict'` / ES Modules `.mjs`), lexical `const`/`let`, private class fields (`#field`), `Object.hasOwn`, and `null`/`undefined` coalescing (`??`). |
| 2 | **Type System & Inference** | Dynamic IEEE 754 `Number` vs arbitrary-precision `BigInt`; validate runtime schemas at every I/O boundary and document JSDoc `@ts-check` annotations. |
| 3 | **Memory Management** | V8 Orinoco generational GC, `WeakMap`/`WeakRef`/`FinalizationRegistry`, and explicit listener/timer cleanup (`AbortSignal`) to prevent closure leaks. |
| 4 | **Concurrency & Async Programming** | Single-threaded call stack + microtask queue (`Promise.then`/`queueMicrotask`) + libuv macrotask phases; use `worker_threads` with `SharedArrayBuffer`/`Atomics` for CPU work. |
| 5 | **Standard Library & Ecosystem** | Node.js built-ins (`node:test`, `node:stream/promises`, `node:crypto`), ESLint, Prettier. |
| 6 | **Build Systems & Package Management** | `package.json` (`"type": "module"`, `"engines"`), `npm ci --ignore-scripts`, lockfile integrity (`package-lock.json`). |
| 7 | **Compiler / Interpreter Behavior** | V8 Ignition bytecode -> Sparkplug -> Maglev -> TurboFan optimizing JIT; maintain monomorphic object shapes (hidden classes/Maps) by initializing all fields in constructors. |
| 8 | **Debugging** | `node --inspect`, Chrome DevTools Heap Snapshots, `--trace-gc`, and `--prof` CPU ticks. |
| 9 | **Security** | Block prototype pollution (`__proto__`, `constructor.prototype`) using `Object.create(null)` or `Map`, use `crypto.timingSafeEqual`, and avoid `eval`/`new Function`. |
| 10 | **Performance Optimization** | Keep arrays packed (`PACKED_SMI_ELEMENTS` / `Float64Array`), avoid `delete obj.prop` (transitions to slow dictionary mode), and stream backpressure via `pipeline()`. |
| 11 | **Error Handling** | Wrap errors with `{ cause: err }`, attach `unhandledRejection` fail-fast handlers, and pass `AbortSignal` to all async I/O. |
| 12 | **Testing Methodologies** | Native `node --test` runner with `assert/strict` executed directly in V8. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (ES2022 / ES2023 / ES2024 (Node.js 18 / 20 / 22 LTS)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Node-API (`N-API`) ABI-stable native C/C++/Rust addons and `WebAssembly` instantiation. |
| 18 | **Common Engineering Mistakes** | Floating unawaited Promises, IEEE 754 `0.1 + 0.2 !== 0.3` in financial math, and ReDoS catastrophic backtracking. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/javascript-v8-runtime/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **JavaScript**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``node --inspect`, Chrome DevTools Heap Snapshots, `--trace-gc`, and `--prof` CPU ticks.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``package.json` (`"type": "module"`, `"engines"`), `npm ci --ignore-scripts`, lockfile integrity (`package-lock.json`).`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Keep arrays packed (`PACKED_SMI_ELEMENTS` / `Float64Array`), avoid `delete obj.prop` (transitions to slow dictionary mode), and stream backpressure via `pipeline()`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Block prototype pollution (`__proto__`, `constructor.prototype`) using `Object.create(null)` or `Map`, use `crypto.timingSafeEqual`, and avoid `eval`/`new Function`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Native `node --test` runner with `assert/strict` executed directly in V8.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Node-API (`N-API`) ABI-stable native C/C++/Rust addons and `WebAssembly` instantiation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
