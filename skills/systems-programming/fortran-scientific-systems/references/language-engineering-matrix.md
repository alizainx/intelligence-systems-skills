# Deep Engineering Reference: Modern Fortran (2008/2018/2023) Array Computing, Coarrays, OpenMP & ISO_C_BINDING (`fortran-scientific-systems`)

- **Language / Representation**: **Fortran**
- **Taxonomic Classification**: `Scientific & High-Performance Systems Language`
- **Technical Relationship**: High-performance numerical and array-computing language (Fortran 2008/2018/2023) with native column-major multidimensional arrays, Coarrays, and `iso_c_binding`.
- **Governing Standards & Versions**: ISO/IEC 1539-1:2018 (Fortran 2018), ISO/IEC 1539-1:2023 (Fortran 2023) (Fortran 2008 / 2018 / 2023)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Fortran** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Free-form `.f90`/`.f08` source, mandatory `implicit none (type, external)`, explicit `intent(in|out|inout)` on all dummy arguments, and `pure`/`elemental` procedures. |
| 2 | **Type System & Inference** | Portable precision via `use, intrinsic :: iso_fortran_env, only: real64, int64`; never use non-portable `REAL*8` or default single precision. |
| 3 | **Memory Management** | Automatic deallocation of local `allocatable` arrays on scope exit (unlike raw `pointer` attributes which leak) and `contiguous` pointer/array guarantees. |
| 4 | **Concurrency & Async Programming** | `do concurrent` loop parallelism, native Fortran 2018 Coarrays (`x[i]`, `sync all`), OpenMP, and MPI (`mpi_f08`). |
| 5 | **Standard Library & Ecosystem** | BLAS, LAPACK, FFTW, NetCDF, HDF5, `stdlib` (`fortran-lang`). |
| 6 | **Build Systems & Package Management** | Fortran Package Manager (`fpm.toml`), CMake, `gfortran -std=f2018 -Wall -Wextra -Werror -fcheck=all -fimplicit-none`. |
| 7 | **Compiler / Interpreter Behavior** | Fortran assumes dummy arguments do not alias, enabling aggressive auto-vectorization without `restrict` keywords. |
| 8 | **Debugging** | `-fcheck=bounds,do,mem,pointer,recursion`, `-ffpe-trap=invalid,zero,overflow`, and GDB array slice inspection. |
| 9 | **Security** | Prevent out-of-bounds array indexing via assumed-shape arrays (`real(real64), intent(in) :: a(:, :)`) instead of legacy assumed-size `a(*)`. |
| 10 | **Performance Optimization** | Iterate leftmost index (`i`) in the innermost loop (`A(i, j)`) to match Fortran column-major memory layout (`stride-1`). |
| 11 | **Error Handling** | Inspect `stat=` and `errmsg=` on `allocate`/`deallocate` and check IEEE floating-point exceptions via `ieee_arithmetic`. |
| 12 | **Testing Methodologies** | `test-drive` or `pfUnit` assertion suites checking relative `real64` tolerances. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Fortran 2008 / 2018 / 2023); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `use, intrinsic :: iso_c_binding` with `bind(C, name="...")` and awareness of transposed C row-major vs Fortran column-major indexing. |
| 18 | **Common Engineering Mistakes** | Initializing module/local variables at declaration (`integer :: n = 0` implicitly adds `save` attribute!), row-major inner loops thrashing L1 cache, and omitting `implicit none`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/fortran-scientific-systems/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Fortran**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``-fcheck=bounds,do,mem,pointer,recursion`, `-ffpe-trap=invalid,zero,overflow`, and GDB array slice inspection.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Fortran Package Manager (`fpm.toml`), CMake, `gfortran -std=f2018 -Wall -Wextra -Werror -fcheck=all -fimplicit-none`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Iterate leftmost index (`i`) in the innermost loop (`A(i, j)`) to match Fortran column-major memory layout (`stride-1`).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Prevent out-of-bounds array indexing via assumed-shape arrays (`real(real64), intent(in) :: a(:, :)`) instead of legacy assumed-size `a(*)`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`test-drive` or `pfUnit` assertion suites checking relative `real64` tolerances.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`use, intrinsic :: iso_c_binding` with `bind(C, name="...")` and awareness of transposed C row-major vs Fortran column-major indexing.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
