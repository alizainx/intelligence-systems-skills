---
name: ruby-vm-metaprogramming
description: Develop, refactor, profile, and verify production Ruby 3.2/3.3+ applications using frozen_string_literal, Data.define immutable value objects, Sorbet/RBS static typing, Fiber Scheduler/Ractor concurrency, and YJIT optimization.
allowed-tools: execute_bash view_file write_to_file
---

# Ruby (3.2/3.3+ YJIT) Frozen String Literals, RBS/Sorbet Types, Ractors & Metaprogramming Safety

Develop, refactor, profile, and verify production Ruby 3.2/3.3+ applications using frozen_string_literal, Data.define immutable value objects, Sorbet/RBS static typing, Fiber Scheduler/Ractor concurrency, and YJIT optimization.

## A. Identity

- **Skill Name**: `ruby-vm-metaprogramming`
- **Domain**: `programming-languages`
- **Language / Representation**: **Ruby** (`General-Purpose Programming Language`)
- **Technical Relationship**: Dynamic object-oriented language running on CRuby (YARV bytecode VM + YJIT) with RBS/Sorbet static type checking and Ractor concurrency.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Ruby**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 30170 Ruby Language Specification, Ruby 3.3 YARV/YJIT Reference (Ruby 3.2 / Ruby 3.3+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``Gemfile` + `Gemfile.lock` (`bundle config set --local deployment true`), `bundle audit`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Ruby** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Ruby**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Ruby** (`immutable_ledger_entry.rb`, ``Gemfile` + `Gemfile.lock` (`bundle config set --local deployment true`), `bundle audit`.`).

### Prerequisites

- Target language version (Ruby 3.2 / Ruby 3.3+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Ruby** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Ruby 3.2 / Ruby 3.3+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (CRuby Variable Width Allocation (VWA) heap pages and generational incremental GC; avoid retaining large strings/objects in class variables (`@@var`).), type soundness limits (Gradual static typing via RBS type signatures (`sig/*.rbs` + Steep) or Sorbet (`# typed: strict`, `T::Struct`).), and concurrency hazards (GVL (Global VM Lock) in standard threads; `Fiber.set_scheduler` for non-blocking I/O, and share-nothing `Ractor` actors for true multi-core parallelism.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 30170 Ruby Language Specification, Ruby 3.3 YARV/YJIT Reference.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Mandatory `# frozen_string_literal: true` magic comment, `Data.define` immutable value structs (Ruby 3.2+), rightward/pattern matching (`case/in`).
2. **Type System & Inference**: Gradual static typing via RBS type signatures (`sig/*.rbs` + Steep) or Sorbet (`# typed: strict`, `T::Struct`).
3. **Memory Management**: CRuby Variable Width Allocation (VWA) heap pages and generational incremental GC; avoid retaining large strings/objects in class variables (`@@var`).
4. **Concurrency & Async Programming**: GVL (Global VM Lock) in standard threads; `Fiber.set_scheduler` for non-blocking I/O, and share-nothing `Ractor` actors for true multi-core parallelism.
5. **Standard Library & Ecosystem**: Bundler, RSpec, Minitest, RuboCop, Sidekiq, Rack, Zeitwerk.
6. **Build Systems & Package Management**: `Gemfile` + `Gemfile.lock` (`bundle config set --local deployment true`), `bundle audit`.
7. **Compiler / Interpreter Behavior**: YARV bytecode + Rust-based **YJIT** (`RUBY_YJIT_ENABLE=1`) basic-block versioning compiler; maintain consistent object shapes (initialize all `@ivars` in `initialize`).
8. **Debugging & Observability**: `debug` gem (`rdbg`), `ObjectSpace.dump_all`, `stackprof`, and `Vernier` profiler.
9. **Security Hardening**: Never call `Kernel#open` on user strings (command injection if leading `|`; use `File.open`), ban `Marshal.load`/`YAML.unsafe_load` on untrusted data, and prefer `public_send` over `send`.
10. **Performance Optimization**: Avoid `define_method` or singleton class mutations at runtime (invalidates YJIT inline caches) and use `String#freeze`.
11. **Error Handling Discipline**: Rescue `StandardError` (never bare `rescue Exception`, which traps `SignalException` and `SystemExit`).
12. **Testing Methodologies**: RSpec / Minitest suites with `RUBYOPT="-w"` warning enforcement.
13. **Interoperability & Cross-Platform ABI**: C extensions (`Rice` / `rb_define_method`), `Fiddle` (`libffi`), and `magnus` (Rust FFI).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/ruby-vm-metaprogramming/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Ruby 3.2 / Ruby 3.3+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Ruby**: Rescuing `Exception`, mutating shared constants across threads/Ractors, and using `send(params[:action])` allowing private method invocation.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
