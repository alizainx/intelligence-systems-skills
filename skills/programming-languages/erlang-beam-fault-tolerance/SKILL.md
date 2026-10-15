---
name: erlang-beam-fault-tolerance
description: Architect, implement, and verify ultra-reliable Erlang/OTP systems using gen_server, gen_statem state machines, supervisor restart intensity bounds, ETS/Mnesia, binary pattern matching, and Dialyzer.
allowed-tools: execute_bash view_file write_to_file
---

# Erlang/OTP (OTP 26/27) gen_statem, gen_server, Supervision Trees & Hot Code Loading

Architect, implement, and verify ultra-reliable Erlang/OTP systems using gen_server, gen_statem state machines, supervisor restart intensity bounds, ETS/Mnesia, binary pattern matching, and Dialyzer.

## A. Identity

- **Skill Name**: `erlang-beam-fault-tolerance`
- **Domain**: `programming-languages`
- **Language / Representation**: **Erlang** (`Functional Concurrent Programming Language (BEAM / OTP)`)
- **Technical Relationship**: Foundational telecom-grade actor language of the BEAM virtual machine and Open Telecom Platform (OTP).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Erlang**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Erlang/OTP 26 / 27 System Documentation, ERTS User's Guide (Erlang/OTP 25 / 26 / 27)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``rebar.config` + `rebar.lock`, `rebar3 compile`, `rebar3 dialyzer`, `rebar3 tar` releases.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Erlang** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Erlang**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Erlang** (`circuit_breaker_statem.erl`, ``rebar.config` + `rebar.lock`, `rebar3 compile`, `rebar3 dialyzer`, `rebar3 tar` releases.`).

### Prerequisites

- Target language version (Erlang/OTP 25 / 26 / 27), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Erlang** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Erlang/OTP 25 / 26 / 27), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Isolated process heaps, off-heap message queues (`-hmqd off_heap` for high-traffic actors), and `persistent_term` for zero-copy read-mostly configuration.), type soundness limits (`-spec` and `-type`/`-opaque` annotations verified statically by `dialyzer` and `eqWAlizer` / `gradualizer`.), and concurrency hazards (Share-nothing actors communicating via asynchronous messages (`Pid ! Msg`), monitors (`erlang:monitor/2`), links (`link/1`), and selective receive optimization.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Erlang/OTP 26 / 27 System Documentation, ERTS User's Guide.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Single-assignment variables, pattern matching in function heads and `case`/`receive` clauses, guard expressions (`when is_integer(N), N > 0`), and `.hrl` records/maps.
2. **Type System & Inference**: `-spec` and `-type`/`-opaque` annotations verified statically by `dialyzer` and `eqWAlizer` / `gradualizer`.
3. **Memory Management**: Isolated process heaps, off-heap message queues (`-hmqd off_heap` for high-traffic actors), and `persistent_term` for zero-copy read-mostly configuration.
4. **Concurrency & Async Programming**: Share-nothing actors communicating via asynchronous messages (`Pid ! Msg`), monitors (`erlang:monitor/2`), links (`link/1`), and selective receive optimization.
5. **Standard Library & Ecosystem**: `rebar3`, `stdlib`, `kernel`, `sasl`, `mnesia`, `cowboy`, `recon`, `PropEr`, `Common Test`.
6. **Build Systems & Package Management**: `rebar.config` + `rebar.lock`, `rebar3 compile`, `rebar3 dialyzer`, `rebar3 tar` releases.
7. **Compiler / Interpreter Behavior**: `erlc +warnings_as_errors +warn_export_all` compiling via SSA IR to BEAM instructions executed by BeamAsm native JIT.
8. **Debugging & Observability**: `dbg` trace BIFs (always with rate-limited match specs via `recon_trace` in production!), `observer_cli`, and crashdump viewer.
9. **Security Hardening**: Use `binary_to_term(Bin, [safe])`, avoid `os:cmd/1` with unsanitized strings, and configure distributed Erlang TLS cookies.
10. **Performance Optimization**: Avoid O(N) selective `receive` scans on deep mailboxes (use monitor refs configured via `alias`), use `iolist` for network output, and avoid copying large terms across processes.
11. **Error Handling Discipline**: Separate error kernel processes (must-not-fail state owners) from worker processes supervised under bounded intensity (`#{intensity => 3, period => 10}`).
12. **Testing Methodologies**: EUnit (`rebar3 eunit`), Common Test (`rebar3 ct`), and `PropEr` stateful state-machine property tests.
13. **Interoperability & Cross-Platform ABI**: NIFs (Native Implemented Functions in C/Rust using dirty schedulers or `enif_consume_timeslice`), Ports, and C-nodes.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/erlang-beam-fault-tolerance/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Erlang/OTP 25 / 26 / 27), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Erlang**: Unbounded `receive` without `after` timeout in synchronous calls, `-compile(export_all).`, and calling `length(List)` ($O(N)$) inside guards instead of pattern matching `[_, _ | _]`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
