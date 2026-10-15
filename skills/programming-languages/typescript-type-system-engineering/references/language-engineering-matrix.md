# Deep Engineering Reference: TypeScript (5.4/5.6+) Strict Soundness, Branded Types, Variance & Runtime Boundary Validation (`typescript-type-system-engineering`)

- **Language / Representation**: **TypeScript**
- **Taxonomic Classification**: `General-Purpose Programming Language (Statically Typed Superset of JavaScript)`
- **Technical Relationship**: Structural static type system and compiler (`tsc`) erasing to JavaScript; requires runtime validation at untrusted I/O boundaries because types are erased at runtime.
- **Governing Standards & Versions**: TypeScript 5.x Handbook & Compiler Specification, ECMAScript Modules (TypeScript 5.0 / 5.4 / 5.6+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **TypeScript** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `satisfies` operator, `as const` literal narrowing, `using` explicit resource management (ES Decorators & Disposable), and `import type`. |
| 2 | **Type System & Inference** | Structural subtyping, conditional & mapped types, template literal types, `in`/`out` variance annotations, and opaque Branded Types (`T & { readonly __brand: unique symbol }`). |
| 3 | **Memory Management** | Understand that all TypeScript types are completely erased at runtime; enforce V8 monomorphic shapes and `Symbol.dispose` cleanup. |
| 4 | **Concurrency & Async Programming** | Typed `Promise<Result<T, E>>`, `AbortSignal` propagation, and typed Worker message channels. |
| 5 | **Standard Library & Ecosystem** | Zod / Valibot runtime schema validators, `typescript-eslint`, Vitest, `tsx`. |
| 6 | **Build Systems & Package Management** | `tsconfig.json` with `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"verbatimModuleSyntax": true`. |
| 7 | **Compiler / Interpreter Behavior** | Type erasure pitfalls: `as SomeType` assertions perform zero runtime checks; index signatures `arr[i]` return `T | undefined` only when `noUncheckedIndexedAccess` is enabled. |
| 8 | **Debugging** | Source maps (`--sourceMap`), `tsc --noEmit --extendedDiagnostics` typecheck profiling, and `--generateTrace`. |
| 9 | **Security** | Ban `any` (`@typescript-eslint/no-explicit-any`); always parse `JSON.parse()` as `unknown` and narrow via runtime type predicates (`val is Schema`). |
| 10 | **Performance Optimization** | Avoid deeply recursive conditional types that blow up `tsc` instantiation depth; use explicit return types on exported functions for `.d.ts` isolated declarations. |
| 11 | **Error Handling** | Use `useUnknownInCatchVariables` (`catch (err: unknown)`) and discriminated `Result<T, E>` unions with `assertNever(x: never): never`. |
| 12 | **Testing Methodologies** | Compile-time `@ts-expect-error` type tests (`expectTypeOf`) + runtime Node.js V8 execution tests. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (TypeScript 5.0 / 5.4 / 5.6+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Ambient `.d.ts` declarations for JS/Wasm/N-API modules with runtime wrapper validation. |
| 18 | **Common Engineering Mistakes** | Trusting `JSON.parse(str) as User` without runtime validation, bivariant method syntax on interfaces (`fn(x: T): void` instead of `fn: (x: T) => void`), and unchecked array indexing. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/typescript-type-system-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **TypeScript**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Source maps (`--sourceMap`), `tsc --noEmit --extendedDiagnostics` typecheck profiling, and `--generateTrace`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``tsconfig.json` with `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"verbatimModuleSyntax": true`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Avoid deeply recursive conditional types that blow up `tsc` instantiation depth; use explicit return types on exported functions for `.d.ts` isolated declarations.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Ban `any` (`@typescript-eslint/no-explicit-any`); always parse `JSON.parse()` as `unknown` and narrow via runtime type predicates (`val is Schema`).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Compile-time `@ts-expect-error` type tests (`expectTypeOf`) + runtime Node.js V8 execution tests.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Ambient `.d.ts` declarations for JS/Wasm/N-API modules with runtime wrapper validation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
