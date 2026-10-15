# Deep Engineering Reference: Verilog (IEEE 1364-2005) Synthesizable RTL, Non-Blocking Assignments, FSMs & CDC (`verilog-ieee1364-rtl`)

- **Language / Representation**: **Verilog**
- **Taxonomic Classification**: `Hardware Description Language (HDL)`
- **Technical Relationship**: IEEE 1364-2005 RTL hardware description language synthesized into FPGA/ASIC digital logic gates and flip-flops (not a sequential software programming language).
- **Governing Standards & Versions**: IEEE Std 1364-2005 (Verilog HDL), Clifford Cummings Nonblocking & CDC Guidelines (Verilog-2001 / IEEE 1364-2005)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Verilog** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `default_nettype none` at top of every file (prevents 1-bit implicit wire typos!), ANSI port declarations, and parameterized `generate` blocks. |
| 2 | **Type System & Inference** | 4-state logic (`0`, `1`, `X`, `Z`), explicit bit widths (`[WIDTH-1:0]`), `wire` nets vs `reg` variables, and `signed` arithmetic rules. |
| 3 | **Memory Management** | Hardware storage elements: synchronous D-flip-flop registers (`reg`), inferred Block RAM (BRAM) arrays, and distributed LUT RAM. |
| 4 | **Concurrency & Async Programming** | All `always` blocks and continuous `assign` statements execute concurrently in hardware; use non-blocking `<=` in clocked `always @(posedge clk)` and blocking `=` in combinational `always @(*)`. |
| 5 | **Standard Library & Ecosystem** | Icarus Verilog (`iverilog`), Verilator (`verilator --lint-only -Wall`), Yosys synthesis, GTKWave. |
| 6 | **Build Systems & Package Management** | Fusesoc / Makefile driving `verilator --lint-only -Wall` and `iverilog -g2005`. |
| 7 | **Compiler / Interpreter Behavior** | RTL synthesis infers unintended transparent latches if any combinational `always @(*)` path omits an output assignment; avoid `X`-optimism in `case` statements. |
| 8 | **Debugging** | VCD/FST waveform dumps (`$dumpfile`, `$dumpvars`), Verilator lint diagnostics (`WIDTH`, `UNOPTFLAT`, `LATCH`). |
| 9 | **Security** | Ensure FSMs have a safe `default:` state recovery transition to prevent fault-injection lockup in undefined encodings. |
| 10 | **Performance Optimization** | Pipeline deep combinational paths with register stages to meet setup/hold static timing closure ($f_{\max}$). |
| 11 | **Error Handling** | Valid/ready AXI-Stream handshake backpressure (`tvalid && tready`) without combinational loops between `ready` and `valid`. |
| 12 | **Testing Methodologies** | Self-checking testbenches checking reset state, full/empty FIFO boundaries, and multi-cycle protocol handshakes. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Verilog-2001 / IEEE 1364-2005); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Verilog Procedural Interface (VPI) and Verilator C++ cycle-accurate simulation wrappers. |
| 18 | **Common Engineering Mistakes** | Mixing `=` and `<=` on the same signal, omitting `default_nettype none`, inferring latches in incomplete `if`/`case` blocks, and crossing clock domains with multi-bit binary counters instead of Gray code. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/verilog-ieee1364-rtl/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Verilog**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `VCD/FST waveform dumps (`$dumpfile`, `$dumpvars`), Verilator lint diagnostics (`WIDTH`, `UNOPTFLAT`, `LATCH`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Fusesoc / Makefile driving `verilator --lint-only -Wall` and `iverilog -g2005`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Pipeline deep combinational paths with register stages to meet setup/hold static timing closure ($f_{\max}$).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Ensure FSMs have a safe `default:` state recovery transition to prevent fault-injection lockup in undefined encodings.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Self-checking testbenches checking reset state, full/empty FIFO boundaries, and multi-cycle protocol handshakes.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Verilog Procedural Interface (VPI) and Verilator C++ cycle-accurate simulation wrappers.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
