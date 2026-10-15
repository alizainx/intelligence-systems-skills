---
name: bash-posix-shell-engineering
description: Write, audit, debug, and verify defensive GNU Bash 5.x and POSIX shell scripts using set -Eeuo pipefail, IFS hygiene, array command construction, trap EXIT/ERR atomic temp-file cleanup, and native bash verification.
allowed-tools: execute_bash view_file write_to_file
---

# GNU Bash (5.2+) & POSIX Shell Defensive Automation (set -euo pipefail, Quoting & Trap Cleanup)

Write, audit, debug, and verify defensive GNU Bash 5.x and POSIX shell scripts using set -Eeuo pipefail, IFS hygiene, array command construction, trap EXIT/ERR atomic temp-file cleanup, and native bash verification.

## A. Identity

- **Skill Name**: `bash-posix-shell-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **Bash** (`Shell & Systems Automation Language`)
- **Technical Relationship**: GNU Bourne-Again SHell (`bash 5.2+`) superset of the POSIX.1-2017 Shell Command Language natively installed on Linux systems.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Bash**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: IEEE Std 1003.1-2017 (POSIX Shell), GNU Bash 5.2 Reference Manual, Google Shell Style Guide (GNU Bash 4.4 / 5.1 / 5.2+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``bash -n script.sh` syntax validation, `shellcheck -s bash -o all`, `shfmt -i 2 -ci`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Bash** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Bash**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Bash** (`atomic_config_writer.sh`, ``bash -n script.sh` syntax validation, `shellcheck -s bash -o all`, `shfmt -i 2 -ci`.`).

### Prerequisites

- Target language version (GNU Bash 4.4 / 5.1 / 5.2+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Bash** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (GNU Bash 4.4 / 5.1 / 5.2+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Avoid subshell forks inside tight loops (`$(...)` forks a process; use `printf -v var` or parameter expansion `${var#prefix}`).), type soundness limits (String variables, indexed arrays (`declare -a cmd=()`), associative maps (`declare -A map=()`), integer attribute (`declare -i`), and `local -r` constants.), and concurrency hazards (Background jobs with explicit PID tracking (`wait "$pid"`), `flock` file-descriptor locks for single-instance mutual exclusion, and `xargs -0 -P`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce IEEE Std 1003.1-2017 (POSIX Shell), GNU Bash 5.2 Reference Manual, Google Shell Style Guide.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `set -Eeuo pipefail`, `shopt -s inherit_errexit`, `[[ ... ]]` conditional expressions (no word splitting), and `(( ... ))` integer arithmetic.
2. **Type System & Inference**: String variables, indexed arrays (`declare -a cmd=()`), associative maps (`declare -A map=()`), integer attribute (`declare -i`), and `local -r` constants.
3. **Memory Management**: Avoid subshell forks inside tight loops (`$(...)` forks a process; use `printf -v var` or parameter expansion `${var#prefix}`).
4. **Concurrency & Async Programming**: Background jobs with explicit PID tracking (`wait "$pid"`), `flock` file-descriptor locks for single-instance mutual exclusion, and `xargs -0 -P`.
5. **Standard Library & Ecosystem**: GNU Coreutils, `find -print0`, `jq`, `shellcheck`, `shfmt`, `bats-core`.
6. **Build Systems & Package Management**: `bash -n script.sh` syntax validation, `shellcheck -s bash -o all`, `shfmt -i 2 -ci`.
7. **Compiler / Interpreter Behavior**: Line-by-line parsing & expansion order: brace -> tilde -> parameter/variable -> command substitution -> arithmetic -> word splitting -> pathname globbing.
8. **Debugging & Observability**: `PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]:+${FUNCNAME[0]}(): }'` with `set -x` and `trap` stack trace helpers.
9. **Security Hardening**: Quote every expansion (`"$var"`, `"${arr[@]}"`), pass `--` before positional paths (`rm -f -- "$file"`) to block leading-dash flag injection, and never use `eval`.
10. **Performance Optimization**: Use `read -r` line loops with process substitution `< <(...)` (preserving parent shell variables unlike `cmd | while read`).
11. **Error Handling Discipline**: Note that `local var=$(failing_cmd)` masks the exit code of `failing_cmd` because `local` itself succeeds! Separate `local var; var=$(failing_cmd)`.
12. **Testing Methodologies**: Native `bash` self-test execution and `bats-core` TAP suites.
13. **Interoperability & Cross-Platform ABI**: Environment variable sanitization (`env -i PATH=/usr/bin:/bin`), exit codes (`0`..`255`), and NUL-delimited streams (`\0`).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/bash-posix-shell-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (GNU Bash 4.4 / 5.1 / 5.2+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Bash**: `local x=$(cmd)` masking exit codes under `set -e`, unquoted `$@` instead of `"$@"`, and parsing `ls` output instead of `nullglob` globs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
