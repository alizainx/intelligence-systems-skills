---
name: typescript-type-system-engineering
description: Design, refactor, and verify TypeScript 5.x systems with strict compiler flags (noUncheckedIndexedAccess, exactOptionalPropertyTypes), discriminated unions, assertNever exhaustiveness, branded nominal types, and runtime schema guards.
allowed-tools: execute_bash view_file write_to_file
---

# TypeScript (5.4/5.6+) Strict Soundness, Branded Types, Variance & Runtime Boundary Validation

Design, refactor, and verify TypeScript 5.x systems with strict compiler flags (noUncheckedIndexedAccess, exactOptionalPropertyTypes), discriminated unions, assertNever exhaustiveness, branded nominal types, and runtime schema guards.

## A. Identity

- **Skill Name**: `typescript-type-system-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **TypeScript** (`General-Purpose Programming Language (Statically Typed Superset of JavaScript)`)
- **Technical Relationship**: Structural static type system and compiler (`tsc`) erasing to JavaScript; requires runtime validation at untrusted I/O boundaries because types are erased at runtime.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **TypeScript**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: TypeScript 5.x Handbook & Compiler Specification, ECMAScript Modules (TypeScript 5.0 / 5.4 / 5.6+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``tsconfig.json` with `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"verbatimModuleSyntax": true`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **TypeScript** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **TypeScript**.

### Technical Triggers

- Files, build manifests, or prompts targeting **TypeScript** (`branded_type_guard.mjs`, ``tsconfig.json` with `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"verbatimModuleSyntax": true`.`).

### Prerequisites

- Target language version (TypeScript 5.0 / 5.4 / 5.6+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **TypeScript** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (TypeScript 5.0 / 5.4 / 5.6+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Understand that all TypeScript types are completely erased at runtime; enforce V8 monomorphic shapes and `Symbol.dispose` cleanup.), type soundness limits (Structural subtyping, conditional & mapped types, template literal types, `in`/`out` variance annotations, and opaque Branded Types (`T & { readonly __brand: unique symbol }`).), and concurrency hazards (Typed `Promise<Result<T, E>>`, `AbortSignal` propagation, and typed Worker message channels.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce TypeScript 5.x Handbook & Compiler Specification, ECMAScript Modules.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `satisfies` operator, `as const` literal narrowing, `using` explicit resource management (ES Decorators & Disposable), and `import type`.
2. **Type System & Inference**: Structural subtyping, conditional & mapped types, template literal types, `in`/`out` variance annotations, and opaque Branded Types (`T & { readonly __brand: unique symbol }`).
3. **Memory Management**: Understand that all TypeScript types are completely erased at runtime; enforce V8 monomorphic shapes and `Symbol.dispose` cleanup.
4. **Concurrency & Async Programming**: Typed `Promise<Result<T, E>>`, `AbortSignal` propagation, and typed Worker message channels.
5. **Standard Library & Ecosystem**: Zod / Valibot runtime schema validators, `typescript-eslint`, Vitest, `tsx`.
6. **Build Systems & Package Management**: `tsconfig.json` with `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"verbatimModuleSyntax": true`.
7. **Compiler / Interpreter Behavior**: Type erasure pitfalls: `as SomeType` assertions perform zero runtime checks; index signatures `arr[i]` return `T | undefined` only when `noUncheckedIndexedAccess` is enabled.
8. **Debugging & Observability**: Source maps (`--sourceMap`), `tsc --noEmit --extendedDiagnostics` typecheck profiling, and `--generateTrace`.
9. **Security Hardening**: Ban `any` (`@typescript-eslint/no-explicit-any`); always parse `JSON.parse()` as `unknown` and narrow via runtime type predicates (`val is Schema`).
10. **Performance Optimization**: Avoid deeply recursive conditional types that blow up `tsc` instantiation depth; use explicit return types on exported functions for `.d.ts` isolated declarations.
11. **Error Handling Discipline**: Use `useUnknownInCatchVariables` (`catch (err: unknown)`) and discriminated `Result<T, E>` unions with `assertNever(x: never): never`.
12. **Testing Methodologies**: Compile-time `@ts-expect-error` type tests (`expectTypeOf`) + runtime Node.js V8 execution tests.
13. **Interoperability & Cross-Platform ABI**: Ambient `.d.ts` declarations for JS/Wasm/N-API modules with runtime wrapper validation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/typescript-type-system-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (TypeScript 5.0 / 5.4 / 5.6+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in TypeScript**: Trusting `JSON.parse(str) as User` without runtime validation, bivariant method syntax on interfaces (`fn(x: T): void` instead of `fn: (x: T) => void`), and unchecked array indexing.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
