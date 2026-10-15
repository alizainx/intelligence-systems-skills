---
name: elixir-beam-otp-supervision
description: Design, build, debug, and verify fault-tolerant Elixir/OTP systems using immutable data, bitstring/binary protocol pattern matching, GenServer/Supervisor/DynamicSupervisor lifecycle design, GenStage/Broadway backpressure, and ExUnit.
allowed-tools: execute_bash view_file write_to_file
---

# Elixir (1.16/1.17+ / OTP 26+) GenServer, Supervision Trees, Binary Pattern Matching & Telemetry

Design, build, debug, and verify fault-tolerant Elixir/OTP systems using immutable data, bitstring/binary protocol pattern matching, GenServer/Supervisor/DynamicSupervisor lifecycle design, GenStage/Broadway backpressure, and ExUnit.

## A. Identity

- **Skill Name**: `elixir-beam-otp-supervision`
- **Domain**: `programming-languages`
- **Language / Representation**: **Elixir** (`Functional Concurrent Programming Language (BEAM VM)`)
- **Technical Relationship**: Functional, macro-extensible language compiling to BEAM bytecode with full Erlang/OTP supervision-tree interoperability.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Elixir**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Elixir 1.16 / 1.17 Documentation, Erlang/OTP 26/27 Design Principles (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``mix.exs` + `mix.lock`, `mix compile --warnings-as-errors`, `mix release` self-contained OTP releases.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Elixir** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Elixir**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Elixir** (`protocol_frame_parser.ex`, ``mix.exs` + `mix.lock`, `mix compile --warnings-as-errors`, `mix release` self-contained OTP releases.`).

### Prerequisites

- Target language version (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Elixir** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Per-process isolated BEAM heaps (zero global stop-the-world GC) + shared reference-counted binary heap for binaries > 64 bytes (`:recon_alloc` sub-binary leak awareness).), type soundness limits (Dynamic runtime types with `@spec`/`@type` Dialyzer success typing and Elixir 1.17+ gradual set-theoretic type system checks.), and concurrency hazards (Preemptive reduction-counted BEAM processes (~2.6 KB initial footprint), `Task.Supervisor.async_nolink`, and OTP Supervision strategies (`:one_for_one`, `:rest_for_one`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Elixir 1.16 / 1.17 Documentation, Erlang/OTP 26/27 Design Principles.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Pattern matching (`=`), pin operator (`^`), `with` railway pipelines, hygienic AST macros (`quote`/`unquote`), and binary/bitstring destructuring (`<<version::4, flags::4, payload::binary>>`).
2. **Type System & Inference**: Dynamic runtime types with `@spec`/`@type` Dialyzer success typing and Elixir 1.17+ gradual set-theoretic type system checks.
3. **Memory Management**: Per-process isolated BEAM heaps (zero global stop-the-world GC) + shared reference-counted binary heap for binaries > 64 bytes (`:recon_alloc` sub-binary leak awareness).
4. **Concurrency & Async Programming**: Preemptive reduction-counted BEAM processes (~2.6 KB initial footprint), `Task.Supervisor.async_nolink`, and OTP Supervision strategies (`:one_for_one`, `:rest_for_one`).
5. **Standard Library & Ecosystem**: Mix, Hex, Ecto, Phoenix, Broadway, Telemetry, Credo, Dialyxir, ExUnit.
6. **Build Systems & Package Management**: `mix.exs` + `mix.lock`, `mix compile --warnings-as-errors`, `mix release` self-contained OTP releases.
7. **Compiler / Interpreter Behavior**: Elixir macro expansion -> Erlang Abstract Format -> BEAM SSA -> JIT native code (`+JMsingle true`).
8. **Debugging & Observability**: `:observer`, `:recon` (`:recon.proc_count(:memory, 10)`), `IEx.pry`, and `:telemetry` spans.
9. **Security Hardening**: Never call `String.to_atom/1` on untrusted user input (BEAM atom table is not garbage-collected; use `String.to_existing_atom/1`), and ban `:erlang.binary_to_term(bin)` without `[:safe]`.
10. **Performance Optimization**: Use `ETS` (`:ets`) for concurrent read-heavy state, `IOData` lists (`[head | tail]`) instead of string concatenation `<>` for socket/file writes, and `handle_continue/2` for non-blocking `GenServer.init/1`.
11. **Error Handling Discipline**: "Let it crash" for unexpected transient state corruption under a bounded `Supervisor` (`max_restarts`, `max_seconds`), and `{:ok, val} | {:error, reason}` tuples for domain errors.
12. **Testing Methodologies**: `ExUnit` (`async: true`), `StreamData` property testing, and `Mox` behaviour-verified mocks.
13. **Interoperability & Cross-Platform ABI**: Direct `:erlang_module.func()` invocation, Ports for external OS processes, and Rustler (safe Rust NIFs yielding within 1ms reduction budgets).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/elixir-beam-otp-supervision/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Elixir 1.15 / 1.16 / 1.17+ (OTP 26+)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Elixir**: Atom table exhaustion via `String.to_atom`, GenServer mailbox unbounded queue growth without backpressure, and retaining small slices of huge >64B refc binaries (fix with `:binary.copy/1`).
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
