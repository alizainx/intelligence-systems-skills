# Deep Engineering Reference: MATLAB (R2022b–R2024b+) Vectorized Matrix Algebra, Arguments Validation & Coder Readiness (`matlab-matrix-numerical-engineering`)

- **Language / Representation**: **MATLAB**
- **Taxonomic Classification**: `Numerical & Matrix Computing Language`
- **Technical Relationship**: Proprietary numerical computing environment and matrix language with column-major storage, `arguments` validation blocks, and MEX C/C++/CUDA codegen.
- **Governing Standards & Versions**: MathWorks MATLAB Language Reference (R2022b–R2024b), MAB Modeling Guidelines (MATLAB R2022b / R2023b / R2024b)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **MATLAB** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | 1-based column-major arrays, implicit expansion (broadcasting), `arguments ... end` function input validation blocks, and elementwise `.*/./.^` vs matrix `*`/`/`/`^`. |
| 2 | **Type System & Inference** | Dense `double`/`single`/fixed-point `fi`, `struct`, `table`, `timetable`, and strong classdef value vs `< handle` reference semantics. |
| 3 | **Memory Management** | Copy-on-write array sharing; preallocate outputs via `zeros(N, M, 'like', A)` before any loop. |
| 4 | **Concurrency & Async Programming** | Parallel Computing Toolbox `parfor` (loop-variable slicing classification), `spmd`, and `gpuArray`. |
| 5 | **Standard Library & Ecosystem** | Control System, Signal Processing, Optimization, Simulink, MATLAB Coder (`%#codegen`), `matlab.unittest`. |
| 6 | **Build Systems & Package Management** | MATLAB Projects (`.prj`), `buildtool` (`buildfile.m`), `codeIssues` static analyzer (`checkcode`). |
| 7 | **Compiler / Interpreter Behavior** | LXE JIT accelerator + `%#codegen` static type/size inference for C/C++/HDL generation. |
| 8 | **Debugging** | `dbstop if error`, `dbstop if naninf`, Profiler (`profile on; ...; profile viewer`). |
| 9 | **Security** | Avoid `eval`/`feval` with unchecked strings and check matrix conditioning (`rcond(A)`) before solving. |
| 10 | **Performance Optimization** | Never compute `inv(A) * b` (always use `A \ b` or `decomposition(A)`), iterate column-major (row index inner, column index outer), and vectorize. |
| 11 | **Error Handling** | `MException('Component:Mnemonic', 'Message %s', detail)` with `try`/`catch ME`. |
| 12 | **Testing Methodologies** | `matlab.unittest.TestCase` (`verifyEqual(actual, expected, 'RelTol', 1e-12)`). |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (MATLAB R2022b / R2023b / R2024b); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | MEX C/C++ API (`mexFunction`), `loadlibrary`, and Python/C++ engine interfaces. |
| 18 | **Common Engineering Mistakes** | Using `inv(A)*b` instead of `A\b`, overloading `i` or `j` as loop counters (shadowing imaginary unit; use `1i`), and growing arrays inside loops. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/matlab-matrix-numerical-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **MATLAB**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``dbstop if error`, `dbstop if naninf`, Profiler (`profile on; ...; profile viewer`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `MATLAB Projects (`.prj`), `buildtool` (`buildfile.m`), `codeIssues` static analyzer (`checkcode`).`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Never compute `inv(A) * b` (always use `A \ b` or `decomposition(A)`), iterate column-major (row index inner, column index outer), and vectorize.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Avoid `eval`/`feval` with unchecked strings and check matrix conditioning (`rcond(A)`) before solving.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`matlab.unittest.TestCase` (`verifyEqual(actual, expected, 'RelTol', 1e-12)`).).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (MEX C/C++ API (`mexFunction`), `loadlibrary`, and Python/C++ engine interfaces.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
