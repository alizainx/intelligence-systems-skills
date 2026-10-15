# Deep Engineering Reference: Racket (8.12+) #lang DSLs, syntax/parse Macros, Higher-Order Contracts & Typed Racket (`racket-language-oriented-programming`)

- **Language / Representation**: **Racket**
- **Taxonomic Classification**: `Language-Oriented & Functional Programming Language`
- **Technical Relationship**: Descendant of Scheme Built on Chez Scheme runtime, pioneering Language-Oriented Programming (`#lang`), syntax objects with lexical scope sets, and Higher-Order Contracts.
- **Governing Standards & Versions**: The Racket Reference & Guide (Racket CS 8.12+) (Racket 8.10 / 8.12+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Racket** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Explicit `#lang racket/base` or `#lang typed/racket/base` module header, immutable cons pairs by default (`cons` is immutable; `mcons` is mutable), and `for/fold` comprehensions. |
| 2 | **Type System & Inference** | Higher-order runtime contracts (`->i`, `and/c`, `listof`) with precise blame assignment across module boundaries, plus static occurrence typing in `#lang typed/racket`. |
| 3 | **Memory Management** | Chez Scheme generational GC + Racket **Custodians** (`make-custodian`, `custodian-shutdown-all`) guaranteeing deterministic cleanup of ports, threads, and sockets. |
| 4 | **Concurrency & Async Programming** | Green threads, CML-style synchronizable events (`sync`, `choice-evt`, `handle-evt`, channels, alarms), and OS-level `place` / `future` parallelism. |
| 5 | **Standard Library & Ecosystem** | `raco pkg`, `rackunit`, `syntax/parse`, `scribble`, `redex` (operational semantics modeling). |
| 6 | **Build Systems & Package Management** | `info.rkt` package metadata, `raco setup`, `raco test`, `raco exe`. |
| 7 | **Compiler / Interpreter Behavior** | Set-of-scopes hygiene model (`syntax-parse` syntax classes with automatic error reporting) compiled through Racket's Chez Scheme backend. |
| 8 | **Debugging** | Errortrace source-location stacktraces (`racket -l errortrace -t ...`), Macro Stepper, and Contract profiler (`contract-profile`). |
| 9 | **Security** | Enforce `make-security-guard` and memory-limited custodians (`custodian-limit-memory`) when evaluating untrusted `#lang` modules. |
| 10 | **Performance Optimization** | Prefer `#lang racket/base` over full `#lang racket` for fast startup, and avoid high-frequency Typed/Untyped boundary crossings (which wrap values in runtime contract chaperones). |
| 11 | **Error Handling** | `with-handlers` structured exception matching (`exn:fail:contract?`, `exn:fail:filesystem?`). |
| 12 | **Testing Methodologies** | `module+ test` submodules with `rackunit` (`check-equal?`, `check-exn`) executed automatically by `raco test`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Racket 8.10 / 8.12+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `ffi/unsafe` C FFI (`define-cstruct`, `_fun`). |
| 18 | **Common Engineering Mistakes** | Crossing Typed Racket <-> Untyped Racket boundaries inside tight inner loops (chaperone overhead), and using legacy `syntax-rules` without `syntax/parse` validation. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/racket-language-oriented-programming/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Racket**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Errortrace source-location stacktraces (`racket -l errortrace -t ...`), Macro Stepper, and Contract profiler (`contract-profile`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``info.rkt` package metadata, `raco setup`, `raco test`, `raco exe`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Prefer `#lang racket/base` over full `#lang racket` for fast startup, and avoid high-frequency Typed/Untyped boundary crossings (which wrap values in runtime contract chaperones).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Enforce `make-security-guard` and memory-limited custodians (`custodian-limit-memory`) when evaluating untrusted `#lang` modules.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`module+ test` submodules with `rackunit` (`check-equal?`, `check-exn`) executed automatically by `raco test`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`ffi/unsafe` C FFI (`define-cstruct`, `_fun`).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
