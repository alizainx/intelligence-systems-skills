---
name: lua-c-api-embedding
description: Embed, audit, optimize, and verify Lua 5.4 and LuaJIT scripts and C-API host bindings with strict virtual-stack balance, <close> to-be-closed variables, _ENV sandboxing, custom allocators, and LuaJIT FFI.
allowed-tools: execute_bash view_file write_to_file
---

# Lua (5.4 / LuaJIT) C-API Stack Discipline, Metatables, Coroutines & Sandboxed Embedding

Embed, audit, optimize, and verify Lua 5.4 and LuaJIT scripts and C-API host bindings with strict virtual-stack balance, <close> to-be-closed variables, _ENV sandboxing, custom allocators, and LuaJIT FFI.

## A. Identity

- **Skill Name**: `lua-c-api-embedding`
- **Domain**: `programming-languages`
- **Language / Representation**: **Lua** (`Embeddable Scripting & Extension Language`)
- **Technical Relationship**: Register-based bytecode scripting language (Lua 5.4 / LuaJIT 2.1) designed specifically for deterministic embedding inside C/C++/Rust hosts.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Lua**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Lua 5.4 Reference Manual, LuaJIT 2.1 Reference (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``luacheck --no-global`, `rockspec` manifests.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Lua** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Lua**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Lua** (`sandboxed_eval.lua`, ``luacheck --no-global`, `rockspec` manifests.`).

### Prerequisites

- Target language version (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Lua** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Lua 5.4 generational + incremental GC (`collectgarbage("generational")`) and custom `lua_Alloc` host memory caps to prevent OOM DoS.), type soundness limits (8 basic types (`nil`, `boolean`, `number`, `string`, `function`, `userdata`, `thread`, `table`) + metatable prototypes (`__index`, `__newindex`).), and concurrency hazards (Asymmetric stackful coroutines (`coroutine.create`, `resume`, `yield`) and separate `lua_State` per OS thread.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Lua 5.4 Reference Manual, LuaJIT 2.1 Reference.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: 1-based indexing (`#t`), explicit `local` scoping by default, Lua 5.4 `<const>` and `<close>` (`__close` deterministic RAII metamethod), and 64-bit integer subtype vs float.
2. **Type System & Inference**: 8 basic types (`nil`, `boolean`, `number`, `string`, `function`, `userdata`, `thread`, `table`) + metatable prototypes (`__index`, `__newindex`).
3. **Memory Management**: Lua 5.4 generational + incremental GC (`collectgarbage("generational")`) and custom `lua_Alloc` host memory caps to prevent OOM DoS.
4. **Concurrency & Async Programming**: Asymmetric stackful coroutines (`coroutine.create`, `resume`, `yield`) and separate `lua_State` per OS thread.
5. **Standard Library & Ecosystem**: LuaRocks, `luacheck`, `stylua`, `busted` test framework, OpenResty / Neovim / Redis / game-engine runtimes.
6. **Build Systems & Package Management**: `luacheck --no-global`, `rockspec` manifests.
7. **Compiler / Interpreter Behavior**: Register-based VM in Lua 5.4; trace compiler in LuaJIT (avoid NYI builtins that abort JIT traces).
8. **Debugging & Observability**: `debug.traceback`, `lua_sethook` instruction/memory quota hooks for terminating runaway guest scripts.
9. **Security Hardening**: Sandbox untrusted scripts by replacing `_ENV` with a whitelist table, stripping `os.execute`/`io.popen`/`debug`/`package.loadlib`, and passing mode `"t"` to `load()` (blocking malicious binary bytecode).
10. **Performance Optimization**: Cache globals into `local` variables (`local sin = math.sin`), preallocate array-part vs hash-part tables, and avoid table allocations in LuaJIT trace loops.
11. **Error Handling Discipline**: Protected calls via `pcall` / `xpcall(fn, debug.traceback)` in Lua and `lua_pcall` in C host code (never `lua_call` on untrusted scripts).
12. **Testing Methodologies**: `busted` unit tests and C-API stack-height invariant assertions (`assert(lua_gettop(L) == top_before)`).
13. **Interoperability & Cross-Platform ABI**: C-API virtual stack (`lua_push*`, `luaL_check*`, full `userdata` with `__gc` metatables) and LuaJIT `ffi.cdef`.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/lua-c-api-embedding/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Lua 5.1 (LuaJIT 2.1) / Lua 5.3 / Lua 5.4), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Lua**: Accidental globals from missing `local`, C-API stack overflow/imbalance (`lua_checkstack`), and `#t` undefined length on sparse tables with `nil` holes.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
