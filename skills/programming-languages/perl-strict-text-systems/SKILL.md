---
name: perl-strict-text-systems
description: Write, modernize, audit, and verify Perl 5 (v5.36+) systems and text-processing software using use v5.36, strict/warnings, subroutine signatures, 3-argument open, list-form IPC system/open, and native Perl execution.
allowed-tools: execute_bash view_file write_to_file
---

# Modern Perl 5 (v5.36+) Strict/Warnings, Lexical Sub Signatures, Taint Mode & IPC Safety

Write, modernize, audit, and verify Perl 5 (v5.36+) systems and text-processing software using use v5.36, strict/warnings, subroutine signatures, 3-argument open, list-form IPC system/open, and native Perl execution.

## A. Identity

- **Skill Name**: `perl-strict-text-systems`
- **Domain**: `programming-languages`
- **Language / Representation**: **Perl** (`General-Purpose & Systems Automation Language`)
- **Technical Relationship**: Rich text-processing and UNIX systems programming language (Perl 5.36+) natively installed on POSIX/Linux hosts.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Perl**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Perl 5.36 / 5.38 Documentation (perlfunc, perlsec, perlre) (Perl v5.32 / v5.36 / v5.38+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``cpanfile` + `cpanfile.snapshot`, `perl -c -Mstrict -Mwarnings` syntax check.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Perl** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Perl**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Perl** (`strict_log_aggregator.pl`, ``cpanfile` + `cpanfile.snapshot`, `perl -c -Mstrict -Mwarnings` syntax check.`).

### Prerequisites

- Target language version (Perl v5.32 / v5.36 / v5.38+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Perl** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Perl v5.32 / v5.36 / v5.38+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Deterministic reference counting; break circular object references via `Scalar::Util::weaken($self->{parent})`.), type soundness limits (Sigil context sensitivity (`$scalar`, `@array`, `%hash`), `builtin::blessed` / `$obj isa Class`, and Type::Tiny runtime checks.), and concurrency hazards (Prefer prefork worker processes (`Parallel::ForkManager`) or event loops (`Mojo::IOLoop`, `IO::Async`) over heavyweight interpreter threads (`ithreads`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Perl 5.36 / 5.38 Documentation (perlfunc, perlsec, perlre).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `use v5.36;` (enables `strict`, `warnings`, `signatures`, `isa`, and disables indirect object syntax), lexical filehandles (`open my $fh, '<:encoding(UTF-8)', $path`).
2. **Type System & Inference**: Sigil context sensitivity (`$scalar`, `@array`, `%hash`), `builtin::blessed` / `$obj isa Class`, and Type::Tiny runtime checks.
3. **Memory Management**: Deterministic reference counting; break circular object references via `Scalar::Util::weaken($self->{parent})`.
4. **Concurrency & Async Programming**: Prefer prefork worker processes (`Parallel::ForkManager`) or event loops (`Mojo::IOLoop`, `IO::Async`) over heavyweight interpreter threads (`ithreads`).
5. **Standard Library & Ecosystem**: CPAN, `cpanm`, `Carton` (`cpanfile.snapshot`), `Perl::Critic`, `Perl::Tidy`, `Test2::V0`.
6. **Build Systems & Package Management**: `cpanfile` + `cpanfile.snapshot`, `perl -c -Mstrict -Mwarnings` syntax check.
7. **Compiler / Interpreter Behavior**: Two-phase compile (`BEGIN` blocks) + opcode tree execution (`perl -MO=Concise,func`).
8. **Debugging & Observability**: `perl -d`, `Carp::confess` stack traces, and `Devel::NYTProf` line/subroutine profiler.
9. **Security Hardening**: Taint mode (`perl -T`), mandatory 3-argument `open(my $fh, '<', $file)` (preventing 2-arg pipe injection), and list-form `system($prog, @args)`.
10. **Performance Optimization**: Precompile regular expressions with `qr//`, avoid `$&`/`$`/`$'` match variables on older Perls, and pack binary records with `pack`/`unpack`.
11. **Error Handling Discipline**: `autodie` for lexical system call error checking and structured `try`/`catch` (`use feature 'try'` in 5.36+).
12. **Testing Methodologies**: Native `Test::More` / `Test2::V0` TAP suites executed via `prove` or `perl`.
13. **Interoperability & Cross-Platform ABI**: XS C extensions and `FFI::Platypus` (`libffi`) bindings.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/perl-strict-text-systems/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Perl v5.32 / v5.36 / v5.38+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Perl**: 2-argument `open(FH, $user_path)` RCE vulnerability, string `eval $expr` instead of block `eval { ... }`, and accidental list-context vs scalar-context bugs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
