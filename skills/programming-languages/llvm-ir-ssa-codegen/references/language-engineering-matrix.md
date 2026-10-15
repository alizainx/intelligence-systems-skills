# Deep Engineering Reference: LLVM IR (LLVM 15–19 Opaque Pointers) SSA Dominance, GEP Inbounds, Poison/Freeze & Optimization (`llvm-ir-ssa-codegen`)

- **Language / Representation**: **LLVM IR**
- **Taxonomic Classification**: `Compiler Static Single Assignment Intermediate Representation`
- **Technical Relationship**: Typed, target-aware SSA intermediate representation (`.ll` text / `.bc` bitcode) sitting between language frontends (`clang`, `rustc`, `zig`, `swiftc`, `julia`) and LLVM machine backends.
- **Governing Standards & Versions**: LLVM Language Reference Manual (LangRef LLVM 15–19) (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **LLVM IR** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Infinite virtual registers (`%0`, `%x`) assigned exactly once (Static Single Assignment), explicit basic blocks ending with a terminator (`ret`, `br`, `switch`, `unreachable`), and `phi` nodes at control-flow joins. |
| 2 | **Type System & Inference** | First-class sized types (`i1`, `i8`, `i32`, `i64`, `float`, `double`, `<4 x float>`, `[N x T]`, `{ i32, ptr }`) and LLVM 15+ unified opaque pointer `ptr` (explicit type passed to `load`/`getelementptr` instead of `i32*`). |
| 3 | **Memory Management** | Entry-block `alloca` stack slots promoted to SSA registers via `mem2reg` (`sroa`), explicit `align N` on loads/stores, and `!tbaa` / `noalias` metadata. |
| 4 | **Concurrency & Async Programming** | `atomicrmw`, `cmpxchg`, `fence syncscope("singlethread"|"") seq_cst|acq_rel|acquire|release`. |
| 5 | **Standard Library & Ecosystem** | `opt` (`opt -passes=verify,mem2reg,instcombine,gvn`), `llc`, `llvm-as`, `llvm-dis`, `lli`, `Alive2` (`alive-tv`). |
| 6 | **Build Systems & Package Management** | `opt -passes=verify module.ll -disable-output` and `llc -O2 -filetype=obj module.ll`. |
| 7 | **Compiler / Interpreter Behavior** | Distinguish immediate UB (dividing by `0`, dereferencing `null`/`poison`) from deferred `poison` (`add nsw` overflow produces `poison`, which triggers UB if branched on unless stabilized with `freeze`). |
| 8 | **Debugging** | `opt -print-after-all`, `llvm-extract`, `bugpoint` / `llvm-reduce` crash reducer. |
| 9 | **Security** | Enforce `inbounds` on `getelementptr` only when offset arithmetic stays within the allocated object + 1-past-end byte; emit `llvm.ubsantrap` for checked arithmetic. |
| 10 | **Performance Optimization** | Place all `alloca` instructions in the entry basic block (never inside loops, which causes dynamic stack growth and prevents `mem2reg` SSA promotion!). |
| 11 | **Error Handling** | `invoke` / `landingpad` (Itanium C++/Rust unwinding) or `@llvm.experimental.deoptimize`. |
| 12 | **Testing Methodologies** | Verify SSA single-assignment, CFG dominance before use, and `phi` predecessor completeness. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (LLVM 15 / 16 / 17 / 18 / 19 (Opaque Pointers `ptr`)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `target datalayout` and `target triple` ABI lowering (`sret`, `byval`, `zext`/`sext` parameter attributes). |
| 18 | **Common Engineering Mistakes** | Using deprecated typed pointers (`i32*`) in LLVM 15+, placing `alloca` inside a loop body, and branching on a potentially `poison` condition without `freeze`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/llvm-ir-ssa-codegen/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **LLVM IR**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``opt -print-after-all`, `llvm-extract`, `bugpoint` / `llvm-reduce` crash reducer.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``opt -passes=verify module.ll -disable-output` and `llc -O2 -filetype=obj module.ll`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Place all `alloca` instructions in the entry basic block (never inside loops, which causes dynamic stack growth and prevents `mem2reg` SSA promotion!).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Enforce `inbounds` on `getelementptr` only when offset arithmetic stays within the allocated object + 1-past-end byte; emit `llvm.ubsantrap` for checked arithmetic.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Verify SSA single-assignment, CFG dominance before use, and `phi` predecessor completeness.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`target datalayout` and `target triple` ABI lowering (`sret`, `byval`, `zext`/`sext` parameter attributes).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
