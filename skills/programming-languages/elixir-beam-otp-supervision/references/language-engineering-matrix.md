# Deep Engineering Reference: Elixir (1.16/1.17+ / OTP 26+) GenServer, Supervision Trees, Binary Pattern Matching & Telemetry (`elixir-beam-otp-supervision`)

- **Language / Representation**: **Elixir**
- **Taxonomic Classification**: `Functional Concurrent Programming Language (BEAM VM)`
- **Technical Relationship**: Functional, macro-extensible language compiling to BEAM bytecode with full Erlang/OTP supervision-tree interoperability.
- **Governing Standards & Versions**: Elixir 1.16 / 1.17 Documentation, Erlang/OTP 26/27 Design Principles (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Elixir** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Pattern matching (`=`), pin operator (`^`), `with` railway pipelines, hygienic AST macros (`quote`/`unquote`), and binary/bitstring destructuring (`<<version::4, flags::4, payload::binary>>`). |
| 2 | **Type System & Inference** | Dynamic runtime types with `@spec`/`@type` Dialyzer success typing and Elixir 1.17+ gradual set-theoretic type system checks. |
| 3 | **Memory Management** | Per-process isolated BEAM heaps (zero global stop-the-world GC) + shared reference-counted binary heap for binaries > 64 bytes (`:recon_alloc` sub-binary leak awareness). |
| 4 | **Concurrency & Async Programming** | Preemptive reduction-counted BEAM processes (~2.6 KB initial footprint), `Task.Supervisor.async_nolink`, and OTP Supervision strategies (`:one_for_one`, `:rest_for_one`). |
| 5 | **Standard Library & Ecosystem** | Mix, Hex, Ecto, Phoenix, Broadway, Telemetry, Credo, Dialyxir, ExUnit. |
| 6 | **Build Systems & Package Management** | `mix.exs` + `mix.lock`, `mix compile --warnings-as-errors`, `mix release` self-contained OTP releases. |
| 7 | **Compiler / Interpreter Behavior** | Elixir macro expansion -> Erlang Abstract Format -> BEAM SSA -> JIT native code (`+JMsingle true`). |
| 8 | **Debugging** | `:observer`, `:recon` (`:recon.proc_count(:memory, 10)`), `IEx.pry`, and `:telemetry` spans. |
| 9 | **Security** | Never call `String.to_atom/1` on untrusted user input (BEAM atom table is not garbage-collected; use `String.to_existing_atom/1`), and ban `:erlang.binary_to_term(bin)` without `[:safe]`. |
| 10 | **Performance Optimization** | Use `ETS` (`:ets`) for concurrent read-heavy state, `IOData` lists (`[head | tail]`) instead of string concatenation `<>` for socket/file writes, and `handle_continue/2` for non-blocking `GenServer.init/1`. |
| 11 | **Error Handling** | "Let it crash" for unexpected transient state corruption under a bounded `Supervisor` (`max_restarts`, `max_seconds`), and `{:ok, val} | {:error, reason}` tuples for domain errors. |
| 12 | **Testing Methodologies** | `ExUnit` (`async: true`), `StreamData` property testing, and `Mox` behaviour-verified mocks. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Direct `:erlang_module.func()` invocation, Ports for external OS processes, and Rustler (safe Rust NIFs yielding within 1ms reduction budgets). |
| 18 | **Common Engineering Mistakes** | Atom table exhaustion via `String.to_atom`, GenServer mailbox unbounded queue growth without backpressure, and retaining small slices of huge >64B refc binaries (fix with `:binary.copy/1`). |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/elixir-beam-otp-supervision/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Elixir**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``:observer`, `:recon` (`:recon.proc_count(:memory, 10)`), `IEx.pry`, and `:telemetry` spans.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``mix.exs` + `mix.lock`, `mix compile --warnings-as-errors`, `mix release` self-contained OTP releases.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `ETS` (`:ets`) for concurrent read-heavy state, `IOData` lists (`[head | tail]`) instead of string concatenation `<>` for socket/file writes, and `handle_continue/2` for non-blocking `GenServer.init/1`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Never call `String.to_atom/1` on untrusted user input (BEAM atom table is not garbage-collected; use `String.to_existing_atom/1`), and ban `:erlang.binary_to_term(bin)` without `[:safe]`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`ExUnit` (`async: true`), `StreamData` property testing, and `Mox` behaviour-verified mocks.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Direct `:erlang_module.func()` invocation, Ports for external OS processes, and Rustler (safe Rust NIFs yielding within 1ms reduction budgets).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
