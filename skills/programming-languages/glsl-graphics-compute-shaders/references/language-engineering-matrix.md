# Deep Engineering Reference: GLSL (450/460 Vulkan & OpenGL) std140/std430 Layout, SPIR-V, Derivatives & Compute Shaders (`glsl-graphics-compute-shaders`)

- **Language / Representation**: **GLSL**
- **Taxonomic Classification**: `Graphics & Compute Shader Language`
- **Technical Relationship**: Khronos OpenGL / Vulkan (`#version 450` / `#version 460`) shading language compiling to SPIR-V for GPU graphics pipelines and compute stages.
- **Governing Standards & Versions**: OpenGL Shading Language Specification 4.60, Vulkan GLSL Extension (`GL_KHR_vulkan_glsl`) (GLSL 330 / 450 / 460 / ES 320)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **GLSL** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Mandatory `#version 450 core` header, explicit `layout(set = M, binding = N)` descriptors, `in`/`out` stage interfaces, and `layout(local_size_x = 64) in;`. |
| 2 | **Type System & Inference** | `vec2`/`vec3`/`vec4`, column-major `mat4` (`m[col][row]`), `uvec4`, `sampler2D`, `image2D` (`rgba8`, `r32f`). |
| 3 | **Memory Management** | UBO (`std140` 16-byte `vec4` rounding) vs SSBO (`std430` tightly packed scalars/arrays, except `vec3` still aligns to 16 bytes (`4N`)!), and push constants (`<= 128` bytes). |
| 4 | **Concurrency & Async Programming** | Compute shader `shared` memory with `memoryBarrierShared(); barrier();` and `GL_KHR_shader_subgroup` operations. |
| 5 | **Standard Library & Ecosystem** | `glslangValidator`, `spirv-opt`, `spirv-val`, `spirv-cross`, RenderDoc, Vulkan SDK. |
| 6 | **Build Systems & Package Management** | `glslangValidator -V shader.comp -o shader.spv && spirv-val shader.spv`. |
| 7 | **Compiler / Interpreter Behavior** | Compiles to Khronos SPIR-V SSA intermediate representation; loops are unrolled or predicated by driver backend. |
| 8 | **Debugging** | RenderDoc shader step-debugging, `GL_EXT_debug_printf`, and NaN/Inf false-color visualization. |
| 9 | **Security** | Avoid unbounded shader loops controlled by untrusted uniform buffers (prevents GPU TDR device-lost resets) and clamp `pow(x, y)` inputs (`max(x, 1e-6)`). |
| 10 | **Performance Optimization** | Replace `vec3` in `std140`/`std430` structs with `vec4` (packs a useful scalar in `.w` and avoids 4-byte alignment traps!), use `fma(a, b, c)`, and minimize dynamic branching. |
| 11 | **Error Handling** | Validate SPIR-V assembly (`spirv-val`) at build time and check `glGetShaderInfoLog`. |
| 12 | **Testing Methodologies** | Verify `std140`/`std430` byte-offset alignment parity between C/C++ host structs and GLSL blocks. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (GLSL 330 / 450 / 460 / ES 320); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Vulkan/OpenGL host descriptor bindings (`VkDescriptorSetLayoutBinding`) and `spirv-cross` cross-compilation to HLSL/MSL. |
| 18 | **Common Engineering Mistakes** | Using `vec3` inside C++ structs mapped to `std140`/`std430` buffers (C++ `sizeof` is 12 bytes, GLSL alignment is 16 bytes!), and calling `texture()` inside non-uniform control flow (broken mipmap `dFdx`/`dFdy` quads). |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/glsl-graphics-compute-shaders/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **GLSL**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via `RenderDoc shader step-debugging, `GL_EXT_debug_printf`, and NaN/Inf false-color visualization.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via ``glslangValidator -V shader.comp -o shader.spv && spirv-val shader.spv`.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Replace `vec3` in `std140`/`std430` structs with `vec4` (packs a useful scalar in `.w` and avoids 4-byte alignment traps!), use `fma(a, b, c)`, and minimize dynamic branching.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Avoid unbounded shader loops controlled by untrusted uniform buffers (prevents GPU TDR device-lost resets) and clamp `pow(x, y)` inputs (`max(x, 1e-6)`).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Verify `std140`/`std430` byte-offset alignment parity between C/C++ host structs and GLSL blocks.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Vulkan/OpenGL host descriptor bindings (`VkDescriptorSetLayoutBinding`) and `spirv-cross` cross-compilation to HLSL/MSL.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
