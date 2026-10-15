---
name: nim-systems-programming
description: Develop and verify Nim systems software using deterministic --mm:orc / --mm:arc memory management, sink/lent move semantics, .raises: [] effect tracking, distinct types, and zero-overhead C/C++ codegen.
allowed-tools: execute_bash view_file write_to_file
---

# Nim Systems Programming (ARC/ORC Memory Management, Effect System & Hygienic Macros)

Develop and verify Nim systems software using deterministic --mm:orc / --mm:arc memory management, sink/lent move semantics, .raises: [] effect tracking, distinct types, and zero-overhead C/C++ codegen.

## A. Identity

- **Skill Name**: `nim-systems-programming`
- **Domain**: `systems-programming`
- **Language / Representation**: **Nim** (`Systems Programming Language`)
- **Technical Relationship**: Statically typed systems language compiling to C/C++ with deterministic ARC/ORC reference counting and hygienic AST macro metaprogramming.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Nim**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Nim Manual (Nim 2.0+ Default ARC/ORC Memory Model) (Nim 2.0 / 2.2+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``nimble build`, `nim c --mm:orc --panics:on -d:release`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Nim** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Nim**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Nim** (`arc_distinct_units.nim`, ``nimble build`, `nim c --mm:orc --panics:on -d:release`.`).

### Prerequisites

- Target language version (Nim 2.0 / 2.2+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Nim** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Nim 2.0 / 2.2+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (`--mm:orc` (cycle-collecting deterministic RC) or `--mm:arc` (hard real-time deterministic RC without cycle collector); use `sink` and `lent` to avoid refcount traffic.), type soundness limits (`distinct` types (`typeMeters = distinct float64`), ordinal subranges (`range[0..255]`), concept constraints, and compile-time effect tracking (`.raises: []`, `.noSideEffect`).), and concurrency hazards (`Isolated[T]` ownership transfer across threads (`std/tasks`, `malebolgia`) preventing shared mutable heap races under ARC/ORC.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Nim Manual (Nim 2.0+ Default ARC/ORC Memory Model).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Indentation-based syntax with hygienic typed AST macros (`macro`), `defer:`, and ``=destroy``/``=sink``/``=copy`` lifetime hooks.
2. **Type System & Inference**: `distinct` types (`typeMeters = distinct float64`), ordinal subranges (`range[0..255]`), concept constraints, and compile-time effect tracking (`.raises: []`, `.noSideEffect`).
3. **Memory Management**: `--mm:orc` (cycle-collecting deterministic RC) or `--mm:arc` (hard real-time deterministic RC without cycle collector); use `sink` and `lent` to avoid refcount traffic.
4. **Concurrency & Async Programming**: `Isolated[T]` ownership transfer across threads (`std/tasks`, `malebolgia`) preventing shared mutable heap races under ARC/ORC.
5. **Standard Library & Ecosystem**: Nimble package manager, `std/strformat`, `std/monotimes`, `chronos` async.
6. **Build Systems & Package Management**: `nimble build`, `nim c --mm:orc --panics:on -d:release`.
7. **Compiler / Interpreter Behavior**: Compiles to ISO C/C++ in `nimcache/`; respects backend C compiler sanitizer flags (`--passC:-fsanitize=address,undefined`).
8. **Debugging & Observability**: `--debugger:native` emitting `#line` directives mapped to Nim source in GDB/LLDB.
9. **Security Hardening**: Compile-time `.raises: [IOError]` effect annotations and runtime bounds/overflow checks (`--overflowChecks:on`).
10. **Performance Optimization**: `--mm:arc` deterministic destruction, value-type `object` (stack) vs `ref object` (heap), and `=sink` move optimization.
11. **Error Handling Discipline**: Checked exception tracking via `{.raises: [].}` pragma or `Result[T, E]` value returns.
12. **Testing Methodologies**: `unittest` and `testament` suites compiled with `--mm:orc` and C sanitizers.
13. **Interoperability & Cross-Platform ABI**: `{.importc, header: "...".}` and `{.exportc, cdecl.}` zero-glue C/C++ FFI.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/nim-systems-programming/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Nim 2.0 / 2.2+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Nim**: Creating reference cycles under `--mm:arc` without `{.cursor.}` annotations, and omitting `{.raises: [].}` on C FFI callbacks.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
