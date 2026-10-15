# Deep Engineering Reference: Modern Perl 5 (v5.36+) Strict/Warnings, Lexical Sub Signatures, Taint Mode & IPC Safety (`perl-strict-text-systems`)

- **Language / Representation**: **Perl**
- **Taxonomic Classification**: `General-Purpose & Systems Automation Language`
- **Technical Relationship**: Rich text-processing and UNIX systems programming language (Perl 5.36+) natively installed on POSIX/Linux hosts.
- **Governing Standards & Versions**: Perl 5.36 / 5.38 Documentation (perlfunc, perlsec, perlre) (Perl v5.32 / v5.36 / v5.38+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Perl** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `use v5.36;` (enables `strict`, `warnings`, `signatures`, `isa`, and disables indirect object syntax), lexical filehandles (`open my $fh, '<:encoding(UTF-8)', $path`). |
| 2 | **Type System & Inference** | Sigil context sensitivity (`$scalar`, `@array`, `%hash`), `builtin::blessed` / `$obj isa Class`, and Type::Tiny runtime checks. |
| 3 | **Memory Management** | Deterministic reference counting; break circular object references via `Scalar::Util::weaken($self->{parent})`. |
| 4 | **Concurrency & Async Programming** | Prefer prefork worker processes (`Parallel::ForkManager`) or event loops (`Mojo::IOLoop`, `IO::Async`) over heavyweight interpreter threads (`ithreads`). |
| 5 | **Standard Library & Ecosystem** | CPAN, `cpanm`, `Carton` (`cpanfile.snapshot`), `Perl::Critic`, `Perl::Tidy`, `Test2::V0`. |
| 6 | **Build Systems & Package Management** | `cpanfile` + `cpanfile.snapshot`, `perl -c -Mstrict -Mwarnings` syntax check. |
| 7 | **Compiler / Interpreter Behavior** | Two-phase compile (`BEGIN` blocks) + opcode tree execution (`perl -MO=Concise,func`). |
| 8 | **Debugging** | `perl -d`, `Carp::confess` stack traces, and `Devel::NYTProf` line/subroutine profiler. |
| 9 | **Security** | Taint mode (`perl -T`), mandatory 3-argument `open(my $fh, '<', $file)` (preventing 2-arg pipe injection), and list-form `system($prog, @args)`. |
| 10 | **Performance Optimization** | Precompile regular expressions with `qr//`, avoid `$&`/`$`/`$'` match variables on older Perls, and pack binary records with `pack`/`unpack`. |
| 11 | **Error Handling** | `autodie` for lexical system call error checking and structured `try`/`catch` (`use feature 'try'` in 5.36+). |
| 12 | **Testing Methodologies** | Native `Test::More` / `Test2::V0` TAP suites executed via `prove` or `perl`. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Perl v5.32 / v5.36 / v5.38+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | XS C extensions and `FFI::Platypus` (`libffi`) bindings. |
| 18 | **Common Engineering Mistakes** | 2-argument `open(FH, $user_path)` RCE vulnerability, string `eval $expr` instead of block `eval { ... }`, and accidental list-context vs scalar-context bugs. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/perl-strict-text-systems/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Perl**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``perl -d`, `Carp::confess` stack traces, and `Devel::NYTProf` line/subroutine profiler.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``cpanfile` + `cpanfile.snapshot`, `perl -c -Mstrict -Mwarnings` syntax check.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Precompile regular expressions with `qr//`, avoid `$&`/`$`/`$'` match variables on older Perls, and pack binary records with `pack`/`unpack`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Taint mode (`perl -T`), mandatory 3-argument `open(my $fh, '<', $file)` (preventing 2-arg pipe injection), and list-form `system($prog, @args)`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Native `Test::More` / `Test2::V0` TAP suites executed via `prove` or `perl`.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (XS C extensions and `FFI::Platypus` (`libffi`) bindings.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
