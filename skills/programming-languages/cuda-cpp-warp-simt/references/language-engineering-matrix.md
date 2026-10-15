# Deep Engineering Reference: CUDA C++ (CUDA 12+) Coalesced Memory, 32-Bank Shared Memory, Warp Primitives & Streams (`cuda-cpp-warp-simt`)

- **Language / Representation**: **CUDA C++**
- **Taxonomic Classification**: `GPU Parallel Compute Language (SIMT Extension of C++)`
- **Technical Relationship**: NVIDIA SIMT heterogeneous parallel programming extension of ISO C++ (`__global__`, `__device__`, `__shared__`) compiled by `nvcc` / `clang --cuda-gpu-arch`.
- **Governing Standards & Versions**: NVIDIA CUDA C++ Programming Guide (CUDA 12.x), PTX ISA (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **CUDA C++** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Execution space qualifiers (`__global__`, `__device__`, `__host__`), launch configuration `<<<grid, block, shmem, stream>>>`, and 32-thread Warp SIMT execution. |
| 2 | **Type System & Inference** | Vector alignment types (`float4`, `int4` 16-byte vectorized loads), `__half`/`__nv_bfloat16`, and `__restrict__` pointer aliasing promises. |
| 3 | **Memory Management** | Global DRAM (coalesced across 32 threads in a warp), per-SM Shared Memory (`__shared__`, 32 banks of 4 bytes each), Constant/Texture caches, and `cudaMallocAsync` stream-ordered pools. |
| 4 | **Concurrency & Async Programming** | `__syncthreads()` (must be reached by all threads in block—never inside divergent conditional branches!), `__syncwarp(mask)`, `cooperative_groups`, and `cuda::atomic`. |
| 5 | **Standard Library & Ecosystem** | cuBLAS, cuDNN, Thrust, CUB (`cub::BlockReduce`), Cutlass, Nsight Compute (`ncu`), Nsight Systems (`nsys`). |
| 6 | **Build Systems & Package Management** | CMake (`LANGUAGES CUDA`, `CMAKE_CUDA_ARCHITECTURES "80;86;90"`), `nvcc -lineinfo --use_fast_math`. |
| 7 | **Compiler / Interpreter Behavior** | Splits host C++ and device PTX/SASS compilation; inspect register spilling and local-memory traffic via `nvcc --ptxas-options=-v`. |
| 8 | **Debugging** | `compute-sanitizer --tool memcheck|racecheck|initcheck|synccheck` and `cuda-gdb`. |
| 9 | **Security** | Guard every thread index against problem bounds (`if (idx < N)`) before reading or writing global memory. |
| 10 | **Performance Optimization** | Eliminate 32-way shared-memory bank conflicts by padding 2D tiles (`__shared__ float tile[32][33]`), use `__shfl_down_sync(0xffffffffu, val, offset)` for warp reductions, and overlap H2D/D2H copies via pinned host memory (`cudaMallocHost`) + streams. |
| 11 | **Error Handling** | Wrap every CUDA runtime call and follow kernel launches with `cudaGetLastError()` checking (`CUDA_CHECK(err)`). |
| 12 | **Testing Methodologies** | Verify shared-memory bank-conflict-free stride geometry and compare GPU output against an IEEE 754 `double` CPU reference. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (CUDA 11.8 / 12.x (Compute Capability sm_70 / sm_80 / sm_90)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | C/C++ host ABI, PyTorch custom C++/CUDA extensions, and DLPack zero-copy tensor sharing. |
| 18 | **Common Engineering Mistakes** | Calling `__syncthreads()` inside a thread-divergent `if (threadIdx.x < 16)` branch (deadlocks SM!), unpadded `[32][32]` shared-memory column access causing 32-way bank conflicts, and ignoring asynchronous kernel launch errors. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/cuda-cpp-warp-simt/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **CUDA C++**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``compute-sanitizer --tool memcheck|racecheck|initcheck|synccheck` and `cuda-gdb`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `CMake (`LANGUAGES CUDA`, `CMAKE_CUDA_ARCHITECTURES "80;86;90"`), `nvcc -lineinfo --use_fast_math`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Eliminate 32-way shared-memory bank conflicts by padding 2D tiles (`__shared__ float tile[32][33]`), use `__shfl_down_sync(0xffffffffu, val, offset)` for warp reductions, and overlap H2D/D2H copies via pinned host memory (`cudaMallocHost`) + streams.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Guard every thread index against problem bounds (`if (idx < N)`) before reading or writing global memory.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Verify shared-memory bank-conflict-free stride geometry and compare GPU output against an IEEE 754 `double` CPU reference.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (C/C++ host ABI, PyTorch custom C++/CUDA extensions, and DLPack zero-copy tensor sharing.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
