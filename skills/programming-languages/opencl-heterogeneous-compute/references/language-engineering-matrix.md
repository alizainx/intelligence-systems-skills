# Deep Engineering Reference: OpenCL (2.0/3.0) NDRange Work-Groups, Address Spaces, Local Barriers & SPIR-V (`opencl-heterogeneous-compute`)

- **Language / Representation**: **OpenCL**
- **Taxonomic Classification**: `Heterogeneous Parallel Compute Language (C99/C++ Kernel Subset)`
- **Technical Relationship**: Khronos open-standard heterogeneous compute language (`OpenCL C` / `C++ for OpenCL`) targeting GPUs, CPUs, FPGAs, and DSPs via SPIR-V.
- **Governing Standards & Versions**: Khronos OpenCL 3.0 Specification, OpenCL C Language Specification, SPIR-V (OpenCL 1.2 / 2.0 / 3.0)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **OpenCL** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Explicit address-space qualifiers (`__global`, `__local`, `__constant`, `__private`), built-in vector types (`float4`, `int8`), and `get_global_id(0)` / `get_local_id(0)`. |
| 2 | **Type System & Inference** | Fixed-width scalars, vector swizzling (`v.xyzw`, `v.lo`, `v.hi`), `image2d_t` sampler types, and `restrict` pointers. |
| 3 | **Memory Management** | Host-device `cl_mem` buffers (`CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR`), pinned host staging buffers (`CL_MEM_ALLOC_HOST_PTR`), and SVM (Shared Virtual Memory). |
| 4 | **Concurrency & Async Programming** | `barrier(CLK_LOCAL_MEM_FENCE | CLK_GLOBAL_MEM_FENCE)` work-group synchronization, sub-group shuffle operations (`cl_khr_subgroups`), and out-of-order `cl_command_queue` event DAGs. |
| 5 | **Standard Library & Ecosystem** | Khronos ICD Loader, `clinfo`, `clspv`, `pocld`, `ViennaCL`, `CLBlast`. |
| 6 | **Build Systems & Package Management** | Offline compilation to SPIR-V (`clang -cl-std=CL3.0 --target=spirv64`) or runtime `clBuildProgram` with `-cl-mad-enable -cl-no-signed-zeros`. |
| 7 | **Compiler / Interpreter Behavior** | Vendor JIT compilation from source or SPIR-V; always inspect `clGetProgramBuildInfo(..., CL_PROGRAM_BUILD_LOG, ...)` on build failure. |
| 8 | **Debugging** | CodeXL / RenderDoc / Intel GTPin / `printf` in OpenCL 1.2+ kernels. |
| 9 | **Security** | Bounds-check `get_global_id(0) < n` when `global_work_size` is rounded up to a multiple of `local_work_size`. |
| 10 | **Performance Optimization** | Select `local_work_size` as a multiple of device preferred work-group size multiple (`CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE`, typically 32 or 64) and vectorize loads (`vload4`/`vstore4`). |
| 11 | **Error Handling** | Check every `cl_int` return status (`CL_SUCCESS == 0`) on host API calls. |
| 12 | **Testing Methodologies** | Validate work-group tree reduction invariants across non-power-of-two array sizes. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (OpenCL 1.2 / 2.0 / 3.0); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Vulkan/OpenGL buffer sharing (`cl_khr_gl_sharing`, `cl_khr_external_memory`) and C/C++ host drivers. |
| 18 | **Common Engineering Mistakes** | Passing `global_work_size` not divisible by `local_work_size` in OpenCL 1.2, divergent `barrier(CLK_LOCAL_MEM_FENCE)`, and ignoring `clBuildProgram` logs. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/opencl-heterogeneous-compute/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **OpenCL**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `CodeXL / RenderDoc / Intel GTPin / `printf` in OpenCL 1.2+ kernels.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Offline compilation to SPIR-V (`clang -cl-std=CL3.0 --target=spirv64`) or runtime `clBuildProgram` with `-cl-mad-enable -cl-no-signed-zeros`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Select `local_work_size` as a multiple of device preferred work-group size multiple (`CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE`, typically 32 or 64) and vectorize loads (`vload4`/`vstore4`).).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Bounds-check `get_global_id(0) < n` when `global_work_size` is rounded up to a multiple of `local_work_size`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Validate work-group tree reduction invariants across non-power-of-two array sizes.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Vulkan/OpenGL buffer sharing (`cl_khr_gl_sharing`, `cl_khr_external_memory`) and C/C++ host drivers.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
