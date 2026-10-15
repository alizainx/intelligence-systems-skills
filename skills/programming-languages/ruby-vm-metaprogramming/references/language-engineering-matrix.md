# Deep Engineering Reference: Ruby (3.2/3.3+ YJIT) Frozen String Literals, RBS/Sorbet Types, Ractors & Metaprogramming Safety (`ruby-vm-metaprogramming`)

- **Language / Representation**: **Ruby**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: Dynamic object-oriented language running on CRuby (YARV bytecode VM + YJIT) with RBS/Sorbet static type checking and Ractor concurrency.
- **Governing Standards & Versions**: ISO/IEC 30170 Ruby Language Specification, Ruby 3.3 YARV/YJIT Reference (Ruby 3.2 / Ruby 3.3+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Ruby** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Mandatory `# frozen_string_literal: true` magic comment, `Data.define` immutable value structs (Ruby 3.2+), rightward/pattern matching (`case/in`). |
| 2 | **Type System & Inference** | Gradual static typing via RBS type signatures (`sig/*.rbs` + Steep) or Sorbet (`# typed: strict`, `T::Struct`). |
| 3 | **Memory Management** | CRuby Variable Width Allocation (VWA) heap pages and generational incremental GC; avoid retaining large strings/objects in class variables (`@@var`). |
| 4 | **Concurrency & Async Programming** | GVL (Global VM Lock) in standard threads; `Fiber.set_scheduler` for non-blocking I/O, and share-nothing `Ractor` actors for true multi-core parallelism. |
| 5 | **Standard Library & Ecosystem** | Bundler, RSpec, Minitest, RuboCop, Sidekiq, Rack, Zeitwerk. |
| 6 | **Build Systems & Package Management** | `Gemfile` + `Gemfile.lock` (`bundle config set --local deployment true`), `bundle audit`. |
| 7 | **Compiler / Interpreter Behavior** | YARV bytecode + Rust-based **YJIT** (`RUBY_YJIT_ENABLE=1`) basic-block versioning compiler; maintain consistent object shapes (initialize all `@ivars` in `initialize`). |
| 8 | **Debugging** | `debug` gem (`rdbg`), `ObjectSpace.dump_all`, `stackprof`, and `Vernier` profiler. |
| 9 | **Security** | Never call `Kernel#open` on user strings (command injection if leading `|`; use `File.open`), ban `Marshal.load`/`YAML.unsafe_load` on untrusted data, and prefer `public_send` over `send`. |
| 10 | **Performance Optimization** | Avoid `define_method` or singleton class mutations at runtime (invalidates YJIT inline caches) and use `String#freeze`. |
| 11 | **Error Handling** | Rescue `StandardError` (never bare `rescue Exception`, which traps `SignalException` and `SystemExit`). |
| 12 | **Testing Methodologies** | RSpec / Minitest suites with `RUBYOPT="-w"` warning enforcement. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Ruby 3.2 / Ruby 3.3+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | C extensions (`Rice` / `rb_define_method`), `Fiddle` (`libffi`), and `magnus` (Rust FFI). |
| 18 | **Common Engineering Mistakes** | Rescuing `Exception`, mutating shared constants across threads/Ractors, and using `send(params[:action])` allowing private method invocation. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/ruby-vm-metaprogramming/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Ruby**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``debug` gem (`rdbg`), `ObjectSpace.dump_all`, `stackprof`, and `Vernier` profiler.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``Gemfile` + `Gemfile.lock` (`bundle config set --local deployment true`), `bundle audit`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Avoid `define_method` or singleton class mutations at runtime (invalidates YJIT inline caches) and use `String#freeze`.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Never call `Kernel#open` on user strings (command injection if leading `|`; use `File.open`), ban `Marshal.load`/`YAML.unsafe_load` on untrusted data, and prefer `public_send` over `send`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (RSpec / Minitest suites with `RUBYOPT="-w"` warning enforcement.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (C extensions (`Rice` / `rb_define_method`), `Fiddle` (`libffi`), and `magnus` (Rust FFI).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
