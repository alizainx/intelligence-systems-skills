# Deep Engineering Reference: Haskell (GHC 9.6/9.8+) Strictness Control, GADTs, Typeclasses, STM & Core Optimization (`haskell-lazy-typelevel`)

- **Language / Representation**: **Haskell**
- **Taxonomic Classification**: `Purely Functional Programming Language`
- **Technical Relationship**: Purely functional, call-by-need (lazy) language compiled by GHC via System FC core IR with GADTs, Type Families, and STM.
- **Governing Standards & Versions**: Haskell 2010 Report, GHC2021 / GHC2024 Language Extensions (GHC 9.4 / 9.6 / 9.8+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Haskell** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Call-by-need laziness by default (`Thunk` allocation); enforce strictness at accumulator boundaries via `BangPatterns` (`!`), `StrictData`, and `Data.List.foldl'`. |
| 2 | **Type System & Inference** | Hindley-Milner + System FC (`GADTs`, `TypeFamilies`, `DataKinds`, `RoleAnnotations`), `newtype` zero-cost wrappers (`GeneralizedNewtypeDeriving`), and total pattern matching (`-Wincomplete-patterns`). |
| 3 | **Memory Management** | GHC generational copying/compact-region GC; eliminate space leaks from lazy thunks in long-lived state (`TVar`, `IORef`, `Map.Strict`). |
| 4 | **Concurrency & Async Programming** | Lightweight green threads (`forkIO`), `async` structured concurrency (`withAsync`), and composable atomic `STM` transactions (`TVar`, `retry`, `orElse`). |
| 5 | **Standard Library & Ecosystem** | `base`, `text`, `bytestring`, `containers`, ` unordered-containers`, `vector`, `stm`, `aeson`, `QuickCheck`, `hspec`. |
| 6 | **Build Systems & Package Management** | Cabal (`*.cabal`, `cabal.project.freeze`) and Stack with `ghc-options: -Wall -Wcompat -Werror -Widentities -Wpartial-fields`. |
| 7 | **Compiler / Interpreter Behavior** | GHC Core (`-ddump-simpl`) worker/wrapper transformation, unboxing (`{-# UNPACK #-}`), and rewrite rules (`RULES`) stream fusion. |
| 8 | **Debugging** | GHCi `:sprint` (inspect unevaluated thunks without forcing), `-prof -fprof-auto` heap retainer profiling (`+RTS -hc -l`), and `eventlog2html`. |
| 9 | **Security** | Ban partial functions (`head`, `tail`, `fromJust`, `read`); use `Data.List.NonEmpty` and `Text.Read.readMaybe`. |
| 10 | **Performance Optimization** | Use `Data.Text` / `Data.ByteString` instead of `[Char]` (`String` linked list), unboxed `Data.Vector.Unboxed`, and `foldl'`. |
| 11 | **Error Handling** | Pure `Either Err a` / `ExceptT` for domain errors and `Control.Exception.Safe.bracket` for asynchronous exception-safe resource cleanup. |
| 12 | **Testing Methodologies** | `QuickCheck` / `Hedgehog` property-based law verification (`Functor`, `Applicative`, `Monad` laws) and `tasty`/`hspec`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (GHC 9.4 / 9.6 / 9.8+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Haskell 2010 Foreign Function Interface (`foreign import ccall safe/unsafe`) with `Foreign.Ptr` and `Storable`. |
| 18 | **Common Engineering Mistakes** | Using lazy `foldl` or `Control.Monad.State.Lazy` (catastrophic thunk stack overflow), using `String` (`[Char]`) for I/O, and partial record fields in sum types. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/haskell-lazy-typelevel/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Haskell**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `GHCi `:sprint` (inspect unevaluated thunks without forcing), `-prof -fprof-auto` heap retainer profiling (`+RTS -hc -l`), and `eventlog2html`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Cabal (`*.cabal`, `cabal.project.freeze`) and Stack with `ghc-options: -Wall -Wcompat -Werror -Widentities -Wpartial-fields`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `Data.Text` / `Data.ByteString` instead of `[Char]` (`String` linked list), unboxed `Data.Vector.Unboxed`, and `foldl'`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Ban partial functions (`head`, `tail`, `fromJust`, `read`); use `Data.List.NonEmpty` and `Text.Read.readMaybe`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`QuickCheck` / `Hedgehog` property-based law verification (`Functor`, `Applicative`, `Monad` laws) and `tasty`/`hspec`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Haskell 2010 Foreign Function Interface (`foreign import ccall safe/unsafe`) with `Foreign.Ptr` and `Storable`.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
