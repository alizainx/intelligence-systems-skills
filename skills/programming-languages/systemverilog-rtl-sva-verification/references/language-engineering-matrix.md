# Deep Engineering Reference: SystemVerilog (IEEE 1800-2017/2023) always_ff/always_comb, Packed Structs, Interfaces & SVA (`systemverilog-rtl-sva-verification`)

- **Language / Representation**: **SystemVerilog**
- **Taxonomic Classification**: `Hardware Description & Verification Language (HDVL)`
- **Technical Relationship**: IEEE 1800-2017/2023 unified RTL design (`always_ff`, `always_comb`, `logic`) and formal/constrained-random verification (`SVA`, `UVM`) superset of Verilog.
- **Governing Standards & Versions**: IEEE Std 1800-2017 / IEEE Std 1800-2023 (SystemVerilog) (SystemVerilog-2012 / 2017 / 2023)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **SystemVerilog** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Use `logic` instead of `reg`, explicit synthesis intent blocks (`always_ff @(posedge clk)`, `always_comb`, `always_latch`), and `unique case`. |
| 2 | **Type System & Inference** | `typedef enum logic [1:0]`, `typedef struct packed`, multidimensional packed/unpacked arrays, and `interface` with `modport` directional contracts. |
| 3 | **Memory Management** | Synthesizable packed arrays/FIFOs in RTL; dynamic queues (`q[$]`) and associative arrays in UVM testbenches. |
| 4 | **Concurrency & Async Programming** | RTL concurrent processes + SVA concurrent assertions (`assert property (@(posedge clk) disable iff (!rst_n) req |-> ##[1:3] ack)`). |
| 5 | **Standard Library & Ecosystem** | Verilator, Synopsys VCS, Cadence Xcelium, Questa, SymbiYosys (formal SVA), Cocotb, UVM. |
| 6 | **Build Systems & Package Management** | SystemVerilog `package` namespaces (`import pkg::*;`), Filelists (`.f`), FuseSoC. |
| 7 | **Compiler / Interpreter Behavior** | `always_comb` automatically checks sensitivity completeness and errors at compile time if any variable is also driven by another process or infers a latch. |
| 8 | **Debugging** | SVA `cover property` / `assert property` formal counterexample traces (SymbiYosys) and waveform assertion markers. |
| 9 | **Security** | Formal SVA proofs of hardware lock bits, bus privilege isolation, and FSM reachability (`$onehot(state)`). |
| 10 | **Performance Optimization** | Zero-bubble pipelined `valid`/`ready` stages and packed struct single-vector bus routing. |
| 11 | **Error Handling** | Parity/ECC syndromes (`^data`) and protocol violation SVA traps (`$error`, `$fatal`). |
| 12 | **Testing Methodologies** | Formal verification (`assume property`, `assert property`, `cover property`) + Cocotb/UVM scoreboard verification. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (SystemVerilog-2012 / 2017 / 2023); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Direct Programming Interface (`import "DPI-C" function ...`) for C/C++ golden reference co-simulation. |
| 18 | **Common Engineering Mistakes** | Using legacy `always @(*)` instead of `always_comb`, `full_case`/`parallel_case` synthesis pragmas (causes pre/post-synthesis simulation mismatch; use `unique case`), and unpacked structs in synthesizable ports. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/systemverilog-rtl-sva-verification/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **SystemVerilog**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `SVA `cover property` / `assert property` formal counterexample traces (SymbiYosys) and waveform assertion markers.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `SystemVerilog `package` namespaces (`import pkg::*;`), Filelists (`.f`), FuseSoC.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Zero-bubble pipelined `valid`/`ready` stages and packed struct single-vector bus routing.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Formal SVA proofs of hardware lock bits, bus privilege isolation, and FSM reachability (`$onehot(state)`).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Formal verification (`assume property`, `assert property`, `cover property`) + Cocotb/UVM scoreboard verification.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Direct Programming Interface (`import "DPI-C" function ...`) for C/C++ golden reference co-simulation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
