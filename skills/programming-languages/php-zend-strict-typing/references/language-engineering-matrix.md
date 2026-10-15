# Deep Engineering Reference: Modern PHP (8.2/8.3+) Strict Types, Readonly Classes, Enums, Fibers & PHPStan Level 9 (`php-zend-strict-typing`)

- **Language / Representation**: **PHP**
- **Taxonomic Classification**: `General-Purpose & Web Systems Language`
- **Technical Relationship**: Managed scripting/application language running on the Zend Engine (PHP 8.2/8.3+ OPcache JIT) with explicit strict-type mode and static analysis via PHPStan/Psalm.
- **Governing Standards & Versions**: PHP-FIG PSR-1, PSR-4, PSR-7, PSR-12, PSR-15 (PHP 8.2 / PHP 8.3+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **PHP** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Mandatory `declare(strict_types=1);` at line 1 of every file, `readonly class`, backed `enum Status: string`, and `match ($val)` (strict `===` comparison). |
| 2 | **Type System & Inference** | Union (`int|float`), intersection (`Countable&Iterator`), Disjunctive Normal Form (DNF) types, `never` return type, and `@template T` generics in PHPStan/Psalm. |
| 3 | **Memory Management** | Zend reference-counted `zval` copy-on-write + cycle collector; use generators (`yield`) for streaming large datasets with $O(1)$ memory. |
| 4 | **Concurrency & Async Programming** | PHP 8.1+ `Fiber` cooperative multitasking (Revolt/Amp/Swoole) and stateless shared-nothing FPM worker isolation. |
| 5 | **Standard Library & Ecosystem** | Composer (`composer.json`, `composer.lock`), PHPUnit, Pest, PHPStan, Psalm, Symfony/Laravel components. |
| 6 | **Build Systems & Package Management** | `composer install --no-dev --optimize-autoloader --classmap-authoritative`, `phpstan analyse --level=max`. |
| 7 | **Compiler / Interpreter Behavior** | Zend OPcache bytecode caching and tracing/function JIT (`opcache.jit=tracing`). |
| 8 | **Debugging** | Xdebug 3 (`xdebug.mode=debug,profile`), Blackfire, and `php -l` syntax linter. |
| 9 | **Security** | Always use `===` (never loose `==`), `password_hash(..., PASSWORD_ARGON2ID)`, `random_bytes()`, and `PDO::ATTR_EMULATE_PREPARES => false`. |
| 10 | **Performance Optimization** | Preload classes via `opcache.preload`, avoid dynamic property creation (deprecated in PHP 8.2+), and use packed arrays. |
| 11 | **Error Handling** | Throw typed `DomainException`/`InvalidArgumentException` hierarchies; enable `JSON_THROW_ON_ERROR` on `json_decode`/`json_encode`. |
| 12 | **Testing Methodologies** | PHPUnit 10/11 strict mode (`failOnWarning`, `failOnRisky`) + Infection mutation testing. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (PHP 8.2 / PHP 8.3+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `FFI::cdef` for binding C shared libraries in CLI/daemon processes. |
| 18 | **Common Engineering Mistakes** | Omitting `declare(strict_types=1);` causing silent string-to-int coercion, using `switch` (loose `==`) instead of `match` (strict `===`), and `unserialize()` on user input. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/php-zend-strict-typing/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **PHP**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Xdebug 3 (`xdebug.mode=debug,profile`), Blackfire, and `php -l` syntax linter.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``composer install --no-dev --optimize-autoloader --classmap-authoritative`, `phpstan analyse --level=max`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Preload classes via `opcache.preload`, avoid dynamic property creation (deprecated in PHP 8.2+), and use packed arrays.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Always use `===` (never loose `==`), `password_hash(..., PASSWORD_ARGON2ID)`, `random_bytes()`, and `PDO::ATTR_EMULATE_PREPARES => false`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (PHPUnit 10/11 strict mode (`failOnWarning`, `failOnRisky`) + Infection mutation testing.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`FFI::cdef` for binding C shared libraries in CLI/daemon processes.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
