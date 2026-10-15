---
name: llvm-ir-ssa-codegen
description: Generate, analyze, optimize, and verify LLVM IR (.ll) modules using LLVM 15+ opaque pointers (ptr), strict SSA dominance, phi nodes, getelementptr inbounds semantics, nuw/nsw poison-value tracking, freeze, and Alive2 translation validation.
allowed-tools: execute_bash view_file write_to_file
---

# LLVM IR (LLVM 15-19 Opaque Pointers) SSA Dominance, GEP Inbounds, Poison/Freeze & Optimization

Generate, analyze, optimize, and verify LLVM IR (.ll) modules using LLVM 15+ opaque pointers (ptr), strict SSA dominance, phi nodes, getelementptr inbounds semantics, nuw/nsw poison-value tracking, freeze, and Alive2 translation validation.

## A. Identity

- **Skill Name**: `llvm-ir-ssa-codegen`
- **Domain**: `programming-languages`
- **Language / Representation**: **LLVM IR** (`Compiler Static Single Assignment Intermediate Representation`)
- **Technical Relationship**: Typed, target-aware SSA intermediate representation (`.ll` text / `.bc` bitcode) sitting between language frontends (`clang`, `rustc`, `zig`, `swiftc`, `julia`) and LLVM machine backends.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **LLVM IR**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: LLVM Language Reference Manual (LangRef LLVM 15-19) (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``opt -passes=verify module.ll -disable-output` and `llc -O2 -filetype=obj module.ll`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **LLVM IR** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **LLVM IR**.

### Technical Triggers

- Files, build manifests, or prompts targeting **LLVM IR** (`opaque_ptr_ssa_dot.ll`, ``opt -passes=verify module.ll -disable-output` and `llc -O2 -filetype=obj module.ll`.`).

### Prerequisites

- Target language version (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **LLVM IR** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Entry-block `alloca` stack slots promoted to SSA registers via `mem2reg` (`sroa`), explicit `align N` on loads/stores, and `!tbaa` / `noalias` metadata.), type soundness limits (First-class sized types (`i1`, `i8`, `i32`, `i64`, `float`, `double`, `<4 x float>`, `[N x T]`, `{ i32, ptr }`) and LLVM 15+ unified opaque pointer `ptr` (explicit type passed to `load`/`getelementptr` instead of `i32*`).), and concurrency hazards (`atomicrmw`, `cmpxchg`, `fence syncscope("singlethread"|"") seq_cst|acq_rel|acquire|release`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce LLVM Language Reference Manual (LangRef LLVM 15-19).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Infinite virtual registers (`%0`, `%x`) assigned exactly once (Static Single Assignment), explicit basic blocks ending with a terminator (`ret`, `br`, `switch`, `unreachable`), and `phi` nodes at control-flow joins.
2. **Type System & Inference**: First-class sized types (`i1`, `i8`, `i32`, `i64`, `float`, `double`, `<4 x float>`, `[N x T]`, `{ i32, ptr }`) and LLVM 15+ unified opaque pointer `ptr` (explicit type passed to `load`/`getelementptr` instead of `i32*`).
3. **Memory Management**: Entry-block `alloca` stack slots promoted to SSA registers via `mem2reg` (`sroa`), explicit `align N` on loads/stores, and `!tbaa` / `noalias` metadata.
4. **Concurrency & Async Programming**: `atomicrmw`, `cmpxchg`, `fence syncscope("singlethread"|"") seq_cst|acq_rel|acquire|release`.
5. **Standard Library & Ecosystem**: `opt` (`opt -passes=verify,mem2reg,instcombine,gvn`), `llc`, `llvm-as`, `llvm-dis`, `lli`, `Alive2` (`alive-tv`).
6. **Build Systems & Package Management**: `opt -passes=verify module.ll -disable-output` and `llc -O2 -filetype=obj module.ll`.
7. **Compiler / Interpreter Behavior**: Distinguish immediate UB (dividing by `0`, dereferencing `null`/`poison`) from deferred `poison` (`add nsw` overflow produces `poison`, which triggers UB if branched on unless stabilized with `freeze`).
8. **Debugging & Observability**: `opt -print-after-all`, `llvm-extract`, `bugpoint` / `llvm-reduce` crash reducer.
9. **Security Hardening**: Enforce `inbounds` on `getelementptr` only when offset arithmetic stays within the allocated object + 1-past-end byte; emit `llvm.ubsantrap` for checked arithmetic.
10. **Performance Optimization**: Place all `alloca` instructions in the entry basic block (never inside loops, which causes dynamic stack growth and prevents `mem2reg` SSA promotion!).
11. **Error Handling Discipline**: `invoke` / `landingpad` (Itanium C++/Rust unwinding) or `@llvm.experimental.deoptimize`.
12. **Testing Methodologies**: Verify SSA single-assignment, CFG dominance before use, and `phi` predecessor completeness.
13. **Interoperability & Cross-Platform ABI**: `target datalayout` and `target triple` ABI lowering (`sret`, `byval`, `zext`/`sext` parameter attributes).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/llvm-ir-ssa-codegen/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in LLVM IR**: Using deprecated typed pointers (`i32*`) in LLVM 15+, placing `alloca` inside a loop body, and branching on a potentially `poison` condition without `freeze`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
