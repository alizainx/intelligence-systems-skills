# Deep Engineering Reference: Common Lisp (ANSI / SBCL) Type Declarations, CLOS Generic Functions, Condition Restarts & Hygienic Macros (`common-lisp-clos-macros`)

- **Language / Representation**: **Common Lisp**
- **Taxonomic Classification**: `Multi-Paradigm & Symbolic Functional Programming Language`
- **Technical Relationship**: ANSI X3.226 image-based compiled Lisp (SBCL) with the Common Lisp Object System (CLOS), condition/restart system, and unboxed native code compilation.
- **Governing Standards & Versions**: ANSI INCITS 226-1994 (R1999) Common Lisp Standard, SBCL User Manual (ANSI Common Lisp (SBCL 2.3 / 2.4+))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Common Lisp** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Lisp-2 namespace (`#'fn` vs variable value), lexical scope by default (`defparameter`/`defvar` earmarked `*special*`), and homoiconic S-expression macros (`defmacro`). |
| 2 | **Type System & Inference** | Dynamic typing with optional gradual static type inference and compilation notes in SBCL (`declaim (ftype (function (fixnum fixnum) fixnum) ...)`). |
| 3 | **Memory Management** | SBCL generational GC, `dynamic-extent` stack allocation declarations, and typed unboxed arrays (`(simple-array double-float (*))`). |
| 4 | **Concurrency & Async Programming** | `bordeaux-threads`, `lparallel` worker pools, and `sb-concurrency` lock-free queues/mailboxes. |
| 5 | **Standard Library & Ecosystem** | ASDF 3 build system, Quicklisp / Qlot (`qlfile.lock`), Alexandria, Serapeum, FiveAM, Coalton. |
| 6 | **Build Systems & Package Management** | `.asd` system definitions (`:serial t` or package-inferred systems) and standalone binaries via `(sb-ext:save-lisp-and-die ... :executable t)`. |
| 7 | **Compiler / Interpreter Behavior** | SBCL Python compiler emitting native machine code directly; inspect disassembly via `(disassemble #'fn)` and resolve all compiler efficiency notes. |
| 8 | **Debugging** | SLIME/SLY interactive inspector, stack frame restartable debugger, and `sb-sprof` statistical profiler. |
| 9 | **Security** | Set `*read-eval*` to `nil` (`(with-standard-io-syntax (let ((*read-eval* nil)) (read ...)))`) before reading untrusted S-expressions to prevent `#.` reader macro RCE! |
| 10 | **Performance Optimization** | Prevent variable capture in macros using `gensym` / `alexandria:with-unique-names`, declare `(type (simple-array ...))`, and avoid `(safety 0)` in production. |
| 11 | **Error Handling** | Separate mechanism from policy using Common Lisp's Condition System (`signal`, `error`, `restart-case`, `handler-bind`, `handler-case`). |
| 12 | **Testing Methodologies** | `FiveAM` / `Parachute` / `Rove` test suites run via `(asdf:test-system :my-sys)`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (ANSI Common Lisp (SBCL 2.3 / 2.4+)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | CFFI (`cffi:defcfun`, `cffi:with-foreign-object`) portable across SBCL, CCL, and ECL. |
| 18 | **Common Engineering Mistakes** | Mutating quoted literal constants (`'(1 2 3)`), variable capture in `defmacro` without `gensym`, and leaving `*read-eval*` true on external inputs. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/common-lisp-clos-macros/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Common Lisp**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `SLIME/SLY interactive inspector, stack frame restartable debugger, and `sb-sprof` statistical profiler.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``.asd` system definitions (`:serial t` or package-inferred systems) and standalone binaries via `(sb-ext:save-lisp-and-die ... :executable t)`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Prevent variable capture in macros using `gensym` / `alexandria:with-unique-names`, declare `(type (simple-array ...))`, and avoid `(safety 0)` in production.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Set `*read-eval*` to `nil` (`(with-standard-io-syntax (let ((*read-eval* nil)) (read ...)))`) before reading untrusted S-expressions to prevent `#.` reader macro RCE!).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`FiveAM` / `Parachute` / `Rove` test suites run via `(asdf:test-system :my-sys)`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (CFFI (`cffi:defcfun`, `cffi:with-foreign-object`) portable across SBCL, CCL, and ECL.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
