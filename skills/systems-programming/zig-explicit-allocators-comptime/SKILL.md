---
name: zig-explicit-allocators-comptime
description: Develop, debug, and verify Zig systems software using explicit std.mem.Allocator injection, defer/errdefer deterministic unwind chains, comptime type reflection, sentinel slices, and @cImport C ABI interoperability.
allowed-tools: execute_bash view_file write_to_file
---

# Zig Explicit Allocators, errdefer Resource Safety, Comptime & C Interop

Develop, debug, and verify Zig systems software using explicit std.mem.Allocator injection, defer/errdefer deterministic unwind chains, comptime type reflection, sentinel slices, and @cImport C ABI interoperability.

## A. Identity

- **Skill Name**: `zig-explicit-allocators-comptime`
- **Domain**: `systems-programming`
- **Language / Representation**: **Zig** (`Systems Programming Language`)
- **Technical Relationship**: Low-level systems language with first-class C ABI drop-in cross-compilation and compile-time (`comptime`) generics.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Zig**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Zig Language Reference (0.12 / 0.13 / 0.14) (Zig 0.12 / 0.13+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``build.zig` and `build.zig.zon` declarative package graph with built-in cross-compiling (`-Dtarget=x86_64-linux-musl`).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Zig** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Zig**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Zig** (`comptime_matrix_arena.zig`, ``build.zig` and `build.zig.zon` declarative package graph with built-in cross-compiling (`-Dtarget=x86_64-linux-musl`).`).

### Prerequisites

- Target language version (Zig 0.12 / 0.13+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Zig** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Zig 0.12 / 0.13+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (No hidden heap allocations; pass `std.mem.Allocator` explicitly, pair allocations immediately with `errdefer`/`defer`, and test with `std.testing.allocator`.), type soundness limits (`comptime` generic functions returning `type`, tagged unions (`union(enum)`), arbitrary bit-width integers (`u3`, `i24`), and explicit pointer alignment.), and concurrency hazards (`std.Thread`, `std.atomic.Value`, and evented I/O loops with explicit stack-frame sizing.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Zig Language Reference (0.12 / 0.13 / 0.14).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Zero hidden control flow, zero operator overloading, explicit error unions (`!T`), and compile-time code execution (`comptime`).
2. **Type System & Inference**: `comptime` generic functions returning `type`, tagged unions (`union(enum)`), arbitrary bit-width integers (`u3`, `i24`), and explicit pointer alignment.
3. **Memory Management**: No hidden heap allocations; pass `std.mem.Allocator` explicitly, pair allocations immediately with `errdefer`/`defer`, and test with `std.testing.allocator`.
4. **Concurrency & Async Programming**: `std.Thread`, `std.atomic.Value`, and evented I/O loops with explicit stack-frame sizing.
5. **Standard Library & Ecosystem**: `std.mem`, `std.heap.ArenaAllocator`, `std.heap.FixedBufferAllocator`, `@cImport` / `translate-c`.
6. **Build Systems & Package Management**: `build.zig` and `build.zig.zon` declarative package graph with built-in cross-compiling (`-Dtarget=x86_64-linux-musl`).
7. **Compiler / Interpreter Behavior**: Safety-checked `ReleaseSafe` vs `ReleaseFast`/`ReleaseSmall`; illegal behavior traps on integer overflow and bounds violations in safe modes.
8. **Debugging & Observability**: DWARF stack traces on error return traces, GDB/LLDB inspection, and `std.testing.allocator` leak detection.
9. **Security Hardening**: Distinguish single-item pointers (`*T`), many-item pointers (`[*]T`), bounds-checked slices (`[]T`), and null-terminated sentinel slices (`[:0]const u8`).
10. **Performance Optimization**: `@Vector(N, T)` portable SIMD, `MultiArrayList` Struct-of-Arrays (SoA) cache layout, and `comptime` lookup generation.
11. **Error Handling Discipline**: Exhaustive error sets (`error{OutOfMemory, Overflow}`), `try`/`catch`, and `errdefer` rollback on partial initialization failure.
12. **Testing Methodologies**: Inline `test "..." {}` blocks executed via `zig test` with automatic memory-leak detection.
13. **Interoperability & Cross-Platform ABI**: Direct C header ingestion via `@cInclude`, `export fn` with `callconv(.C)`, and `extern struct` layout compatibility.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/zig-explicit-allocators-comptime/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Zig 0.12 / 0.13+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Zig**: Returning pointers to stack-local arrays, omitting `errdefer` between sequential allocations, and using `[*]T` where a bounds-checked slice `[]T` is required.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
