# Deep Engineering Reference: Nim Systems Programming (ARC/ORC Memory Management, Effect System & Hygienic Macros) (`nim-systems-programming`)

- **Language / Representation**: **Nim**
- **Taxonomic Classification**: `Systems Programming Language`
- **Technical Relationship**: Statically typed systems language compiling to C/C++ with deterministic ARC/ORC reference counting and hygienic AST macro metaprogramming.
- **Governing Standards & Versions**: Nim Manual (Nim 2.0+ Default ARC/ORC Memory Model) (Nim 2.0 / 2.2+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Nim** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Indentation-based syntax with hygienic typed AST macros (`macro`), `defer:`, and ``=destroy``/``=sink``/``=copy`` lifetime hooks. |
| 2 | **Type System & Inference** | `distinct` types (`typeMeters = distinct float64`), ordinal subranges (`range[0..255]`), concept constraints, and compile-time effect tracking (`.raises: []`, `.noSideEffect`). |
| 3 | **Memory Management** | `--mm:orc` (cycle-collecting deterministic RC) or `--mm:arc` (hard real-time deterministic RC without cycle collector); use `sink` and `lent` to avoid refcount traffic. |
| 4 | **Concurrency & Async Programming** | `Isolated[T]` ownership transfer across threads (`std/tasks`, `malebolgia`) preventing shared mutable heap races under ARC/ORC. |
| 5 | **Standard Library & Ecosystem** | Nimble package manager, `std/strformat`, `std/monotimes`, `chronos` async. |
| 6 | **Build Systems & Package Management** | `nimble build`, `nim c --mm:orc --panics:on -d:release`. |
| 7 | **Compiler / Interpreter Behavior** | Compiles to ISO C/C++ in `nimcache/`; respects backend C compiler sanitizer flags (`--passC:-fsanitize=address,undefined`). |
| 8 | **Debugging** | `--debugger:native` emitting `#line` directives mapped to Nim source in GDB/LLDB. |
| 9 | **Security** | Compile-time `.raises: [IOError]` effect annotations and runtime bounds/overflow checks (`--overflowChecks:on`). |
| 10 | **Performance Optimization** | `--mm:arc` deterministic destruction, value-type `object` (stack) vs `ref object` (heap), and `=sink` move optimization. |
| 11 | **Error Handling** | Checked exception tracking via `{.raises: [].}` pragma or `Result[T, E]` value returns. |
| 12 | **Testing Methodologies** | `unittest` and `testament` suites compiled with `--mm:orc` and C sanitizers. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Nim 2.0 / 2.2+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `{.importc, header: "...".}` and `{.exportc, cdecl.}` zero-glue C/C++ FFI. |
| 18 | **Common Engineering Mistakes** | Creating reference cycles under `--mm:arc` without `{.cursor.}` annotations, and omitting `{.raises: [].}` on C FFI callbacks. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/nim-systems-programming/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Nim**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``--debugger:native` emitting `#line` directives mapped to Nim source in GDB/LLDB.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``nimble build`, `nim c --mm:orc --panics:on -d:release`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (`--mm:arc` deterministic destruction, value-type `object` (stack) vs `ref object` (heap), and `=sink` move optimization.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Compile-time `.raises: [IOError]` effect annotations and runtime bounds/overflow checks (`--overflowChecks:on`).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`unittest` and `testament` suites compiled with `--mm:orc` and C sanitizers.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`{.importc, header: "...".}` and `{.exportc, cdecl.}` zero-glue C/C++ FFI.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
