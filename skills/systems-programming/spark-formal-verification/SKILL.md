---
name: spark-formal-verification
description: Specify and mathematically prove Absence of Run-Time Errors (AoRTE), data/information flow contracts, loop invariants, loop variants, and functional correctness in SPARK 2014 using GNATprove.
allowed-tools: execute_bash view_file write_to_file
---

# SPARK 2014 Deductive Formal Verification (AoRTE, Flow Analysis & Ghost Code)

Specify and mathematically prove Absence of Run-Time Errors (AoRTE), data/information flow contracts, loop invariants, loop variants, and functional correctness in SPARK 2014 using GNATprove.

## A. Identity

- **Skill Name**: `spark-formal-verification`
- **Domain**: `systems-programming`
- **Language / Representation**: **SPARK** (`Formal Verification Contract Sublanguage (Ada Subset)`)
- **Technical Relationship**: Formally verifiable subset and deductive contract language of Ada (`SPARK_Mode => On`), verified statically via GNATprove (Why3 / Z3 / CVC5 / Alt-Ergo).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **SPARK**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: SPARK 2014 Reference Manual, DO-178C Formal Methods Supplement (DO-333) (SPARK 2014 (GNATprove 13 / 14))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``gnatprove -P project.gpr --level=4 --mode=all` (Stone -> Bronze -> Silver -> Gold -> Platinum assurance levels).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **SPARK** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **SPARK**.

### Technical Triggers

- Files, build manifests, or prompts targeting **SPARK** (`spark_saturating_add.ads`, ``gnatprove -P project.gpr --level=4 --mode=all` (Stone -> Bronze -> Silver -> Gold -> Platinum assurance levels).`).

### Prerequisites

- Target language version (SPARK 2014 (GNATprove 13 / 14)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **SPARK** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (SPARK 2014 (GNATprove 13 / 14)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Static stack/global allocation or formally tracked single-owner pointers with zero garbage collection or leaks.), type soundness limits (Strict ownership move/borrow rules for local access types in SPARK (Rust-like non-aliasing pointer verification) and subtype predicates.), and concurrency hazards (Ravenscar protected objects verified free of data races and priority ceiling violations by GNATprove flow analysis.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce SPARK 2014 Reference Manual, DO-178C Formal Methods Supplement (DO-333).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `pragma SPARK_Mode (On)` banning aliasing, side-effecting functions, controlled types, and arbitrary gotos/exceptions.
2. **Type System & Inference**: Strict ownership move/borrow rules for local access types in SPARK (Rust-like non-aliasing pointer verification) and subtype predicates.
3. **Memory Management**: Static stack/global allocation or formally tracked single-owner pointers with zero garbage collection or leaks.
4. **Concurrency & Async Programming**: Ravenscar protected objects verified free of data races and priority ceiling violations by GNATprove flow analysis.
5. **Standard Library & Ecosystem**: SPARK Lemma Library (`SPARK.Lemmas`), `SPARK.Containers.Formal`, Why3, Z3, CVC5, Alt-Ergo.
6. **Build Systems & Package Management**: `gnatprove -P project.gpr --level=4 --mode=all` (Stone -> Bronze -> Silver -> Gold -> Platinum assurance levels).
7. **Compiler / Interpreter Behavior**: Generates Verification Conditions (VCs) for every possible division by zero, array index, range check, and arithmetic overflow.
8. **Debugging & Observability**: Counterexample trace inspection (`--ce`), `pragma Assert_And_Cut`, and ghost variables/functions (`with Ghost`).
9. **Security Hardening**: Information-flow contracts (`Depends => (Ciphertext => (Plaintext, Key))`) proving zero secret leakage to untrusted outputs.
10. **Performance Optimization**: Once `Silver`/`Gold` AoRTE is mathematically proven, runtime checks (`-gnatp`) can be safely suppressed with formal justification.
11. **Error Handling Discipline**: Total functions: preconditions (`Pre`) forbid invalid calls at compile time; `Contract_Cases` partition behavior exhaustively.
12. **Testing Methodologies**: Combine SMT deductive proofs (`gnatprove`) with boundary execution tests on hardware.
13. **Interoperability & Cross-Platform ABI**: Isolate hardware MMIO or C FFI inside `SPARK_Mode => Off` package bodies while exposing a formally specified `SPARK_Mode => On` package spec.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/systems-programming/spark-formal-verification/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (SPARK 2014 (GNATprove 13 / 14)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in SPARK**: Writing weak `Loop_Invariant` clauses that fail inductive step proofs, omitting `Loop_Variant` for termination, and under-specifying `Global`/`Depends`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
