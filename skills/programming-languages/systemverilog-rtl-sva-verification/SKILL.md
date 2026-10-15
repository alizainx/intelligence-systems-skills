---
name: systemverilog-rtl-sva-verification
description: Design and formally verify SystemVerilog RTL and verification environments using logic types, always_ff/always_comb intent blocks, unique/priority case, modport interfaces, and SystemVerilog Assertions (SVA).
allowed-tools: execute_bash view_file write_to_file
---

# SystemVerilog (IEEE 1800-2017/2023) always_ff/always_comb, Packed Structs, Interfaces & SVA

Design and formally verify SystemVerilog RTL and verification environments using logic types, always_ff/always_comb intent blocks, unique/priority case, modport interfaces, and SystemVerilog Assertions (SVA).

## A. Identity

- **Skill Name**: `systemverilog-rtl-sva-verification`
- **Domain**: `programming-languages`
- **Language / Representation**: **SystemVerilog** (`Hardware Description & Verification Language (HDVL)`)
- **Technical Relationship**: IEEE 1800-2017/2023 unified RTL design (`always_ff`, `always_comb`, `logic`) and formal/constrained-random verification (`SVA`, `UVM`) superset of Verilog.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **SystemVerilog**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: IEEE Std 1800-2017 / IEEE Std 1800-2023 (SystemVerilog) (SystemVerilog-2012 / 2017 / 2023)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`SystemVerilog `package` namespaces (`import pkg::*;`), Filelists (`.f`), FuseSoC.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **SystemVerilog** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **SystemVerilog**.

### Technical Triggers

- Files, build manifests, or prompts targeting **SystemVerilog** (`sync_fifo_sva.sv`, `SystemVerilog `package` namespaces (`import pkg::*;`), Filelists (`.f`), FuseSoC.`).

### Prerequisites

- Target language version (SystemVerilog-2012 / 2017 / 2023), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **SystemVerilog** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (SystemVerilog-2012 / 2017 / 2023), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Synthesizable packed arrays/FIFOs in RTL; dynamic queues (`q[$]`) and associative arrays in UVM testbenches.), type soundness limits (`typedef enum logic [1:0]`, `typedef struct packed`, multidimensional packed/unpacked arrays, and `interface` with `modport` directional contracts.), and concurrency hazards (RTL concurrent processes + SVA concurrent assertions (`assert property (@(posedge clk) disable iff (!rst_n) req |-> ##[1:3] ack)`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce IEEE Std 1800-2017 / IEEE Std 1800-2023 (SystemVerilog).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Use `logic` instead of `reg`, explicit synthesis intent blocks (`always_ff @(posedge clk)`, `always_comb`, `always_latch`), and `unique case`.
2. **Type System & Inference**: `typedef enum logic [1:0]`, `typedef struct packed`, multidimensional packed/unpacked arrays, and `interface` with `modport` directional contracts.
3. **Memory Management**: Synthesizable packed arrays/FIFOs in RTL; dynamic queues (`q[$]`) and associative arrays in UVM testbenches.
4. **Concurrency & Async Programming**: RTL concurrent processes + SVA concurrent assertions (`assert property (@(posedge clk) disable iff (!rst_n) req |-> ##[1:3] ack)`).
5. **Standard Library & Ecosystem**: Verilator, Synopsys VCS, Cadence Xcelium, Questa, SymbiYosys (formal SVA), Cocotb, UVM.
6. **Build Systems & Package Management**: SystemVerilog `package` namespaces (`import pkg::*;`), Filelists (`.f`), FuseSoC.
7. **Compiler / Interpreter Behavior**: `always_comb` automatically checks sensitivity completeness and errors at compile time if any variable is also driven by another process or infers a latch.
8. **Debugging & Observability**: SVA `cover property` / `assert property` formal counterexample traces (SymbiYosys) and waveform assertion markers.
9. **Security Hardening**: Formal SVA proofs of hardware lock bits, bus privilege isolation, and FSM reachability (`$onehot(state)`).
10. **Performance Optimization**: Zero-bubble pipelined `valid`/`ready` stages and packed struct single-vector bus routing.
11. **Error Handling Discipline**: Parity/ECC syndromes (`^data`) and protocol violation SVA traps (`$error`, `$fatal`).
12. **Testing Methodologies**: Formal verification (`assume property`, `assert property`, `cover property`) + Cocotb/UVM scoreboard verification.
13. **Interoperability & Cross-Platform ABI**: Direct Programming Interface (`import "DPI-C" function ...`) for C/C++ golden reference co-simulation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/systemverilog-rtl-sva-verification/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (SystemVerilog-2012 / 2017 / 2023), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in SystemVerilog**: Using legacy `always @(*)` instead of `always_comb`, `full_case`/`parallel_case` synthesis pragmas (causes pre/post-synthesis simulation mismatch; use `unique case`), and unpacked structs in synthesizable ports.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
