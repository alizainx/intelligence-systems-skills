# Deep Engineering Reference: SPARK 2014 Deductive Formal Verification (AoRTE, Flow Analysis & Ghost Code) (`spark-formal-verification`)

- **Language / Representation**: **SPARK**
- **Taxonomic Classification**: `Formal Verification Contract Sublanguage (Ada Subset)`
- **Technical Relationship**: Formally verifiable subset and deductive contract language of Ada (`SPARK_Mode => On`), verified statically via GNATprove (Why3 / Z3 / CVC5 / Alt-Ergo).
- **Governing Standards & Versions**: SPARK 2014 Reference Manual, DO-178C Formal Methods Supplement (DO-333) (SPARK 2014 (GNATprove 13 / 14))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **SPARK** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `pragma SPARK_Mode (On)` banning aliasing, side-effecting functions, controlled types, and arbitrary gotos/exceptions. |
| 2 | **Type System & Inference** | Strict ownership move/borrow rules for local access types in SPARK (Rust-like non-aliasing pointer verification) and subtype predicates. |
| 3 | **Memory Management** | Static stack/global allocation or formally tracked single-owner pointers with zero garbage collection or leaks. |
| 4 | **Concurrency & Async Programming** | Ravenscar protected objects verified free of data races and priority ceiling violations by GNATprove flow analysis. |
| 5 | **Standard Library & Ecosystem** | SPARK Lemma Library (`SPARK.Lemmas`), `SPARK.Containers.Formal`, Why3, Z3, CVC5, Alt-Ergo. |
| 6 | **Build Systems & Package Management** | `gnatprove -P project.gpr --level=4 --mode=all` (Stone -> Bronze -> Silver -> Gold -> Platinum assurance levels). |
| 7 | **Compiler / Interpreter Behavior** | Generates Verification Conditions (VCs) for every possible division by zero, array index, range check, and arithmetic overflow. |
| 8 | **Debugging** | Counterexample trace inspection (`--ce`), `pragma Assert_And_Cut`, and ghost variables/functions (`with Ghost`). |
| 9 | **Security** | Information-flow contracts (`Depends => (Ciphertext => (Plaintext, Key))`) proving zero secret leakage to untrusted outputs. |
| 10 | **Performance Optimization** | Once `Silver`/`Gold` AoRTE is mathematically proven, runtime checks (`-gnatp`) can be safely suppressed with formal justification. |
| 11 | **Error Handling** | Total functions: preconditions (`Pre`) forbid invalid calls at compile time; `Contract_Cases` partition behavior exhaustively. |
| 12 | **Testing Methodologies** | Combine SMT deductive proofs (`gnatprove`) with boundary execution tests on hardware. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (SPARK 2014 (GNATprove 13 / 14)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Isolate hardware MMIO or C FFI inside `SPARK_Mode => Off` package bodies while exposing a formally specified `SPARK_Mode => On` package spec. |
| 18 | **Common Engineering Mistakes** | Writing weak `Loop_Invariant` clauses that fail inductive step proofs, omitting `Loop_Variant` for termination, and under-specifying `Global`/`Depends`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/systems-programming/spark-formal-verification/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **SPARK**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Counterexample trace inspection (`--ce`), `pragma Assert_And_Cut`, and ghost variables/functions (`with Ghost`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``gnatprove -P project.gpr --level=4 --mode=all` (Stone -> Bronze -> Silver -> Gold -> Platinum assurance levels).`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Once `Silver`/`Gold` AoRTE is mathematically proven, runtime checks (`-gnatp`) can be safely suppressed with formal justification.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Information-flow contracts (`Depends => (Ciphertext => (Plaintext, Key))`) proving zero secret leakage to untrusted outputs.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Combine SMT deductive proofs (`gnatprove`) with boundary execution tests on hardware.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Isolate hardware MMIO or C FFI inside `SPARK_Mode => Off` package bodies while exposing a formally specified `SPARK_Mode => On` package spec.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
