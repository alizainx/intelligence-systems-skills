# Deep Engineering Reference: Ada (Ada 2012/2022) Strong Subtyping, Ravenscar Tasking & Representation Clauses (`ada-systems-engineering`)

- **Language / Representation**: **Ada**
- **Taxonomic Classification**: `Systems Programming Language`
- **Technical Relationship**: Strongly typed, safety-critical systems language standardized for avionics, rail, space, and defense (DO-178C / EN 50128).
- **Governing Standards & Versions**: ISO/IEC 8652:2012 (Ada 2012), ISO/IEC 8652:2023 (Ada 2022), DO-178C (Ada 2005 / Ada 2012 / Ada 2022)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Ada** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Explicit package specifications (`.ads`) vs bodies (`.adb`), parameter modes (`in`, `out`, `in out`), and aspect specifications (`with Pre => ...`). |
| 2 | **Type System & Inference** | Nominal distinct numeric types (`type Meters is new Float`), constrained range subtypes (`subtype Percent is Integer range 0 .. 100`), and discriminated records. |
| 3 | **Memory Management** | Stack-allocated unconstrained arrays (`String`), bounded containers (`Ada.Containers.Bounded_Vectors`), and custom `System.Storage_Pools` without `Unchecked_Deallocation`. |
| 4 | **Concurrency & Async Programming** | Protected objects (`protected type` with ceiling priority locking) and deterministic `pragma Profile (Ravenscar)` / `Jorvik` real-time tasks. |
| 5 | **Standard Library & Ecosystem** | GNAT Toolchain, Alire (`alr`) package manager, `Ada.Real_Time`, `Interfaces.C`. |
| 6 | **Build Systems & Package Management** | GPRbuild project files (`.gpr`) and Alire (`alire.toml`) with `-gnatwa -gnatwe -gnatVa` validity/overflow checks. |
| 7 | **Compiler / Interpreter Behavior** | GNAT runtime `Constraint_Error` checks on range/index/overflow (`-gnato`) and elaboration order analysis (`pragma Pure`, `pragma Preelaborate`). |
| 8 | **Debugging** | GDB with Ada mode (`catch exception`), `gnatmem`, and stack usage analysis (`-fcallgraph-info`). |
| 9 | **Security** | Eliminate buffer overruns via first/last array attributes (`Arr'First .. Arr'Last`) and forbid `Unchecked_Conversion` without size/alignment static checks. |
| 10 | **Performance Optimization** | `pragma Inline`, zero-copy slice views, and bit-exact hardware register overlays via representation clauses (`for Reg use record ...`). |
| 11 | **Error Handling** | Design by contract (`Dynamic_Predicate`, `Type_Invariant`) combined with bounded exception handlers in non-Ravenscar profiles. |
| 12 | **Testing Methodologies** | AUnit test harnesses and boundary range subtype testing. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Ada 2005 / Ada 2012 / Ada 2022); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `with Convention => C, Export => True, External_Name => "..."` using `Interfaces.C` types. |
| 18 | **Common Engineering Mistakes** | Hardcoding `1 .. Length` instead of `Arr'Range`, elaboration cycles across packages, and using heap `access` types in safety-critical profiles. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/ada-systems-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Ada**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GDB with Ada mode (`catch exception`), `gnatmem`, and stack usage analysis (`-fcallgraph-info`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `GPRbuild project files (`.gpr`) and Alire (`alire.toml`) with `-gnatwa -gnatwe -gnatVa` validity/overflow checks.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (`pragma Inline`, zero-copy slice views, and bit-exact hardware register overlays via representation clauses (`for Reg use record ...`).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Eliminate buffer overruns via first/last array attributes (`Arr'First .. Arr'Last`) and forbid `Unchecked_Conversion` without size/alignment static checks.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (AUnit test harnesses and boundary range subtype testing.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`with Convention => C, Export => True, External_Name => "..."` using `Interfaces.C` types.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
