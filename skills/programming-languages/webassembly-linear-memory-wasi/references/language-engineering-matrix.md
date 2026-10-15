# Deep Engineering Reference: WebAssembly (Wasm Core 2.0 & WASI) Linear Memory Safety, Stack Validation & Host Instantiation (`webassembly-linear-memory-wasi`)

- **Language / Representation**: **WebAssembly**
- **Taxonomic Classification**: `Low-Level Portable Binary & Text Intermediate Representation`
- **Technical Relationship**: W3C stack-based portable binary instruction format (`.wasm`) and text format (`.wat`) targeted by C/C++/Rust/Zig/Go compilers and executed by V8, Wasmtime, and Wasmer.
- **Governing Standards & Versions**: W3C WebAssembly Core Specification 2.0, WASI (Preview 1 / Preview 2 Component Model) (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **WebAssembly** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Structured control flow (`block`, `loop`, `if`, `br`, `br_if`, `br_table` — irreducible arbitrary `goto` is forbidden by bytecode validation!), and typed value stack (`i32`, `i64`, `f32`, `f64`, `v128`, `funcref`, `externref`). |
| 2 | **Type System & Inference** | Single-pass linear-time stack polymorphism and function-signature validation before instantiation; `call_indirect` validates table element signature at runtime. |
| 3 | **Memory Management** | Sandboxed contiguous byte array (`WebAssembly.Memory` in 64 KiB page units) completely disjoint from the execution call stack and code space (preventing ROP return-address overwrites!). |
| 4 | **Concurrency & Async Programming** | Shared linear memory (`new WebAssembly.Memory({ initial, maximum, shared: true })`) with atomic `i32.atomic.rmw.cmpxchg` and `memory.atomic.wait32`/`notify`. |
| 5 | **Standard Library & Ecosystem** | WABT (`wat2wasm`, `wasm2wat`, `wasm-objdump`, `wasm-validate`), Binaryen (`wasm-opt`), Wasmtime, Node.js V8. |
| 6 | **Build Systems & Package Management** | `clang --target=wasm32-wasi`, `cargo build --target wasm32-wasip1`, `wasm-opt -O3`. |
| 7 | **Compiler / Interpreter Behavior** | Streaming baseline compilation (Liftoff in V8, Winch in Wasmtime) followed by optimizing tier (TurboFan / Cranelift). |
| 8 | **Debugging** | DWARF in custom sections, `wasm-objdump -d`, Chrome DevTools / `lldb` Wasmtime support. |
| 9 | **Security** | Enforce explicit `maximum` page limits on `memory` imports/exports and capability-based WASI preopened directory descriptors; audit linear-memory heap overflow between guest allocations. |
| 10 | **Performance Optimization** | 128-bit Fixed-Width SIMD (`v128`), `memory.copy`/`memory.fill` bulk memory ops, and minimizing JS <-> Wasm boundary crossings per frame. |
| 11 | **Error Handling** | Hardware/runtime `RuntimeError: unreachable` or `memory access out of bounds` traps cleanly isolated inside the host. |
| 12 | **Testing Methodologies** | Instantiate binary `.wasm` modules directly in Node.js V8 and verify exported functions and boundary traps. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Typed numeric imports/exports, shared `Uint8Array(memory.buffer)` views, and WIT (Wasm Interface Types) Component Model. |
| 18 | **Common Engineering Mistakes** | Holding a cached `new Uint8Array(memory.buffer)` view in JS after Wasm calls `memory.grow` (detaches the old `ArrayBuffer`!), and passing unvalidated guest pointers. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/webassembly-linear-memory-wasi/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **WebAssembly**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `DWARF in custom sections, `wasm-objdump -d`, Chrome DevTools / `lldb` Wasmtime support.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``clang --target=wasm32-wasi`, `cargo build --target wasm32-wasip1`, `wasm-opt -O3`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (128-bit Fixed-Width SIMD (`v128`), `memory.copy`/`memory.fill` bulk memory ops, and minimizing JS <-> Wasm boundary crossings per frame.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Enforce explicit `maximum` page limits on `memory` imports/exports and capability-based WASI preopened directory descriptors; audit linear-memory heap overflow between guest allocations.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Instantiate binary `.wasm` modules directly in Node.js V8 and verify exported functions and boundary traps.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Typed numeric imports/exports, shared `Uint8Array(memory.buffer)` views, and WIT (Wasm Interface Types) Component Model.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
