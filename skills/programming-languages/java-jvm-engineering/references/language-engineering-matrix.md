# Deep Engineering Reference: Java (Java 17/21 LTS) JVM Internals, JMM Concurrency, Virtual Threads & Panama FFI (`java-jvm-engineering`)

- **Language / Representation**: **Java**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: Primary managed language of the Java Virtual Machine (JVM) governed by the Java Language Specification (JLS) and Java Memory Model (JMM).
- **Governing Standards & Versions**: Java Language Specification (JLS SE 21), JVM Specification (JVMS SE 21) (Java 17 LTS / Java 21 LTS)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Java** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Immutable `record` types, `sealed interface` with exhaustive `switch` pattern matching, and `try-with-resources` (`AutoCloseable`). |
| 2 | **Type System & Inference** | Reified arrays vs type-erased generics (`List<T>`), bounded wildcards (`? extends T` PECS), and `@NullMarked` (JSpecify) nullness annotations. |
| 3 | **Memory Management** | JVM heap generations, Escape Analysis scalar replacement, off-heap `Arena` (`java.lang.foreign.MemorySegment`), and low-pause ZGC/G1GC. |
| 4 | **Concurrency & Async Programming** | Java Memory Model (`volatile` acquire/release, `VarHandle`), `CompletableFuture`, `StructuredTaskScope`, and Virtual Threads (`Executors.newVirtualThreadPerTaskExecutor()`). |
| 5 | **Standard Library & Ecosystem** | JDK standard library (`java.util.concurrent`, `java.nio`), JUnit 5, JMH (Java Microbenchmark Harness), Jackson, Netty. |
| 6 | **Build Systems & Package Management** | Maven (`pom.xml` with Enforcer plugin) and Gradle (`build.gradle.kts` with version catalogs and reproducible lockfiles). |
| 7 | **Compiler / Interpreter Behavior** | `javac -Xlint:all -Werror` bytecode emission followed by HotSpot C1/C2 tiered JIT compilation (`-XX:+PrintCompilation`, inline thresholds). |
| 8 | **Debugging** | JDK Flight Recorder (`jfr`), `jcmd`, `jstack`, Async-Profiler flamegraphs, and JDWP debugger. |
| 9 | **Security** | Prevent JNDI/deserialization RCE (`ObjectInputFilter`), SQL injection (`PreparedStatement`), and XXE in XML parsers. |
| 10 | **Performance Optimization** | Avoid autoboxing in hot paths (`IntStream`, primitive collections), prevent Virtual Thread pinning inside `synchronized` blocks (use `ReentrantLock`), and benchmark with JMH. |
| 11 | **Error Handling** | Checked exceptions for recoverable protocol faults, unchecked domain exceptions with context, never swallow `InterruptedException` (restore `Thread.currentThread().interrupt()`). |
| 12 | **Testing Methodologies** | JUnit 5 parameterized tests, `jqwik` property tests, and Testcontainers integration harnesses. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Java 17 LTS / Java 21 LTS); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Project Panama Foreign Function & Memory (FFM) API (`Linker.nativeLinker()`, `MemorySegment`) replacing unsafe JNI. |
| 18 | **Common Engineering Mistakes** | Broken `equals`/`hashCode` contracts on mutable keys, double-checked locking without `volatile`, and pinning carrier threads in Virtual Threads. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/java-jvm-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Java**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `JDK Flight Recorder (`jfr`), `jcmd`, `jstack`, Async-Profiler flamegraphs, and JDWP debugger.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Maven (`pom.xml` with Enforcer plugin) and Gradle (`build.gradle.kts` with version catalogs and reproducible lockfiles).`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Avoid autoboxing in hot paths (`IntStream`, primitive collections), prevent Virtual Thread pinning inside `synchronized` blocks (use `ReentrantLock`), and benchmark with JMH.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Prevent JNDI/deserialization RCE (`ObjectInputFilter`), SQL injection (`PreparedStatement`), and XXE in XML parsers.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (JUnit 5 parameterized tests, `jqwik` property tests, and Testcontainers integration harnesses.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Project Panama Foreign Function & Memory (FFM) API (`Linker.nativeLinker()`, `MemorySegment`) replacing unsafe JNI.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
