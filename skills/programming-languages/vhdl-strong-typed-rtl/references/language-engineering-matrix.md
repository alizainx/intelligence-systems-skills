# Deep Engineering Reference: VHDL (IEEE 1076-2008) numeric_std, Safe FSMs, Generics & Synchronous RTL (`vhdl-strong-typed-rtl`)

- **Language / Representation**: **VHDL**
- **Taxonomic Classification**: `Hardware Description Language (HDL)`
- **Technical Relationship**: Strongly typed IEEE 1076-2008/2019 hardware description language widely required in defense, aerospace (DO-254), and European ASIC/FPGA flows.
- **Governing Standards & Versions**: IEEE Std 1076-2008 / IEEE Std 1076-2019 (VHDL), DO-254 (VHDL-93 / VHDL-2008 / VHDL-2019)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **VHDL** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `entity` interface vs `architecture` implementation, `process(all)` (VHDL-2008 combinational sensitivity), and `rising_edge(clk)` synchronous clocking. |
| 2 | **Type System & Inference** | Strict nominal typing: `std_logic`, `std_logic_vector` (bag of bits), `unsigned` and `signed` from `ieee.numeric_std`, `natural`/`positive` integer ranges, and enumerated FSM states. |
| 3 | **Memory Management** | Signal drivers (delta-cycle scheduled updates `<=`) vs process-local immediate `variable` (`:=`) assignments. |
| 4 | **Concurrency & Async Programming** | Concurrent signal assignments, `process` blocks, and `generate` (`for ... generate`, `if ... generate`) hardware replication. |
| 5 | **Standard Library & Ecosystem** | GHDL (`ghdl -a --std=08`), VUnit, OSVVM (Open Source VHDL Verification Methodology), Vivado/Quartus. |
| 6 | **Build Systems & Package Management** | `ghdl -a --std=08 -Werror`, VUnit `run.py`. |
| 7 | **Compiler / Interpreter Behavior** | Delta-cycle simulation semantics: signal assignments `<=` take effect on the next delta cycle, preventing order-dependent race conditions between processes. |
| 8 | **Debugging** | GHDL waveform export (`--wave=sim.ghw`) with GTKWave and VHDL `assert ... report ... severity failure;`. |
| 9 | **Security** | Never import non-standard Synopsys `std_logic_arith` or `std_logic_unsigned` (ambiguous signed/unsigned overloading); always use standard `ieee.numeric_std`! |
| 10 | **Performance Optimization** | Use integer ranges (`natural range 0 to MAX_COUNT - 1`) for counters to avoid 32-bit full-width adder inference. |
| 11 | **Error Handling** | `when others =>` recovery state in every FSM `case` statement and compile-time `assert` checks on `generic` parameters. |
| 12 | **Testing Methodologies** | Self-checking VHDL-2008 testbenches using `std.env.stop` / `assert`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (VHDL-93 / VHDL-2008 / VHDL-2019); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | VHPIDIRECT C bindings in GHDL and mixed-language VHDL/SystemVerilog hierarchy instantiation. |
| 18 | **Common Engineering Mistakes** | Using `std_logic_unsigned`/`std_logic_arith` instead of `ieee.numeric_std`, using `clk'event and clk = '1'` instead of `rising_edge(clk)`, and incomplete sensitivity lists in pre-2008 combinational processes. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/vhdl-strong-typed-rtl/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **VHDL**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GHDL waveform export (`--wave=sim.ghw`) with GTKWave and VHDL `assert ... report ... severity failure;`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``ghdl -a --std=08 -Werror`, VUnit `run.py`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use integer ranges (`natural range 0 to MAX_COUNT - 1`) for counters to avoid 32-bit full-width adder inference.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Never import non-standard Synopsys `std_logic_arith` or `std_logic_unsigned` (ambiguous signed/unsigned overloading); always use standard `ieee.numeric_std`!).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Self-checking VHDL-2008 testbenches using `std.env.stop` / `assert`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (VHPIDIRECT C bindings in GHDL and mixed-language VHDL/SystemVerilog hierarchy instantiation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
