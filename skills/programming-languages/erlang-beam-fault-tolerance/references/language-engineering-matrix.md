# Deep Engineering Reference: Erlang/OTP (OTP 26/27) gen_statem, gen_server, Supervision Trees & Hot Code Loading (`erlang-beam-fault-tolerance`)

- **Language / Representation**: **Erlang**
- **Taxonomic Classification**: `Functional Concurrent Programming Language (BEAM / OTP)`
- **Technical Relationship**: Foundational telecom-grade actor language of the BEAM virtual machine and Open Telecom Platform (OTP).
- **Governing Standards & Versions**: Erlang/OTP 26 / 27 System Documentation, ERTS User's Guide (Erlang/OTP 25 / 26 / 27)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Erlang** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Single-assignment variables, pattern matching in function heads and `case`/`receive` clauses, guard expressions (`when is_integer(N), N > 0`), and `.hrl` records/maps. |
| 2 | **Type System & Inference** | `-spec` and `-type`/`-opaque` annotations verified statically by `dialyzer` and `eqWAlizer` / `gradualizer`. |
| 3 | **Memory Management** | Isolated process heaps, off-heap message queues (`-hmqd off_heap` for high-traffic actors), and `persistent_term` for zero-copy read-mostly configuration. |
| 4 | **Concurrency & Async Programming** | Share-nothing actors communicating via asynchronous messages (`Pid ! Msg`), monitors (`erlang:monitor/2`), links (`link/1`), and selective receive optimization. |
| 5 | **Standard Library & Ecosystem** | `rebar3`, `stdlib`, `kernel`, `sasl`, `mnesia`, `cowboy`, `recon`, `PropEr`, `Common Test`. |
| 6 | **Build Systems & Package Management** | `rebar.config` + `rebar.lock`, `rebar3 compile`, `rebar3 dialyzer`, `rebar3 tar` releases. |
| 7 | **Compiler / Interpreter Behavior** | `erlc +warnings_as_errors +warn_export_all` compiling via SSA IR to BEAM instructions executed by BeamAsm native JIT. |
| 8 | **Debugging** | `dbg` trace BIFs (always with rate-limited match specs via `recon_trace` in production!), `observer_cli`, and crashdump viewer. |
| 9 | **Security** | Use `binary_to_term(Bin, [safe])`, avoid `os:cmd/1` with unsanitized strings, and configure distributed Erlang TLS cookies. |
| 10 | **Performance Optimization** | Avoid O(N) selective `receive` scans on deep mailboxes (use monitor refs configured via `alias`), use `iolist` for network output, and avoid copying large terms across processes. |
| 11 | **Error Handling** | Separate error kernel processes (must-not-fail state owners) from worker processes supervised under bounded intensity (`#{intensity => 3, period => 10}`). |
| 12 | **Testing Methodologies** | EUnit (`rebar3 eunit`), Common Test (`rebar3 ct`), and `PropEr` stateful state-machine property tests. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Erlang/OTP 25 / 26 / 27); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | NIFs (Native Implemented Functions in C/Rust using dirty schedulers or `enif_consume_timeslice`), Ports, and C-nodes. |
| 18 | **Common Engineering Mistakes** | Unbounded `receive` without `after` timeout in synchronous calls, `-compile(export_all).`, and calling `length(List)` ($O(N)$) inside guards instead of pattern matching `[_, _ | _]`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/erlang-beam-fault-tolerance/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Erlang**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``dbg` trace BIFs (always with rate-limited match specs via `recon_trace` in production!), `observer_cli`, and crashdump viewer.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``rebar.config` + `rebar.lock`, `rebar3 compile`, `rebar3 dialyzer`, `rebar3 tar` releases.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Avoid O(N) selective `receive` scans on deep mailboxes (use monitor refs configured via `alias`), use `iolist` for network output, and avoid copying large terms across processes.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Use `binary_to_term(Bin, [safe])`, avoid `os:cmd/1` with unsanitized strings, and configure distributed Erlang TLS cookies.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (EUnit (`rebar3 eunit`), Common Test (`rebar3 ct`), and `PropEr` stateful state-machine property tests.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (NIFs (Native Implemented Functions in C/Rust using dirty schedulers or `enif_consume_timeslice`), Ports, and C-nodes.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
