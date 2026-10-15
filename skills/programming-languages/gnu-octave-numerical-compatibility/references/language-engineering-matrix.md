# Deep Engineering Reference: GNU Octave (8.x/9.x) Portable M-File Engineering, Vectorization & MATLAB Compatibility (`gnu-octave-numerical-compatibility`)

- **Language / Representation**: **GNU Octave**
- **Taxonomic Classification**: `Scientific & Numerical Computing Language`
- **Technical Relationship**: Open-source numerical matrix computing language largely syntax-compatible with MATLAB while adding GNU Octave extensions and `.oct` C++ bindings.
- **Governing Standards & Versions**: GNU Octave 8 / 9 Manual, Portable M-File Subset (GNU Octave 8.4 / 9.1+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **GNU Octave** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Maintain portable `end` (rather than Octave-only `endif`/`endfunction`) and `'...'` single-quoted strings when dual MATLAB compatibility is required. |
| 2 | **Type System & Inference** | Dense IEEE 754 matrices, sparse CSC matrices (`sparse`), cell arrays, and struct arrays. |
| 3 | **Memory Management** | Reference-counted copy-on-write `octave_value` containers; preallocate with `zeros`/`NaN`. |
| 4 | **Concurrency & Async Programming** | `parcellfun` / `pararrayfun` (`parallel` Forge package) and multi-threaded OpenBLAS. |
| 5 | **Standard Library & Ecosystem** | Octave Forge (`pkg install -forge control signal optim`), OpenBLAS, SuiteSparse. |
| 6 | **Build Systems & Package Management** | `pkg` package manager (`DESCRIPTION`, `INDEX`) and `mkoctfile` for native C++/Fortran extensions. |
| 7 | **Compiler / Interpreter Behavior** | AST tree-walker interpreter; vectorization into underlying C++/Fortran BLAS/LAPACK routines is critical because scalar loops are not JIT-compiled. |
| 8 | **Debugging** | `dbstop`, `profile on`, `whos` memory inspection. |
| 9 | **Security** | Validate matrix dimensions (`ismatrix`, `isvector`, ` rows(A) == rows(b)`) and avoid `eval`. |
| 10 | **Performance Optimization** | Use `bsxfun` / implicit broadcasting, `accumarray`, and sparse matrices (`speye`, `spdiags`) to avoid scalar `for` loops. |
| 11 | **Error Handling** | `error('id:msg', ...)` and `unwind_protect ... unwind_protect_cleanup ... end_unwind_protect` (or portable `onCleanup`). |
| 12 | **Testing Methodologies** | Embedded `%!test` and `%!assert(actual, expected, tol)` blocks executed via `test filename.m`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (GNU Octave 8.4 / 9.1+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `mkoctfile` (`.oct` native C++ API) and `.mex` compatibility API. |
| 18 | **Common Engineering Mistakes** | Writing unvectorized scalar loops in Octave, using `+=` or `"double quotes"` in files meant to run in both Octave and MATLAB without checking. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/gnu-octave-numerical-compatibility/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **GNU Octave**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``dbstop`, `profile on`, `whos` memory inspection.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``pkg` package manager (`DESCRIPTION`, `INDEX`) and `mkoctfile` for native C++/Fortran extensions.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `bsxfun` / implicit broadcasting, `accumarray`, and sparse matrices (`speye`, `spdiags`) to avoid scalar `for` loops.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Validate matrix dimensions (`ismatrix`, `isvector`, ` rows(A) == rows(b)`) and avoid `eval`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Embedded `%!test` and `%!assert(actual, expected, tol)` blocks executed via `test filename.m`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`mkoctfile` (`.oct` native C++ API) and `.mex` compatibility API.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
