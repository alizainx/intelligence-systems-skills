---
name: ada-systems-engineering
description: Architect, implement, and verify safety-critical Ada 2012/2022 software using distinct numeric types, constrained array subtypes, representation clauses, Ravenscar/Jorvik deterministic tasking, and storage pools.
allowed-tools: execute_bash view_file write_to_file
---

# Ada (Ada 2012/2022) Strong Subtyping, Ravenscar Tasking & Representation Clauses

Architect, implement, and verify safety-critical Ada 2012/2022 software using distinct numeric types, constrained array subtypes, representation clauses, Ravenscar/Jorvik deterministic tasking, and storage pools.

## A. Identity

- **Skill Name**: `ada-systems-engineering`
- **Domain**: `systems-programming`
- **Language / Representation**: **Ada** (`Systems Programming Language`)
- **Technical Relationship**: Strongly typed, safety-critical systems language standardized for avionics, rail, space, and defense (DO-178C / EN 50128).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Ada**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 8652:2012 (Ada 2012), ISO/IEC 8652:2023 (Ada 2022), DO-178C (Ada 2005 / Ada 2012 / Ada 2022)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`GPRbuild project files (`.gpr`) and Alire (`alire.toml`) with `-gnatwa -gnatwe -gnatVa` validity/overflow checks.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Ada** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Ada**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Ada** (`telemetry_packet.ads`, `GPRbuild project files (`.gpr`) and Alire (`alire.toml`) with `-gnatwa -gnatwe -gnatVa` validity/overflow checks.`).

### Prerequisites

- Target language version (Ada 2005 / Ada 2012 / Ada 2022), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Ada** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Ada 2005 / Ada 2012 / Ada 2022), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Stack-allocated unconstrained arrays (`String`), bounded containers (`Ada.Containers.Bounded_Vectors`), and custom `System.Storage_Pools` without `Unchecked_Deallocation`.), type soundness limits (Nominal distinct numeric types (`type Meters is new Float`), constrained range subtypes (`subtype Percent is Integer range 0 .. 100`), and discriminated records.), and concurrency hazards (Protected objects (`protected type` with ceiling priority locking) and deterministic `pragma Profile (Ravenscar)` / `Jorvik` real-time tasks.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 8652:2012 (Ada 2012), ISO/IEC 8652:2023 (Ada 2022), DO-178C.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit package specifications (`.ads`) vs bodies (`.adb`), parameter modes (`in`, `out`, `in out`), and aspect specifications (`with Pre => ...`).
2. **Type System & Inference**: Nominal distinct numeric types (`type Meters is new Float`), constrained range subtypes (`subtype Percent is Integer range 0 .. 100`), and discriminated records.
3. **Memory Management**: Stack-allocated unconstrained arrays (`String`), bounded containers (`Ada.Containers.Bounded_Vectors`), and custom `System.Storage_Pools` without `Unchecked_Deallocation`.
4. **Concurrency & Async Programming**: Protected objects (`protected type` with ceiling priority locking) and deterministic `pragma Profile (Ravenscar)` / `Jorvik` real-time tasks.
5. **Standard Library & Ecosystem**: GNAT Toolchain, Alire (`alr`) package manager, `Ada.Real_Time`, `Interfaces.C`.
6. **Build Systems & Package Management**: GPRbuild project files (`.gpr`) and Alire (`alire.toml`) with `-gnatwa -gnatwe -gnatVa` validity/overflow checks.
7. **Compiler / Interpreter Behavior**: GNAT runtime `Constraint_Error` checks on range/index/overflow (`-gnato`) and elaboration order analysis (`pragma Pure`, `pragma Preelaborate`).
8. **Debugging & Observability**: GDB with Ada mode (`catch exception`), `gnatmem`, and stack usage analysis (`-fcallgraph-info`).
9. **Security Hardening**: Eliminate buffer overruns via first/last array attributes (`Arr'First .. Arr'Last`) and forbid `Unchecked_Conversion` without size/alignment static checks.
10. **Performance Optimization**: `pragma Inline`, zero-copy slice views, and bit-exact hardware register overlays via representation clauses (`for Reg use record ...`).
11. **Error Handling Discipline**: Design by contract (`Dynamic_Predicate`, `Type_Invariant`) combined with bounded exception handlers in non-Ravenscar profiles.
12. **Testing Methodologies**: AUnit test harnesses and boundary range subtype testing.
13. **Interoperability & Cross-Platform ABI**: `with Convention => C, Export => True, External_Name => "..."` using `Interfaces.C` types.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/ada-systems-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Ada 2005 / Ada 2012 / Ada 2022), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Ada**: Hardcoding `1 .. Length` instead of `Arr'Range`, elaboration cycles across packages, and using heap `access` types in safety-critical profiles.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
