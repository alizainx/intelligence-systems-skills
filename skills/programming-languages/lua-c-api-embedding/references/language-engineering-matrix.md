# Deep Engineering Reference: Lua (5.4 / LuaJIT) C-API Stack Discipline, Metatables, Coroutines & Sandboxed Embedding (`lua-c-api-embedding`)

- **Language / Representation**: **Lua**
- **Taxonomic Classification**: `Embeddable Scripting & Extension Language`
- **Technical Relationship**: Register-based bytecode scripting language (Lua 5.4 / LuaJIT 2.1) designed specifically for deterministic embedding inside C/C++/Rust hosts.
- **Governing Standards & Versions**: Lua 5.4 Reference Manual, LuaJIT 2.1 Reference (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Lua** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | 1-based indexing (`#t`), explicit `local` scoping by default, Lua 5.4 `<const>` and `<close>` (`__close` deterministic RAII metamethod), and 64-bit integer subtype vs float. |
| 2 | **Type System & Inference** | 8 basic types (`nil`, `boolean`, `number`, `string`, `function`, `userdata`, `thread`, `table`) + metatable prototypes (`__index`, `__newindex`). |
| 3 | **Memory Management** | Lua 5.4 generational + incremental GC (`collectgarbage("generational")`) and custom `lua_Alloc` host memory caps to prevent OOM DoS. |
| 4 | **Concurrency & Async Programming** | Asymmetric stackful coroutines (`coroutine.create`, `resume`, `yield`) and separate `lua_State` per OS thread. |
| 5 | **Standard Library & Ecosystem** | LuaRocks, `luacheck`, `stylua`, `busted` test framework, OpenResty / Neovim / Redis / game-engine runtimes. |
| 6 | **Build Systems & Package Management** | `luacheck --no-global`, `rockspec` manifests. |
| 7 | **Compiler / Interpreter Behavior** | Register-based VM in Lua 5.4; trace compiler in LuaJIT (avoid NYI builtins that abort JIT traces). |
| 8 | **Debugging** | `debug.traceback`, `lua_sethook` instruction/memory quota hooks for terminating runaway guest scripts. |
| 9 | **Security** | Sandbox untrusted scripts by replacing `_ENV` with a whitelist table, stripping `os.execute`/`io.popen`/`debug`/`package.loadlib`, and passing mode `"t"` to `load()` (blocking malicious binary bytecode). |
| 10 | **Performance Optimization** | Cache globals into `local` variables (`local sin = math.sin`), preallocate array-part vs hash-part tables, and avoid table allocations in LuaJIT trace loops. |
| 11 | **Error Handling** | Protected calls via `pcall` / `xpcall(fn, debug.traceback)` in Lua and `lua_pcall` in C host code (never `lua_call` on untrusted scripts). |
| 12 | **Testing Methodologies** | `busted` unit tests and C-API stack-height invariant assertions (`assert(lua_gettop(L) == top_before)`). |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | C-API virtual stack (`lua_push*`, `luaL_check*`, full `userdata` with `__gc` metatables) and LuaJIT `ffi.cdef`. |
| 18 | **Common Engineering Mistakes** | Accidental globals from missing `local`, C-API stack overflow/imbalance (`lua_checkstack`), and `#t` undefined length on sparse tables with `nil` holes. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/lua-c-api-embedding/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Lua**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``debug.traceback`, `lua_sethook` instruction/memory quota hooks for terminating runaway guest scripts.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``luacheck --no-global`, `rockspec` manifests.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Cache globals into `local` variables (`local sin = math.sin`), preallocate array-part vs hash-part tables, and avoid table allocations in LuaJIT trace loops.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Sandbox untrusted scripts by replacing `_ENV` with a whitelist table, stripping `os.execute`/`io.popen`/`debug`/`package.loadlib`, and passing mode `"t"` to `load()` (blocking malicious binary bytecode).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (`busted` unit tests and C-API stack-height invariant assertions (`assert(lua_gettop(L) == top_before)`).).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (C-API virtual stack (`lua_push*`, `luaL_check*`, full `userdata` with `__gc` metatables) and LuaJIT `ffi.cdef`.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
