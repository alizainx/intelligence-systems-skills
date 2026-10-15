# Deep Engineering Reference: Python (3.11/3.12+) Type Checking, Asyncio, CPython Internals & Native Extensions (`python-production-engineering`)

- **Language / Representation**: **Python**
- **Taxonomic Classification**: `General-Purpose Programming Language`
- **Technical Relationship**: High-level bytecode-interpreted language (CPython VM) with native C/Rust extension ABI (`PyObject*`, `PyO3`, `cffi`).
- **Governing Standards & Versions**: Python 3.11 / 3.12 / 3.13 Language Reference, PEP 8, PEP 484, PEP 585, PEP 621 (Python 3.11 / 3.12 / 3.13)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **Python** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Structural pattern matching (`match`/`case`), `dataclass(frozen=True, slots=True)`, context managers (`with`/`async with`), and late-bound default closure hygiene. |
| 2 | **Type System & Inference** | `typing.Protocol`, `TypeVar`/`ParamSpec`, `TypedDict`, `@final`, and strict validation via `mypy --strict` / `pyright`. |
| 3 | **Memory Management** | CPython reference counting (`ob_refcnt`) + generational cyclic GC; avoid reference cycles with `__del__` and use `__slots__` / `memoryview` zero-copy buffers. |
| 4 | **Concurrency & Async Programming** | `asyncio.TaskGroup` structured concurrency, `multiprocessing.shared_memory` for CPU-bound work (bypassing GIL), and PEP 703 free-threaded awareness. |
| 5 | **Standard Library & Ecosystem** | `pytest`, `hypothesis`, `ruff`, `mypy`, `pydantic`, `cffi`, `PyO3`. |
| 6 | **Build Systems & Package Management** | `pyproject.toml` (PEP 517/621), `uv` / `pip-tools` / `poetry` hash-pinned lockfiles, and manylinux wheels. |
| 7 | **Compiler / Interpreter Behavior** | CPython 3.11+ adaptive specializing bytecode interpreter (`LOAD_ATTR` inline caches); inspect via `dis.dis`. |
| 8 | **Debugging** | `pdb`, `faulthandler`, `tracemalloc` heap snapshots, `cProfile`, and `py-spy` sampling profiler. |
| 9 | **Security** | Ban `eval`/`exec`, `pickle.loads` on untrusted bytes, and `subprocess.run(..., shell=True)`; use `secrets` for cryptographic tokens. |
| 10 | **Performance Optimization** | Vectorize numerical loops, preallocate `bytearray`/`memoryview`, use `collections.deque` for $O(1)$ FIFO, and offload tight loops to C/Rust extensions. |
| 11 | **Error Handling** | Chain exceptions explicitly (`raise DomainError(...) from exc`), never use bare `except:`, and preserve `asyncio.CancelledError` propagation. |
| 12 | **Testing Methodologies** | Deterministic `pytest` fixtures, `hypothesis` property-based testing, and AST static policy checks. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (Python 3.11 / 3.12 / 3.13); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | `ctypes`, `cffi`, `PyO3` (Rust), and Python C-API (`PyArg_ParseTuple`, `Py_BEGIN_ALLOW_THREADS` GIL release). |
| 18 | **Common Engineering Mistakes** | Mutable default arguments (`def f(x=[])`), blocking the `asyncio` event loop with synchronous `requests`/`time.sleep`, and swallowing `CancelledError`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/python-production-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **Python**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``pdb`, `faulthandler`, `tracemalloc` heap snapshots, `cProfile`, and `py-spy` sampling profiler.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``pyproject.toml` (PEP 517/621), `uv` / `pip-tools` / `poetry` hash-pinned lockfiles, and manylinux wheels.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Vectorize numerical loops, preallocate `bytearray`/`memoryview`, use `collections.deque` for $O(1)$ FIFO, and offload tight loops to C/Rust extensions.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Ban `eval`/`exec`, `pickle.loads` on untrusted bytes, and `subprocess.run(..., shell=True)`; use `secrets` for cryptographic tokens.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Deterministic `pytest` fixtures, `hypothesis` property-based testing, and AST static policy checks.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (`ctypes`, `cffi`, `PyO3` (Rust), and Python C-API (`PyArg_ParseTuple`, `Py_BEGIN_ALLOW_THREADS` GIL release).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
