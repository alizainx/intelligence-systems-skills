---
name: php-zend-strict-typing
description: Engineer, audit, and verify modern PHP 8.2/8.3+ software using declare(strict_types=1), readonly classes, backed Enums, intersection/DNF types, Zend OPcache JIT tuning, PDO prepared statements, and PHPStan Level 9 static analysis.
allowed-tools: execute_bash view_file write_to_file
---

# Modern PHP (8.2/8.3+) Strict Types, Readonly Classes, Enums, Fibers & PHPStan Level 9

Engineer, audit, and verify modern PHP 8.2/8.3+ software using declare(strict_types=1), readonly classes, backed Enums, intersection/DNF types, Zend OPcache JIT tuning, PDO prepared statements, and PHPStan Level 9 static analysis.

## A. Identity

- **Skill Name**: `php-zend-strict-typing`
- **Domain**: `programming-languages`
- **Language / Representation**: **PHP** (`General-Purpose & Web Systems Language`)
- **Technical Relationship**: Managed scripting/application language running on the Zend Engine (PHP 8.2/8.3+ OPcache JIT) with explicit strict-type mode and static analysis via PHPStan/Psalm.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **PHP**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: PHP-FIG PSR-1, PSR-4, PSR-7, PSR-12, PSR-15 (PHP 8.2 / PHP 8.3+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``composer install --no-dev --optimize-autoloader --classmap-authoritative`, `phpstan analyse --level=max`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **PHP** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **PHP**.

### Technical Triggers

- Files, build manifests, or prompts targeting **PHP** (`StrictReadonlyMoney.php`, ``composer install --no-dev --optimize-autoloader --classmap-authoritative`, `phpstan analyse --level=max`.`).

### Prerequisites

- Target language version (PHP 8.2 / PHP 8.3+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **PHP** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (PHP 8.2 / PHP 8.3+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Zend reference-counted `zval` copy-on-write + cycle collector; use generators (`yield`) for streaming large datasets with $O(1)$ memory.), type soundness limits (Union (`int|float`), intersection (`Countable&Iterator`), Disjunctive Normal Form (DNF) types, `never` return type, and `@template T` generics in PHPStan/Psalm.), and concurrency hazards (PHP 8.1+ `Fiber` cooperative multitasking (Revolt/Amp/Swoole) and stateless shared-nothing FPM worker isolation.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce PHP-FIG PSR-1, PSR-4, PSR-7, PSR-12, PSR-15.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Mandatory `declare(strict_types=1);` at line 1 of every file, `readonly class`, backed `enum Status: string`, and `match ($val)` (strict `===` comparison).
2. **Type System & Inference**: Union (`int|float`), intersection (`Countable&Iterator`), Disjunctive Normal Form (DNF) types, `never` return type, and `@template T` generics in PHPStan/Psalm.
3. **Memory Management**: Zend reference-counted `zval` copy-on-write + cycle collector; use generators (`yield`) for streaming large datasets with $O(1)$ memory.
4. **Concurrency & Async Programming**: PHP 8.1+ `Fiber` cooperative multitasking (Revolt/Amp/Swoole) and stateless shared-nothing FPM worker isolation.
5. **Standard Library & Ecosystem**: Composer (`composer.json`, `composer.lock`), PHPUnit, Pest, PHPStan, Psalm, Symfony/Laravel components.
6. **Build Systems & Package Management**: `composer install --no-dev --optimize-autoloader --classmap-authoritative`, `phpstan analyse --level=max`.
7. **Compiler / Interpreter Behavior**: Zend OPcache bytecode caching and tracing/function JIT (`opcache.jit=tracing`).
8. **Debugging & Observability**: Xdebug 3 (`xdebug.mode=debug,profile`), Blackfire, and `php -l` syntax linter.
9. **Security Hardening**: Always use `===` (never loose `==`), `password_hash(..., PASSWORD_ARGON2ID)`, `random_bytes()`, and `PDO::ATTR_EMULATE_PREPARES => false`.
10. **Performance Optimization**: Preload classes via `opcache.preload`, avoid dynamic property creation (deprecated in PHP 8.2+), and use packed arrays.
11. **Error Handling Discipline**: Throw typed `DomainException`/`InvalidArgumentException` hierarchies; enable `JSON_THROW_ON_ERROR` on `json_decode`/`json_encode`.
12. **Testing Methodologies**: PHPUnit 10/11 strict mode (`failOnWarning`, `failOnRisky`) + Infection mutation testing.
13. **Interoperability & Cross-Platform ABI**: `FFI::cdef` for binding C shared libraries in CLI/daemon processes.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/php-zend-strict-typing/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (PHP 8.2 / PHP 8.3+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in PHP**: Omitting `declare(strict_types=1);` causing silent string-to-int coercion, using `switch` (loose `==`) instead of `match` (strict `===`), and `unserialize()` on user input.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
