---
name: odin-systems-programming
description: Engineer and verify data-oriented Odin systems software using implicit context.allocator and context.temp_allocator propagation, #soa struct-of-arrays layouts, defer cleanup, and distinct scalar/matrix types.
allowed-tools: execute_bash view_file write_to_file
---

# Odin Data-Oriented Systems Programming (Context Allocators, #soa & Explicit Layout)

Engineer and verify data-oriented Odin systems software using implicit context.allocator and context.temp_allocator propagation, #soa struct-of-arrays layouts, defer cleanup, and distinct scalar/matrix types.

## A. Identity

- **Skill Name**: `odin-systems-programming`
- **Domain**: `systems-programming`
- **Language / Representation**: **Odin** (`Systems Programming Language`)
- **Technical Relationship**: Data-oriented systems programming language with implicit `context` allocator/logger propagation and first-class SOA (Struct-of-Arrays) types.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Odin**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Odin Programming Language Specification (Odin dev-2024+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``odin build src/ -vet -strict-style -o:speed` and `odin test`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Odin** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Odin**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Odin** (`soa_tracking_arena.odin`, ``odin build src/ -vet -strict-style -o:speed` and `odin test`.`).

### Prerequisites

- Target language version (Odin dev-2024+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Odin** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Odin dev-2024+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Every scope carries an implicit `context` struct (`context.allocator`, `context.temp_allocator`); track leaks via `mem.Tracking_Allocator`.), type soundness limits (Distinct primitive types (`distinct int`), built-in `matrix[R, C]T` and `#simd[N]T`, bit_set, and `#soa[]Entity` native Struct-of-Arrays slices.), and concurrency hazards (`core:thread`, `core:sync`, and explicit atomic operations (`sync.atomic_load_explicit`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Odin Programming Language Specification.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit procedure overloading, `defer` (statement-scoped and block-scoped), `or_return` / `or_else` error propagation, and zero constructors/destructors.
2. **Type System & Inference**: Distinct primitive types (`distinct int`), built-in `matrix[R, C]T` and `#simd[N]T`, bit_set, and `#soa[]Entity` native Struct-of-Arrays slices.
3. **Memory Management**: Every scope carries an implicit `context` struct (`context.allocator`, `context.temp_allocator`); track leaks via `mem.Tracking_Allocator`.
4. **Concurrency & Async Programming**: `core:thread`, `core:sync`, and explicit atomic operations (`sync.atomic_load_explicit`).
5. **Standard Library & Ecosystem**: `core:mem`, `core:math/linalg`, `core:sys/posix`, `vendor:vulkan`.
6. **Build Systems & Package Management**: `odin build src/ -vet -strict-style -o:speed` and `odin test`.
7. **Compiler / Interpreter Behavior**: LLVM backend with built-in bounds checking (`#no_bounds_check` opt-out) and `#bounds_check` enforcement.
8. **Debugging & Observability**: Tracking allocator leak/bad-free reports (`track.allocation_map`, `track.bad_free_array`) and GDB/LLDB DWARF symbols.
9. **Security Hardening**: Mandatory array/slice bounds checks by default and explicit `#raw_union` tagging.
10. **Performance Optimization**: `#soa` dynamic and fixed arrays for SIMD cache-line utilization without manual AoS-to-SoA refactoring.
11. **Error Handling Discipline**: Multiple return values `(val: T, err: Allocator_Error)` propagated concisely with `or_return`.
12. **Testing Methodologies**: `@(test)` procedures taking `t: ^testing.T` verified with `mem.Tracking_Allocator`.
13. **Interoperability & Cross-Platform ABI**: `foreign import` blocks with static/dynamic C libraries and `#ccall` calling convention.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/odin-systems-programming/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Odin dev-2024+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Odin**: Retaining pointers allocated from `context.temp_allocator` across frame resets (`free_all(context.temp_allocator)`), and forgetting `-vet`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
