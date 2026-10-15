# Deep Engineering Reference: D Systems Programming (@safe, @nogc, dip1000 Scope Pointers & -betterC) (`d-systems-programming`)

- **Language / Representation**: **D**
- **Taxonomic Classification**: `Systems Programming Language`
- **Technical Relationship**: Native systems programming language supporting both GC-managed application code and `@safe @nogc nothrow pure` freestanding/C-compatible `-betterC` systems programming.
- **Governing Standards & Versions**: D Language Specification (DMD / LDC2 / GDC), DIP1000 Scoped Pointers (D 2.105+ (LDC 1.36+))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **D** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `scope(exit)`/`scope(failure)` deterministic cleanup, `in`/`out` contract blocks, and `static if` Design by Introspection. |
| 2 | **Type System & Inference** | Function safety attributes (`@safe`, `@trusted`, `@system`), purity (`pure`), GC-freedom (`@nogc`), and template constraints (`if (isIntegral!T)`). |
| 3 | **Memory Management** | Enforce `@nogc` in real-time/kernel paths, `scope`/`return scope` (`-preview=dip1000`) to prevent escaping stack pointers, and `-betterC` for zero runtime dependency. |
| 4 | **Concurrency & Async Programming** | `shared` type qualifier preventing accidental thread sharing, `core.atomic`, and message-passing `std.concurrency`. |
| 5 | **Standard Library & Ecosystem** | Phobos (`std.algorithm`, `std.range`), `core.stdc`, DUB package manager. |
| 6 | **Build Systems & Package Management** | `dub.json`/`dub.sdl`, `ldc2 -O3 -release -boundscheck=safeonly -preview=dip1000`. |
| 7 | **Compiler / Interpreter Behavior** | CTFE (Compile-Time Function Execution), slice bounds checks preserved in `@safe` code even in `-release` mode. |
| 8 | **Debugging** | GDB/LLDB DWARF support, `-fsanitize=address` in LDC2. |
| 9 | **Security** | Keep `@trusted` wrappers minimal and audit every pointer slice construction `ptr[0 .. len]` inside `@trusted`. |
| 10 | **Performance Optimization** | Lazy range pipelines (zero intermediate allocations), `ldc.simd`, and `struct` value semantics on the stack. |
| 11 | **Error Handling** | `nothrow` error-code/tagged-union returns in `@nogc` systems code (`Exceptions` allocate on GC heap unless pre-allocated/DIP1008). |
| 12 | **Testing Methodologies** | Built-in `unittest {}` blocks verified via `dub test`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (D 2.105+ (LDC 1.36+)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `extern(C)` and `extern(C++)` ABI linkage plus ImportC direct `.c` file compilation. |
| 18 | **Common Engineering Mistakes** | Escaping slice references to stack arrays without `-preview=dip1000`, and triggering hidden GC allocations via array concatenation `~` in hot loops. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/d-systems-programming/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **D**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GDB/LLDB DWARF support, `-fsanitize=address` in LDC2.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``dub.json`/`dub.sdl`, `ldc2 -O3 -release -boundscheck=safeonly -preview=dip1000`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Lazy range pipelines (zero intermediate allocations), `ldc.simd`, and `struct` value semantics on the stack.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Keep `@trusted` wrappers minimal and audit every pointer slice construction `ptr[0 .. len]` inside `@trusted`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Built-in `unittest {}` blocks verified via `dub test`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`extern(C)` and `extern(C++)` ABI linkage plus ImportC direct `.c` file compilation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
