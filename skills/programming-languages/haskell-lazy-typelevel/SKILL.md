---
name: haskell-lazy-typelevel
description: Architect, optimize, and verify Haskell systems using GHC2021, strict data fields (StrictData), foldl' space-leak prevention, GADTs/Type Families, Monad transformer stacks, Software Transactional Memory (STM), and QuickCheck.
allowed-tools: execute_bash view_file write_to_file
---

# Haskell (GHC 9.6/9.8+) Strictness Control, GADTs, Typeclasses, STM & Core Optimization

Architect, optimize, and verify Haskell systems using GHC2021, strict data fields (StrictData), foldl' space-leak prevention, GADTs/Type Families, Monad transformer stacks, Software Transactional Memory (STM), and QuickCheck.

## A. Identity

- **Skill Name**: `haskell-lazy-typelevel`
- **Domain**: `programming-languages`
- **Language / Representation**: **Haskell** (`Purely Functional Programming Language`)
- **Technical Relationship**: Purely functional, call-by-need (lazy) language compiled by GHC via System FC core IR with GADTs, Type Families, and STM.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Haskell**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Haskell 2010 Report, GHC2021 / GHC2024 Language Extensions (GHC 9.4 / 9.6 / 9.8+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Cabal (`*.cabal`, `cabal.project.freeze`) and Stack with `ghc-options: -Wall -Wcompat -Werror -Widentities -Wpartial-fields`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Haskell** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Haskell**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Haskell** (`StrictLedgerFold.hs`, `Cabal (`*.cabal`, `cabal.project.freeze`) and Stack with `ghc-options: -Wall -Wcompat -Werror -Widentities -Wpartial-fields`.`).

### Prerequisites

- Target language version (GHC 9.4 / 9.6 / 9.8+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Haskell** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (GHC 9.4 / 9.6 / 9.8+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (GHC generational copying/compact-region GC; eliminate space leaks from lazy thunks in long-lived state (`TVar`, `IORef`, `Map.Strict`).), type soundness limits (Hindley-Milner + System FC (`GADTs`, `TypeFamilies`, `DataKinds`, `RoleAnnotations`), `newtype` zero-cost wrappers (`GeneralizedNewtypeDeriving`), and total pattern matching (`-Wincomplete-patterns`).), and concurrency hazards (Lightweight green threads (`forkIO`), `async` structured concurrency (`withAsync`), and composable atomic `STM` transactions (`TVar`, `retry`, `orElse`).).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Haskell 2010 Report, GHC2021 / GHC2024 Language Extensions.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Call-by-need laziness by default (`Thunk` allocation); enforce strictness at accumulator boundaries via `BangPatterns` (`!`), `StrictData`, and `Data.List.foldl'`.
2. **Type System & Inference**: Hindley-Milner + System FC (`GADTs`, `TypeFamilies`, `DataKinds`, `RoleAnnotations`), `newtype` zero-cost wrappers (`GeneralizedNewtypeDeriving`), and total pattern matching (`-Wincomplete-patterns`).
3. **Memory Management**: GHC generational copying/compact-region GC; eliminate space leaks from lazy thunks in long-lived state (`TVar`, `IORef`, `Map.Strict`).
4. **Concurrency & Async Programming**: Lightweight green threads (`forkIO`), `async` structured concurrency (`withAsync`), and composable atomic `STM` transactions (`TVar`, `retry`, `orElse`).
5. **Standard Library & Ecosystem**: `base`, `text`, `bytestring`, `containers`, ` unordered-containers`, `vector`, `stm`, `aeson`, `QuickCheck`, `hspec`.
6. **Build Systems & Package Management**: Cabal (`*.cabal`, `cabal.project.freeze`) and Stack with `ghc-options: -Wall -Wcompat -Werror -Widentities -Wpartial-fields`.
7. **Compiler / Interpreter Behavior**: GHC Core (`-ddump-simpl`) worker/wrapper transformation, unboxing (`{-# UNPACK #-}`), and rewrite rules (`RULES`) stream fusion.
8. **Debugging & Observability**: GHCi `:sprint` (inspect unevaluated thunks without forcing), `-prof -fprof-auto` heap retainer profiling (`+RTS -hc -l`), and `eventlog2html`.
9. **Security Hardening**: Ban partial functions (`head`, `tail`, `fromJust`, `read`); use `Data.List.NonEmpty` and `Text.Read.readMaybe`.
10. **Performance Optimization**: Use `Data.Text` / `Data.ByteString` instead of `[Char]` (`String` linked list), unboxed `Data.Vector.Unboxed`, and `foldl'`.
11. **Error Handling Discipline**: Pure `Either Err a` / `ExceptT` for domain errors and `Control.Exception.Safe.bracket` for asynchronous exception-safe resource cleanup.
12. **Testing Methodologies**: `QuickCheck` / `Hedgehog` property-based law verification (`Functor`, `Applicative`, `Monad` laws) and `tasty`/`hspec`.
13. **Interoperability & Cross-Platform ABI**: Haskell 2010 Foreign Function Interface (`foreign import ccall safe/unsafe`) with `Foreign.Ptr` and `Storable`.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/haskell-lazy-typelevel/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (GHC 9.4 / 9.6 / 9.8+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Haskell**: Using lazy `foldl` or `Control.Monad.State.Lazy` (catastrophic thunk stack overflow), using `String` (`[Char]`) for I/O, and partial record fields in sum types.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
