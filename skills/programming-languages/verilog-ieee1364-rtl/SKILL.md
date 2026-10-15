---
name: verilog-ieee1364-rtl
description: Design, lint, simulate, and verify synthesizable IEEE 1364-2005 Verilog RTL modules using `default_nettype none, strict blocking (=) vs non-blocking (<=) rules, latch-free combinational blocks, and 2-FF Gray-code CDC synchronizers.
allowed-tools: execute_bash view_file write_to_file
---

# Verilog (IEEE 1364-2005) Synthesizable RTL, Non-Blocking Assignments, FSMs & CDC

Design, lint, simulate, and verify synthesizable IEEE 1364-2005 Verilog RTL modules using `default_nettype none, strict blocking (=) vs non-blocking (<=) rules, latch-free combinational blocks, and 2-FF Gray-code CDC synchronizers.

## A. Identity

- **Skill Name**: `verilog-ieee1364-rtl`
- **Domain**: `programming-languages`
- **Language / Representation**: **Verilog** (`Hardware Description Language (HDL)`)
- **Technical Relationship**: IEEE 1364-2005 RTL hardware description language synthesized into FPGA/ASIC digital logic gates and flip-flops (not a sequential software programming language).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Verilog**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: IEEE Std 1364-2005 (Verilog HDL), Clifford Cummings Nonblocking & CDC Guidelines (Verilog-2001 / IEEE 1364-2005)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Fusesoc / Makefile driving `verilator --lint-only -Wall` and `iverilog -g2005`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Verilog** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Verilog**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Verilog** (`axis_skid_buffer.v`, `Fusesoc / Makefile driving `verilator --lint-only -Wall` and `iverilog -g2005`.`).

### Prerequisites

- Target language version (Verilog-2001 / IEEE 1364-2005), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Verilog** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Verilog-2001 / IEEE 1364-2005), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Hardware storage elements: synchronous D-flip-flop registers (`reg`), inferred Block RAM (BRAM) arrays, and distributed LUT RAM.), type soundness limits (4-state logic (`0`, `1`, `X`, `Z`), explicit bit widths (`[WIDTH-1:0]`), `wire` nets vs `reg` variables, and `signed` arithmetic rules.), and concurrency hazards (All `always` blocks and continuous `assign` statements execute concurrently in hardware; use non-blocking `<=` in clocked `always @(posedge clk)` and blocking `=` in combinational `always @(*)`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce IEEE Std 1364-2005 (Verilog HDL), Clifford Cummings Nonblocking & CDC Guidelines.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `default_nettype none` at top of every file (prevents 1-bit implicit wire typos!), ANSI port declarations, and parameterized `generate` blocks.
2. **Type System & Inference**: 4-state logic (`0`, `1`, `X`, `Z`), explicit bit widths (`[WIDTH-1:0]`), `wire` nets vs `reg` variables, and `signed` arithmetic rules.
3. **Memory Management**: Hardware storage elements: synchronous D-flip-flop registers (`reg`), inferred Block RAM (BRAM) arrays, and distributed LUT RAM.
4. **Concurrency & Async Programming**: All `always` blocks and continuous `assign` statements execute concurrently in hardware; use non-blocking `<=` in clocked `always @(posedge clk)` and blocking `=` in combinational `always @(*)`.
5. **Standard Library & Ecosystem**: Icarus Verilog (`iverilog`), Verilator (`verilator --lint-only -Wall`), Yosys synthesis, GTKWave.
6. **Build Systems & Package Management**: Fusesoc / Makefile driving `verilator --lint-only -Wall` and `iverilog -g2005`.
7. **Compiler / Interpreter Behavior**: RTL synthesis infers unintended transparent latches if any combinational `always @(*)` path omits an output assignment; avoid `X`-optimism in `case` statements.
8. **Debugging & Observability**: VCD/FST waveform dumps (`$dumpfile`, `$dumpvars`), Verilator lint diagnostics (`WIDTH`, `UNOPTFLAT`, `LATCH`).
9. **Security Hardening**: Ensure FSMs have a safe `default:` state recovery transition to prevent fault-injection lockup in undefined encodings.
10. **Performance Optimization**: Pipeline deep combinational paths with register stages to meet setup/hold static timing closure ($f_{\max}$).
11. **Error Handling Discipline**: Valid/ready AXI-Stream handshake backpressure (`tvalid && tready`) without combinational loops between `ready` and `valid`.
12. **Testing Methodologies**: Self-checking testbenches checking reset state, full/empty FIFO boundaries, and multi-cycle protocol handshakes.
13. **Interoperability & Cross-Platform ABI**: Verilog Procedural Interface (VPI) and Verilator C++ cycle-accurate simulation wrappers.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/verilog-ieee1364-rtl/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Verilog-2001 / IEEE 1364-2005), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Verilog**: Mixing `=` and `<=` on the same signal, omitting `default_nettype none`, inferring latches in incomplete `if`/`case` blocks, and crossing clock domains with multi-bit binary counters instead of Gray code.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
