# Deep Engineering Reference: Scala 3 (Dotty) Type-Level Engineering, Opaque Types, Given/Using & Effect Systems (`scala-functional-jvm`)

- **Language / Representation**: **Scala**
- **Taxonomic Classification**: `General-Purpose & Functional Programming Language`
- **Technical Relationship**: Type-safe functional and object-oriented language on the JVM/Native founded on Dependent Object Types (DOT calculus) in Scala 3.
- **Governing Standards & Versions**: Scala 3 Language Reference (DOT Calculus) (Scala 2.13 / Scala 3.3 LTS / 3.4+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Scala** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Scala 3 `enum` ADTs, `opaque type` zero-cost abstractions, `given`/`using` canonical typeclasses, and `@tailrec` verification. |
| 2 | **Type System & Inference** | Union (`A | B`) and intersection (`A & B`) types, match types, higher-kinded types (`F[_]`), and explicit nulls (`-Yexplicit-nulls`). |
| 3 | **Memory Management** | `opaque type` and `AnyVal` avoiding JVM wrapper allocations; structural sharing in immutable `Vector`/`Map`. |
| 4 | **Concurrency & Async Programming** | Fiber-based functional effect systems (Cats Effect `IO`, ZIO) with resource-safe `Resource.make` / `ZIO.acquireRelease`. |
| 5 | **Standard Library & Ecosystem** | Cats, Cats Effect, ZIO, FS2, Http4s, Circe, ScalaTest, MUnit, ScalaCheck. |
| 6 | **Build Systems & Package Management** | `sbt` (`build.sbt`), Mill, Scala CLI with `-Werror -Wunused:all -Wvalue-discard`. |
| 7 | **Compiler / Interpreter Behavior** | TASTy intermediate representation enabling binary compatibility across Scala 3 minor releases; specialization and tail-call elimination. |
| 8 | **Debugging** | Fiber dumps in Cats Effect / ZIO, JFR profiling, and `-Xprint:typer` phase inspection. |
| 9 | **Security** | Enforce total pattern matching (`-Werror` on non-exhaustive match) and refined/opaque validation at serialization boundaries. |
| 10 | **Performance Optimization** | Use `@tailrec` for stack-safe recursion, `IArray` for immutable unboxed arrays, and avoid closure allocations in hot loops. |
| 11 | **Error Handling** | Typed error channels (`Either[Err, A]`, `ZIO[R, E, A]`, `ValidatedNec[Err, A]`); ban `.get` on `Option`/`Try`. |
| 12 | **Testing Methodologies** | MUnit / ScalaTest + ScalaCheck property-based law verification. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Scala 2.13 / Scala 3.3 LTS / 3.4+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `scala.jdk.CollectionConverters` and `@static` methods for zero-friction Java interop. |
| 18 | **Common Engineering Mistakes** | Calling `Option.get` or `Await.result` blocking thread pools, implicit ambiguity in Scala 2, and accidental boxing in generic collections. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/scala-functional-jvm/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Scala**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `Fiber dumps in Cats Effect / ZIO, JFR profiling, and `-Xprint:typer` phase inspection.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``sbt` (`build.sbt`), Mill, Scala CLI with `-Werror -Wunused:all -Wvalue-discard`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Use `@tailrec` for stack-safe recursion, `IArray` for immutable unboxed arrays, and avoid closure allocations in hot loops.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Enforce total pattern matching (`-Werror` on non-exhaustive match) and refined/opaque validation at serialization boundaries.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (MUnit / ScalaTest + ScalaCheck property-based law verification.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`scala.jdk.CollectionConverters` and `@static` methods for zero-friction Java interop.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
