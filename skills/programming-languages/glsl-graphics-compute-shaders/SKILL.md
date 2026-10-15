---
name: glsl-graphics-compute-shaders
description: Write, audit, and verify GLSL 450/460 vertex, fragment, and compute shaders with explicit std140/std430 UBO/SSBO alignment rules, uniform control flow for derivatives (dFdx/texture), and glslangValidator/SPIR-V compliance.
allowed-tools: execute_bash view_file write_to_file
---

# GLSL (450/460 Vulkan & OpenGL) std140/std430 Layout, SPIR-V, Derivatives & Compute Shaders

Write, audit, and verify GLSL 450/460 vertex, fragment, and compute shaders with explicit std140/std430 UBO/SSBO alignment rules, uniform control flow for derivatives (dFdx/texture), and glslangValidator/SPIR-V compliance.

## A. Identity

- **Skill Name**: `glsl-graphics-compute-shaders`
- **Domain**: `programming-languages`
- **Language / Representation**: **GLSL** (`Graphics & Compute Shader Language`)
- **Technical Relationship**: Khronos OpenGL / Vulkan (`#version 450` / `#version 460`) shading language compiling to SPIR-V for GPU graphics pipelines and compute stages.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **GLSL**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: OpenGL Shading Language Specification 4.60, Vulkan GLSL Extension (`GL_KHR_vulkan_glsl`) (GLSL 330 / 450 / 460 / ES 320)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``glslangValidator -V shader.comp -o shader.spv && spirv-val shader.spv`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **GLSL** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **GLSL**.

### Technical Triggers

- Files, build manifests, or prompts targeting **GLSL** (`pbr_exposure_pass.comp`, ``glslangValidator -V shader.comp -o shader.spv && spirv-val shader.spv`.`).

### Prerequisites

- Target language version (GLSL 330 / 450 / 460 / ES 320), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **GLSL** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (GLSL 330 / 450 / 460 / ES 320), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (UBO (`std140` 16-byte `vec4` rounding) vs SSBO (`std430` tightly packed scalars/arrays, except `vec3` still aligns to 16 bytes (`4N`)!), and push constants (`<= 128` bytes).), type soundness limits (`vec2`/`vec3`/`vec4`, column-major `mat4` (`m[col][row]`), `uvec4`, `sampler2D`, `image2D` (`rgba8`, `r32f`).), and concurrency hazards (Compute shader `shared` memory with `memoryBarrierShared(); barrier();` and `GL_KHR_shader_subgroup` operations.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce OpenGL Shading Language Specification 4.60, Vulkan GLSL Extension (`GL_KHR_vulkan_glsl`).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Mandatory `#version 450 core` header, explicit `layout(set = M, binding = N)` descriptors, `in`/`out` stage interfaces, and `layout(local_size_x = 64) in;`.
2. **Type System & Inference**: `vec2`/`vec3`/`vec4`, column-major `mat4` (`m[col][row]`), `uvec4`, `sampler2D`, `image2D` (`rgba8`, `r32f`).
3. **Memory Management**: UBO (`std140` 16-byte `vec4` rounding) vs SSBO (`std430` tightly packed scalars/arrays, except `vec3` still aligns to 16 bytes (`4N`)!), and push constants (`<= 128` bytes).
4. **Concurrency & Async Programming**: Compute shader `shared` memory with `memoryBarrierShared(); barrier();` and `GL_KHR_shader_subgroup` operations.
5. **Standard Library & Ecosystem**: `glslangValidator`, `spirv-opt`, `spirv-val`, `spirv-cross`, RenderDoc, Vulkan SDK.
6. **Build Systems & Package Management**: `glslangValidator -V shader.comp -o shader.spv && spirv-val shader.spv`.
7. **Compiler / Interpreter Behavior**: Compiles to Khronos SPIR-V SSA intermediate representation; loops are unrolled or predicated by driver backend.
8. **Debugging & Observability**: RenderDoc shader step-debugging, `GL_EXT_debug_printf`, and NaN/Inf false-color visualization.
9. **Security Hardening**: Avoid unbounded shader loops controlled by untrusted uniform buffers (prevents GPU TDR device-lost resets) and clamp `pow(x, y)` inputs (`max(x, 1e-6)`).
10. **Performance Optimization**: Replace `vec3` in `std140`/`std430` structs with `vec4` (packs a useful scalar in `.w` and avoids 4-byte alignment traps!), use `fma(a, b, c)`, and minimize dynamic branching.
11. **Error Handling Discipline**: Validate SPIR-V assembly (`spirv-val`) at build time and check `glGetShaderInfoLog`.
12. **Testing Methodologies**: Verify `std140`/`std430` byte-offset alignment parity between C/C++ host structs and GLSL blocks.
13. **Interoperability & Cross-Platform ABI**: Vulkan/OpenGL host descriptor bindings (`VkDescriptorSetLayoutBinding`) and `spirv-cross` cross-compilation to HLSL/MSL.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/glsl-graphics-compute-shaders/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (GLSL 330 / 450 / 460 / ES 320), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in GLSL**: Using `vec3` inside C++ structs mapped to `std140`/`std430` buffers (C++ `sizeof` is 12 bytes, GLSL alignment is 16 bytes!), and calling `texture()` inside non-uniform control flow (broken mipmap `dFdx`/`dFdy` quads).
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
