---
name: opencl-heterogeneous-compute
description: Develop and verify portable OpenCL 1.2/2.0/3.0 kernels and host dispatch pipelines with explicit __global/__local/__constant/__private address spaces, work-group barrier synchronization, and cl_event profiling.
allowed-tools: execute_bash view_file write_to_file
---

# OpenCL (2.0/3.0) NDRange Work-Groups, Address Spaces, Local Barriers & SPIR-V

Develop and verify portable OpenCL 1.2/2.0/3.0 kernels and host dispatch pipelines with explicit __global/__local/__constant/__private address spaces, work-group barrier synchronization, and cl_event profiling.

## A. Identity

- **Skill Name**: `opencl-heterogeneous-compute`
- **Domain**: `programming-languages`
- **Language / Representation**: **OpenCL** (`Heterogeneous Parallel Compute Language (C99/C++ Kernel Subset)`)
- **Technical Relationship**: Khronos open-standard heterogeneous compute language (`OpenCL C` / `C++ for OpenCL`) targeting GPUs, CPUs, FPGAs, and DSPs via SPIR-V.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **OpenCL**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Khronos OpenCL 3.0 Specification, OpenCL C Language Specification, SPIR-V (OpenCL 1.2 / 2.0 / 3.0)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Offline compilation to SPIR-V (`clang -cl-std=CL3.0 --target=spirv64`) or runtime `clBuildProgram` with `-cl-mad-enable -cl-no-signed-zeros`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **OpenCL** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **OpenCL**.

### Technical Triggers

- Files, build manifests, or prompts targeting **OpenCL** (`workgroup_reduction.cl`, `Offline compilation to SPIR-V (`clang -cl-std=CL3.0 --target=spirv64`) or runtime `clBuildProgram` with `-cl-mad-enable -cl-no-signed-zeros`.`).

### Prerequisites

- Target language version (OpenCL 1.2 / 2.0 / 3.0), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **OpenCL** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (OpenCL 1.2 / 2.0 / 3.0), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Host-device `cl_mem` buffers (`CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR`), pinned host staging buffers (`CL_MEM_ALLOC_HOST_PTR`), and SVM (Shared Virtual Memory).), type soundness limits (Fixed-width scalars, vector swizzling (`v.xyzw`, `v.lo`, `v.hi`), `image2d_t` sampler types, and `restrict` pointers.), and concurrency hazards (`barrier(CLK_LOCAL_MEM_FENCE | CLK_GLOBAL_MEM_FENCE)` work-group synchronization, sub-group shuffle operations (`cl_khr_subgroups`), and out-of-order `cl_command_queue` event DAGs.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Khronos OpenCL 3.0 Specification, OpenCL C Language Specification, SPIR-V.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit address-space qualifiers (`__global`, `__local`, `__constant`, `__private`), built-in vector types (`float4`, `int8`), and `get_global_id(0)` / `get_local_id(0)`.
2. **Type System & Inference**: Fixed-width scalars, vector swizzling (`v.xyzw`, `v.lo`, `v.hi`), `image2d_t` sampler types, and `restrict` pointers.
3. **Memory Management**: Host-device `cl_mem` buffers (`CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR`), pinned host staging buffers (`CL_MEM_ALLOC_HOST_PTR`), and SVM (Shared Virtual Memory).
4. **Concurrency & Async Programming**: `barrier(CLK_LOCAL_MEM_FENCE | CLK_GLOBAL_MEM_FENCE)` work-group synchronization, sub-group shuffle operations (`cl_khr_subgroups`), and out-of-order `cl_command_queue` event DAGs.
5. **Standard Library & Ecosystem**: Khronos ICD Loader, `clinfo`, `clspv`, `pocld`, `ViennaCL`, `CLBlast`.
6. **Build Systems & Package Management**: Offline compilation to SPIR-V (`clang -cl-std=CL3.0 --target=spirv64`) or runtime `clBuildProgram` with `-cl-mad-enable -cl-no-signed-zeros`.
7. **Compiler / Interpreter Behavior**: Vendor JIT compilation from source or SPIR-V; always inspect `clGetProgramBuildInfo(..., CL_PROGRAM_BUILD_LOG, ...)` on build failure.
8. **Debugging & Observability**: CodeXL / RenderDoc / Intel GTPin / `printf` in OpenCL 1.2+ kernels.
9. **Security Hardening**: Bounds-check `get_global_id(0) < n` when `global_work_size` is rounded up to a multiple of `local_work_size`.
10. **Performance Optimization**: Select `local_work_size` as a multiple of device preferred work-group size multiple (`CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE`, typically 32 or 64) and vectorize loads (`vload4`/`vstore4`).
11. **Error Handling Discipline**: Check every `cl_int` return status (`CL_SUCCESS == 0`) on host API calls.
12. **Testing Methodologies**: Validate work-group tree reduction invariants across non-power-of-two array sizes.
13. **Interoperability & Cross-Platform ABI**: Vulkan/OpenGL buffer sharing (`cl_khr_gl_sharing`, `cl_khr_external_memory`) and C/C++ host drivers.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/opencl-heterogeneous-compute/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (OpenCL 1.2 / 2.0 / 3.0), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in OpenCL**: Passing `global_work_size` not divisible by `local_work_size` in OpenCL 1.2, divergent `barrier(CLK_LOCAL_MEM_FENCE)`, and ignoring `clBuildProgram` logs.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
