---
name: cuda-cpp-warp-simt
description: Design, optimize, debug, and verify CUDA C++ GPU kernels using coalesced 128-byte global memory transactions, 32-bank conflict-free shared memory padding, __shfl_down_sync warp reductions, cooperative groups, and asynchronous CUDA Streams.
allowed-tools: execute_bash view_file write_to_file
---

# CUDA C++ (CUDA 12+) Coalesced Memory, 32-Bank Shared Memory, Warp Primitives & Streams

Design, optimize, debug, and verify CUDA C++ GPU kernels using coalesced 128-byte global memory transactions, 32-bank conflict-free shared memory padding, __shfl_down_sync warp reductions, cooperative groups, and asynchronous CUDA Streams.

## A. Identity

- **Skill Name**: `cuda-cpp-warp-simt`
- **Domain**: `programming-languages`
- **Language / Representation**: **CUDA C++** (`GPU Parallel Compute Language (SIMT Extension of C++)`)
- **Technical Relationship**: NVIDIA SIMT heterogeneous parallel programming extension of ISO C++ (`__global__`, `__device__`, `__shared__`) compiled by `nvcc` / `clang --cuda-gpu-arch`.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **CUDA C++**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: NVIDIA CUDA C++ Programming Guide (CUDA 12.x), PTX ISA (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`CMake (`LANGUAGES CUDA`, `CMAKE_CUDA_ARCHITECTURES "80;86;90"`), `nvcc -lineinfo --use_fast_math`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **CUDA C++** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **CUDA C++**.

### Technical Triggers

- Files, build manifests, or prompts targeting **CUDA C++** (`padded_transpose_kernel.cu`, `CMake (`LANGUAGES CUDA`, `CMAKE_CUDA_ARCHITECTURES "80;86;90"`), `nvcc -lineinfo --use_fast_math`.`).

### Prerequisites

- Target language version (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **CUDA C++** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Global DRAM (coalesced across 32 threads in a warp), per-SM Shared Memory (`__shared__`, 32 banks of 4 bytes each), Constant/Texture caches, and `cudaMallocAsync` stream-ordered pools.), type soundness limits (Vector alignment types (`float4`, `int4` 16-byte vectorized loads), `__half`/`__nv_bfloat16`, and `__restrict__` pointer aliasing promises.), and concurrency hazards (`__syncthreads()` (must be reached by all threads in block-never inside divergent conditional branches!), `__syncwarp(mask)`, `cooperative_groups`, and `cuda::atomic`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce NVIDIA CUDA C++ Programming Guide (CUDA 12.x), PTX ISA.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Execution space qualifiers (`__global__`, `__device__`, `__host__`), launch configuration `<<<grid, block, shmem, stream>>>`, and 32-thread Warp SIMT execution.
2. **Type System & Inference**: Vector alignment types (`float4`, `int4` 16-byte vectorized loads), `__half`/`__nv_bfloat16`, and `__restrict__` pointer aliasing promises.
3. **Memory Management**: Global DRAM (coalesced across 32 threads in a warp), per-SM Shared Memory (`__shared__`, 32 banks of 4 bytes each), Constant/Texture caches, and `cudaMallocAsync` stream-ordered pools.
4. **Concurrency & Async Programming**: `__syncthreads()` (must be reached by all threads in block-never inside divergent conditional branches!), `__syncwarp(mask)`, `cooperative_groups`, and `cuda::atomic`.
5. **Standard Library & Ecosystem**: cuBLAS, cuDNN, Thrust, CUB (`cub::BlockReduce`), Cutlass, Nsight Compute (`ncu`), Nsight Systems (`nsys`).
6. **Build Systems & Package Management**: CMake (`LANGUAGES CUDA`, `CMAKE_CUDA_ARCHITECTURES "80;86;90"`), `nvcc -lineinfo --use_fast_math`.
7. **Compiler / Interpreter Behavior**: Splits host C++ and device PTX/SASS compilation; inspect register spilling and local-memory traffic via `nvcc --ptxas-options=-v`.
8. **Debugging & Observability**: `compute-sanitizer --tool memcheck|racecheck|initcheck|synccheck` and `cuda-gdb`.
9. **Security Hardening**: Guard every thread index against problem bounds (`if (idx < N)`) before reading or writing global memory.
10. **Performance Optimization**: Eliminate 32-way shared-memory bank conflicts by padding 2D tiles (`__shared__ float tile[32][33]`), use `__shfl_down_sync(0xffffffffu, val, offset)` for warp reductions, and overlap H2D/D2H copies via pinned host memory (`cudaMallocHost`) + streams.
11. **Error Handling Discipline**: Wrap every CUDA runtime call and follow kernel launches with `cudaGetLastError()` checking (`CUDA_CHECK(err)`).
12. **Testing Methodologies**: Verify shared-memory bank-conflict-free stride geometry and compare GPU output against an IEEE 754 `double` CPU reference.
13. **Interoperability & Cross-Platform ABI**: C/C++ host ABI, PyTorch custom C++/CUDA extensions, and DLPack zero-copy tensor sharing.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/cuda-cpp-warp-simt/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in CUDA C++**: Calling `__syncthreads()` inside a thread-divergent `if (threadIdx.x < 16)` branch (deadlocks SM!), unpadded `[32][32]` shared-memory column access causing 32-way bank conflicts, and ignoring asynchronous kernel launch errors.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
