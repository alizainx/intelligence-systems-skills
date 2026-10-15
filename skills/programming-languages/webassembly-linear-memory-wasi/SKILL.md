---
name: webassembly-linear-memory-wasi
description: Construct, inspect, optimize, and verify WebAssembly (.wasm/.wat) modules, linear memory bounds, indirect call tables (call_indirect type checking), WASI capability sandboxing, and native V8 WebAssembly execution.
allowed-tools: execute_bash view_file write_to_file
---

# WebAssembly (Wasm Core 2.0 & WASI) Linear Memory Safety, Stack Validation & Host Instantiation

Construct, inspect, optimize, and verify WebAssembly (.wasm/.wat) modules, linear memory bounds, indirect call tables (call_indirect type checking), WASI capability sandboxing, and native V8 WebAssembly execution.

## A. Identity

- **Skill Name**: `webassembly-linear-memory-wasi`
- **Domain**: `programming-languages`
- **Language / Representation**: **WebAssembly** (`Low-Level Portable Binary & Text Intermediate Representation`)
- **Technical Relationship**: W3C stack-based portable binary instruction format (`.wasm`) and text format (`.wat`) targeted by C/C++/Rust/Zig/Go compilers and executed by V8, Wasmtime, and Wasmer.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **WebAssembly**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: W3C WebAssembly Core Specification 2.0, WASI (Preview 1 / Preview 2 Component Model) (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``clang --target=wasm32-wasi`, `cargo build --target wasm32-wasip1`, `wasm-opt -O3`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **WebAssembly** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **WebAssembly**.

### Technical Triggers

- Files, build manifests, or prompts targeting **WebAssembly** (`wasm_euclid_gcd.mjs`, ``clang --target=wasm32-wasi`, `cargo build --target wasm32-wasip1`, `wasm-opt -O3`.`).

### Prerequisites

- Target language version (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **WebAssembly** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Sandboxed contiguous byte array (`WebAssembly.Memory` in 64 KiB page units) completely disjoint from the execution call stack and code space (preventing ROP return-address overwrites!).), type soundness limits (Single-pass linear-time stack polymorphism and function-signature validation before instantiation; `call_indirect` validates table element signature at runtime.), and concurrency hazards (Shared linear memory (`new WebAssembly.Memory({ initial, maximum, shared: true })`) with atomic `i32.atomic.rmw.cmpxchg` and `memory.atomic.wait32`/`notify`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce W3C WebAssembly Core Specification 2.0, WASI (Preview 1 / Preview 2 Component Model).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Structured control flow (`block`, `loop`, `if`, `br`, `br_if`, `br_table` - irreducible arbitrary `goto` is forbidden by bytecode validation!), and typed value stack (`i32`, `i64`, `f32`, `f64`, `v128`, `funcref`, `externref`).
2. **Type System & Inference**: Single-pass linear-time stack polymorphism and function-signature validation before instantiation; `call_indirect` validates table element signature at runtime.
3. **Memory Management**: Sandboxed contiguous byte array (`WebAssembly.Memory` in 64 KiB page units) completely disjoint from the execution call stack and code space (preventing ROP return-address overwrites!).
4. **Concurrency & Async Programming**: Shared linear memory (`new WebAssembly.Memory({ initial, maximum, shared: true })`) with atomic `i32.atomic.rmw.cmpxchg` and `memory.atomic.wait32`/`notify`.
5. **Standard Library & Ecosystem**: WABT (`wat2wasm`, `wasm2wat`, `wasm-objdump`, `wasm-validate`), Binaryen (`wasm-opt`), Wasmtime, Node.js V8.
6. **Build Systems & Package Management**: `clang --target=wasm32-wasi`, `cargo build --target wasm32-wasip1`, `wasm-opt -O3`.
7. **Compiler / Interpreter Behavior**: Streaming baseline compilation (Liftoff in V8, Winch in Wasmtime) followed by optimizing tier (TurboFan / Cranelift).
8. **Debugging & Observability**: DWARF in custom sections, `wasm-objdump -d`, Chrome DevTools / `lldb` Wasmtime support.
9. **Security Hardening**: Enforce explicit `maximum` page limits on `memory` imports/exports and capability-based WASI preopened directory descriptors; audit linear-memory heap overflow between guest allocations.
10. **Performance Optimization**: 128-bit Fixed-Width SIMD (`v128`), `memory.copy`/`memory.fill` bulk memory ops, and minimizing JS <-> Wasm boundary crossings per frame.
11. **Error Handling Discipline**: Hardware/runtime `RuntimeError: unreachable` or `memory access out of bounds` traps cleanly isolated inside the host.
12. **Testing Methodologies**: Instantiate binary `.wasm` modules directly in Node.js V8 and verify exported functions and boundary traps.
13. **Interoperability & Cross-Platform ABI**: Typed numeric imports/exports, shared `Uint8Array(memory.buffer)` views, and WIT (Wasm Interface Types) Component Model.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/webassembly-linear-memory-wasi/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Wasm 1.0 / 2.0 (SIMD128, Bulk Memory, Multi-Value, Tail Call)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in WebAssembly**: Holding a cached `new Uint8Array(memory.buffer)` view in JS after Wasm calls `memory.grow` (detaches the old `ArrayBuffer`!), and passing unvalidated guest pointers.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
