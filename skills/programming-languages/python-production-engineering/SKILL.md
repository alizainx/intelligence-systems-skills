---
name: python-production-engineering
description: Design, refactor, profile, debug, and verify production Python 3.11+ software using PEP 484/695 strict static typing, structured asyncio TaskGroups, pyproject.toml packaging, CPython GIL/reference-counting internals, pytest, and C/PyO3 native extensions.
allowed-tools: execute_bash view_file write_to_file
---

# Python (3.11/3.12+) Type Checking, Asyncio, CPython Internals & Native Extensions

Design, refactor, profile, debug, and verify production Python 3.11+ software using PEP 484/695 strict static typing, structured asyncio TaskGroups, pyproject.toml packaging, CPython GIL/reference-counting internals, pytest, and C/PyO3 native extensions.

## A. Identity

- **Skill Name**: `python-production-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **Python** (`General-Purpose Programming Language`)
- **Technical Relationship**: High-level bytecode-interpreted language (CPython VM) with native C/Rust extension ABI (`PyObject*`, `PyO3`, `cffi`).
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Python**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Python 3.11 / 3.12 / 3.13 Language Reference, PEP 8, PEP 484, PEP 585, PEP 621 (Python 3.11 / 3.12 / 3.13)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``pyproject.toml` (PEP 517/621), `uv` / `pip-tools` / `poetry` hash-pinned lockfiles, and manylinux wheels.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Python** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Python**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Python** (`strict_async_rate_limiter.py`, ``pyproject.toml` (PEP 517/621), `uv` / `pip-tools` / `poetry` hash-pinned lockfiles, and manylinux wheels.`).

### Prerequisites

- Target language version (Python 3.11 / 3.12 / 3.13), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Python** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Python 3.11 / 3.12 / 3.13), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (CPython reference counting (`ob_refcnt`) + generational cyclic GC; avoid reference cycles with `__del__` and use `__slots__` / `memoryview` zero-copy buffers.), type soundness limits (`typing.Protocol`, `TypeVar`/`ParamSpec`, `TypedDict`, `@final`, and strict validation via `mypy --strict` / `pyright`.), and concurrency hazards (`asyncio.TaskGroup` structured concurrency, `multiprocessing.shared_memory` for CPU-bound work (bypassing GIL), and PEP 703 free-threaded awareness.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Python 3.11 / 3.12 / 3.13 Language Reference, PEP 8, PEP 484, PEP 585, PEP 621.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Structural pattern matching (`match`/`case`), `dataclass(frozen=True, slots=True)`, context managers (`with`/`async with`), and late-bound default closure hygiene.
2. **Type System & Inference**: `typing.Protocol`, `TypeVar`/`ParamSpec`, `TypedDict`, `@final`, and strict validation via `mypy --strict` / `pyright`.
3. **Memory Management**: CPython reference counting (`ob_refcnt`) + generational cyclic GC; avoid reference cycles with `__del__` and use `__slots__` / `memoryview` zero-copy buffers.
4. **Concurrency & Async Programming**: `asyncio.TaskGroup` structured concurrency, `multiprocessing.shared_memory` for CPU-bound work (bypassing GIL), and PEP 703 free-threaded awareness.
5. **Standard Library & Ecosystem**: `pytest`, `hypothesis`, `ruff`, `mypy`, `pydantic`, `cffi`, `PyO3`.
6. **Build Systems & Package Management**: `pyproject.toml` (PEP 517/621), `uv` / `pip-tools` / `poetry` hash-pinned lockfiles, and manylinux wheels.
7. **Compiler / Interpreter Behavior**: CPython 3.11+ adaptive specializing bytecode interpreter (`LOAD_ATTR` inline caches); inspect via `dis.dis`.
8. **Debugging & Observability**: `pdb`, `faulthandler`, `tracemalloc` heap snapshots, `cProfile`, and `py-spy` sampling profiler.
9. **Security Hardening**: Ban `eval`/`exec`, `pickle.loads` on untrusted bytes, and `subprocess.run(..., shell=True)`; use `secrets` for cryptographic tokens.
10. **Performance Optimization**: Vectorize numerical loops, preallocate `bytearray`/`memoryview`, use `collections.deque` for $O(1)$ FIFO, and offload tight loops to C/Rust extensions.
11. **Error Handling Discipline**: Chain exceptions explicitly (`raise DomainError(...) from exc`), never use bare `except:`, and preserve `asyncio.CancelledError` propagation.
12. **Testing Methodologies**: Deterministic `pytest` fixtures, `hypothesis` property-based testing, and AST static policy checks.
13. **Interoperability & Cross-Platform ABI**: `ctypes`, `cffi`, `PyO3` (Rust), and Python C-API (`PyArg_ParseTuple`, `Py_BEGIN_ALLOW_THREADS` GIL release).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/python-production-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Python 3.11 / 3.12 / 3.13), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Python**: Mutable default arguments (`def f(x=[])`), blocking the `asyncio` event loop with synchronous `requests`/`time.sleep`, and swallowing `CancelledError`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
