---
name: d-systems-programming
description: Write, audit, and verify D systems code using @safe, @nogc, nothrow, pure function attributes, DIP1000 scoped lifetime tracking, Design by Introspection templates, and LDC/GDC native compilation.
allowed-tools: execute_bash view_file write_to_file
---

# D Systems Programming (@safe, @nogc, dip1000 Scope Pointers & -betterC)

Write, audit, and verify D systems code using @safe, @nogc, nothrow, pure function attributes, DIP1000 scoped lifetime tracking, Design by Introspection templates, and LDC/GDC native compilation.

## A. Identity

- **Skill Name**: `d-systems-programming`
- **Domain**: `systems-programming`
- **Language / Representation**: **D** (`Systems Programming Language`)
- **Technical Relationship**: Native systems programming language supporting both GC-managed application code and `@safe @nogc nothrow pure` freestanding/C-compatible `-betterC` systems programming.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **D**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: D Language Specification (DMD / LDC2 / GDC), DIP1000 Scoped Pointers (D 2.105+ (LDC 1.36+))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``dub.json`/`dub.sdl`, `ldc2 -O3 -release -boundscheck=safeonly -preview=dip1000`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **D** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **D**.

### Technical Triggers

- Files, build manifests, or prompts targeting **D** (`nogc_ring_slice.d`, ``dub.json`/`dub.sdl`, `ldc2 -O3 -release -boundscheck=safeonly -preview=dip1000`.`).

### Prerequisites

- Target language version (D 2.105+ (LDC 1.36+)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **D** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (D 2.105+ (LDC 1.36+)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Enforce `@nogc` in real-time/kernel paths, `scope`/`return scope` (`-preview=dip1000`) to prevent escaping stack pointers, and `-betterC` for zero runtime dependency.), type soundness limits (Function safety attributes (`@safe`, `@trusted`, `@system`), purity (`pure`), GC-freedom (`@nogc`), and template constraints (`if (isIntegral!T)`).), and concurrency hazards (`shared` type qualifier preventing accidental thread sharing, `core.atomic`, and message-passing `std.concurrency`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce D Language Specification (DMD / LDC2 / GDC), DIP1000 Scoped Pointers.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `scope(exit)`/`scope(failure)` deterministic cleanup, `in`/`out` contract blocks, and `static if` Design by Introspection.
2. **Type System & Inference**: Function safety attributes (`@safe`, `@trusted`, `@system`), purity (`pure`), GC-freedom (`@nogc`), and template constraints (`if (isIntegral!T)`).
3. **Memory Management**: Enforce `@nogc` in real-time/kernel paths, `scope`/`return scope` (`-preview=dip1000`) to prevent escaping stack pointers, and `-betterC` for zero runtime dependency.
4. **Concurrency & Async Programming**: `shared` type qualifier preventing accidental thread sharing, `core.atomic`, and message-passing `std.concurrency`.
5. **Standard Library & Ecosystem**: Phobos (`std.algorithm`, `std.range`), `core.stdc`, DUB package manager.
6. **Build Systems & Package Management**: `dub.json`/`dub.sdl`, `ldc2 -O3 -release -boundscheck=safeonly -preview=dip1000`.
7. **Compiler / Interpreter Behavior**: CTFE (Compile-Time Function Execution), slice bounds checks preserved in `@safe` code even in `-release` mode.
8. **Debugging & Observability**: GDB/LLDB DWARF support, `-fsanitize=address` in LDC2.
9. **Security Hardening**: Keep `@trusted` wrappers minimal and audit every pointer slice construction `ptr[0 .. len]` inside `@trusted`.
10. **Performance Optimization**: Lazy range pipelines (zero intermediate allocations), `ldc.simd`, and `struct` value semantics on the stack.
11. **Error Handling Discipline**: `nothrow` error-code/tagged-union returns in `@nogc` systems code (`Exceptions` allocate on GC heap unless pre-allocated/DIP1008).
12. **Testing Methodologies**: Built-in `unittest {}` blocks verified via `dub test`.
13. **Interoperability & Cross-Platform ABI**: `extern(C)` and `extern(C++)` ABI linkage plus ImportC direct `.c` file compilation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/d-systems-programming/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (D 2.105+ (LDC 1.36+)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in D**: Escaping slice references to stack arrays without `-preview=dip1000`, and triggering hidden GC allocations via array concatenation `~` in hot loops.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
