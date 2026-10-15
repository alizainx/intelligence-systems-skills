# Deep Engineering Reference: Scheme (R6RS/R7RS / Chez / Guile) Proper Tail Calls, Hygienic Macros & Delimited Continuations (`scheme-continuations-hygienic-macros`)

- **Language / Representation**: **Scheme**
- **Taxonomic Classification**: `Functional Programming Language`
- **Technical Relationship**: Minimalist lexical-scoped Lisp dialect (R6RS / R7RS-small / Chez Scheme / Guile) guaranteeing proper tail recursion and hygienic `syntax-rules` / `syntax-case` macros.
- **Governing Standards & Versions**: IEEE Std 1178, R6RS, R7RS-small, SRFI Specifications (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Scheme** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Lisp-1 single namespace, mandatory proper tail-call optimization (TCO), named `let` iteration, and `define-record-type` (SRFI-9 / R7RS). |
| 2 | **Type System & Inference** | Latent dynamic types with disjoint predicates (`pair?`, `vector?`, `bytevector?`, `procedure?`) and numerical tower (`exact` rationals/bignums vs `inexact` floats). |
| 3 | **Memory Management** | Generational copying GC (Chez Scheme) / BDW or precise GC; use `bytevector` for unboxed binary data. |
| 4 | **Concurrency & Async Programming** | Fibers (Guile delimited continuations `call-with-prompt`), SRFI-18 threads, and Chez SMP threads. |
| 5 | **Standard Library & Ecosystem** | SRFIs (`srfi-1` lists, `srfi-64` testing, `srfi-145` assumptions), Akku.scm / Guild. |
| 6 | **Build Systems & Package Management** | R7RS `(define-library ... (import (scheme base)) (export ...))` or R6RS `(library ...)`. |
| 7 | **Compiler / Interpreter Behavior** | Chez Scheme nanopass compiler framework (50+ fine-grained intermediate IR passes) and Call-with-Current-Continuation (`call/cc`) stack segment copying. |
| 8 | **Debugging** | Chez `debug-on-exception`, trace macros (`trace-lambda`), and Guile `,bt` / `,locals` REPL meta-commands. |
| 9 | **Security** | Use `dynamic-wind` (in, body, out thunks) so resource cleanup runs even when continuations jump out of a dynamic extent. |
| 10 | **Performance Optimization** | Prefer delimited prompts or tail-recursive accumulator passing over full `call/cc` capture, and use fixnum/flonum operations (`fx+`, `fl+` in R6RS/Chez). |
| 11 | **Error Handling** | R6RS/R7RS `guard` and `with-exception-handler` condition hierarchies. |
| 12 | **Testing Methodologies** | SRFI-64 (`test-begin`, `test-equal`, `test-error`, `test-end`) portable test suites. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (R6RS / R7RS (Chez Scheme 10 / GNU Guile 3.0 / Chicken / Chibi)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Chez `foreign-procedure` and Guile `(system foreign)` C FFI. |
| 18 | **Common Engineering Mistakes** | Using `set-car!`/`set-cdr!` on quoted literal lists, capturing full `call/cc` continuations inside C FFI callbacks, and non-tail recursion. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/scheme-continuations-hygienic-macros/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Scheme**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Chez `debug-on-exception`, trace macros (`trace-lambda`), and Guile `,bt` / `,locals` REPL meta-commands.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `R7RS `(define-library ... (import (scheme base)) (export ...))` or R6RS `(library ...)`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Prefer delimited prompts or tail-recursive accumulator passing over full `call/cc` capture, and use fixnum/flonum operations (`fx+`, `fl+` in R6RS/Chez).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Use `dynamic-wind` (in, body, out thunks) so resource cleanup runs even when continuations jump out of a dynamic extent.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (SRFI-64 (`test-begin`, `test-equal`, `test-error`, `test-end`) portable test suites.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Chez `foreign-procedure` and Guile `(system foreign)` C FFI.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
