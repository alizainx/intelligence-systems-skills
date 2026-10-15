---
name: vhdl-strong-typed-rtl
description: Design, simulate, and verify synthesizable VHDL-2008 RTL entities and architectures using ieee.numeric_std (unsigned/signed), std_logic_1164, synchronous rising_edge(clk) processes, and GHDL verification.
allowed-tools: execute_bash view_file write_to_file
---

# VHDL (IEEE 1076-2008) numeric_std, Safe FSMs, Generics & Synchronous RTL

Design, simulate, and verify synthesizable VHDL-2008 RTL entities and architectures using ieee.numeric_std (unsigned/signed), std_logic_1164, synchronous rising_edge(clk) processes, and GHDL verification.

## A. Identity

- **Skill Name**: `vhdl-strong-typed-rtl`
- **Domain**: `programming-languages`
- **Language / Representation**: **VHDL** (`Hardware Description Language (HDL)`)
- **Technical Relationship**: Strongly typed IEEE 1076-2008/2019 hardware description language widely required in defense, aerospace (DO-254), and European ASIC/FPGA flows.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **VHDL**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: IEEE Std 1076-2008 / IEEE Std 1076-2019 (VHDL), DO-254 (VHDL-93 / VHDL-2008 / VHDL-2019)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``ghdl -a --std=08 -Werror`, VUnit `run.py`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **VHDL** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **VHDL**.

### Technical Triggers

- Files, build manifests, or prompts targeting **VHDL** (`saturating_counter.vhdl`, ``ghdl -a --std=08 -Werror`, VUnit `run.py`.`).

### Prerequisites

- Target language version (VHDL-93 / VHDL-2008 / VHDL-2019), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **VHDL** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (VHDL-93 / VHDL-2008 / VHDL-2019), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Signal drivers (delta-cycle scheduled updates `<=`) vs process-local immediate `variable` (`:=`) assignments.), type soundness limits (Strict nominal typing: `std_logic`, `std_logic_vector` (bag of bits), `unsigned` and `signed` from `ieee.numeric_std`, `natural`/`positive` integer ranges, and enumerated FSM states.), and concurrency hazards (Concurrent signal assignments, `process` blocks, and `generate` (`for ... generate`, `if ... generate`) hardware replication.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce IEEE Std 1076-2008 / IEEE Std 1076-2019 (VHDL), DO-254.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `entity` interface vs `architecture` implementation, `process(all)` (VHDL-2008 combinational sensitivity), and `rising_edge(clk)` synchronous clocking.
2. **Type System & Inference**: Strict nominal typing: `std_logic`, `std_logic_vector` (bag of bits), `unsigned` and `signed` from `ieee.numeric_std`, `natural`/`positive` integer ranges, and enumerated FSM states.
3. **Memory Management**: Signal drivers (delta-cycle scheduled updates `<=`) vs process-local immediate `variable` (`:=`) assignments.
4. **Concurrency & Async Programming**: Concurrent signal assignments, `process` blocks, and `generate` (`for ... generate`, `if ... generate`) hardware replication.
5. **Standard Library & Ecosystem**: GHDL (`ghdl -a --std=08`), VUnit, OSVVM (Open Source VHDL Verification Methodology), Vivado/Quartus.
6. **Build Systems & Package Management**: `ghdl -a --std=08 -Werror`, VUnit `run.py`.
7. **Compiler / Interpreter Behavior**: Delta-cycle simulation semantics: signal assignments `<=` take effect on the next delta cycle, preventing order-dependent race conditions between processes.
8. **Debugging & Observability**: GHDL waveform export (`--wave=sim.ghw`) with GTKWave and VHDL `assert ... report ... severity failure;`.
9. **Security Hardening**: Never import non-standard Synopsys `std_logic_arith` or `std_logic_unsigned` (ambiguous signed/unsigned overloading); always use standard `ieee.numeric_std`!
10. **Performance Optimization**: Use integer ranges (`natural range 0 to MAX_COUNT - 1`) for counters to avoid 32-bit full-width adder inference.
11. **Error Handling Discipline**: `when others =>` recovery state in every FSM `case` statement and compile-time `assert` checks on `generic` parameters.
12. **Testing Methodologies**: Self-checking VHDL-2008 testbenches using `std.env.stop` / `assert`.
13. **Interoperability & Cross-Platform ABI**: VHPIDIRECT C bindings in GHDL and mixed-language VHDL/SystemVerilog hierarchy instantiation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/vhdl-strong-typed-rtl/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (VHDL-93 / VHDL-2008 / VHDL-2019), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in VHDL**: Using `std_logic_unsigned`/`std_logic_arith` instead of `ieee.numeric_std`, using `clk'event and clk = '1'` instead of `rising_edge(clk)`, and incomplete sensitivity lists in pre-2008 combinational processes.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
