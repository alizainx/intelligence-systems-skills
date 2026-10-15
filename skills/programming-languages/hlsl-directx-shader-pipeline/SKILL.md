---
name: hlsl-directx-shader-pipeline
description: Write, optimize, and verify HLSL Shader Model 6.x compute, mesh, and pixel shaders using 16-byte cbuffer packing rules, WaveActiveSum/WaveReadLaneFirst intrinsics, SM 6.6 descriptor heap indexing, and DXC compilation.
allowed-tools: execute_bash view_file write_to_file
---

# HLSL (Shader Model 6.6/6.7 DXC) Constant Buffer Packing, Wave Intrinsics & Root Signatures

Write, optimize, and verify HLSL Shader Model 6.x compute, mesh, and pixel shaders using 16-byte cbuffer packing rules, WaveActiveSum/WaveReadLaneFirst intrinsics, SM 6.6 descriptor heap indexing, and DXC compilation.

## A. Identity

- **Skill Name**: `hlsl-directx-shader-pipeline`
- **Domain**: `programming-languages`
- **Language / Representation**: **HLSL** (`Graphics & Compute Shader Language`)
- **Technical Relationship**: High-Level Shader Language for DirectX 12 (`Shader Model 6.x`) and Vulkan, compiled by DXC (`dxc.exe`) to DXIL (LLVM-based) or SPIR-V.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **HLSL**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: Microsoft DirectX Specs (HLSL Shader Model 6.0-6.8) (Shader Model 6.0 / 6.6 / 6.7 (DXC))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (``dxc -T cs_6_6 -E CSMain -WX -Zi -Qembed_debug -O3 shader.hlsl -Fo shader.dxil` (or `-spirv` for Vulkan).`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **HLSL** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **HLSL**.

### Technical Triggers

- Files, build manifests, or prompts targeting **HLSL** (`wave_coalesced_atomic.hlsl`, ``dxc -T cs_6_6 -E CSMain -WX -Zi -Qembed_debug -O3 shader.hlsl -Fo shader.dxil` (or `-spirv` for Vulkan).`).

### Prerequisites

- Target language version (Shader Model 6.0 / 6.6 / 6.7 (DXC)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **HLSL** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Shader Model 6.0 / 6.6 / 6.7 (DXC)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (`cbuffer` / `ConstantBuffer<T>` packs variables into 16-byte (`float4`) registers so a variable never straddles a 16-byte boundary; `groupshared` LDS memory.), type soundness limits (`float4`, `float4x4` (`#pragma pack_matrix(column_major)` or `row_major`), `uint4`, `float16_t` (`-enable-16bit-types`), `StructuredBuffer<T>`, `RWStructuredBuffer<T>`.), and concurrency hazards (`GroupMemoryBarrierWithGroupSync()`, SM 6.0+ Wave Intrinsics (`WaveActiveSum`, `WavePrefixSum`, `WaveIsFirstLane`), and `InterlockedAdd`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce Microsoft DirectX Specs (HLSL Shader Model 6.0-6.8).
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit register bindings (`register(b0, space0)`, `register(t0)`, `register(u0)`), semantics (`SV_DispatchThreadID`, `SV_GroupIndex`, `SV_Target0`), and `[numthreads(X, Y, Z)]`.
2. **Type System & Inference**: `float4`, `float4x4` (`#pragma pack_matrix(column_major)` or `row_major`), `uint4`, `float16_t` (`-enable-16bit-types`), `StructuredBuffer<T>`, `RWStructuredBuffer<T>`.
3. **Memory Management**: `cbuffer` / `ConstantBuffer<T>` packs variables into 16-byte (`float4`) registers so a variable never straddles a 16-byte boundary; `groupshared` LDS memory.
4. **Concurrency & Async Programming**: `GroupMemoryBarrierWithGroupSync()`, SM 6.0+ Wave Intrinsics (`WaveActiveSum`, `WavePrefixSum`, `WaveIsFirstLane`), and `InterlockedAdd`.
5. **Standard Library & Ecosystem**: DirectX Shader Compiler (`dxc`), PIX on Windows, RenderDoc, Agility SDK.
6. **Build Systems & Package Management**: `dxc -T cs_6_6 -E CSMain -WX -Zi -Qembed_debug -O3 shader.hlsl -Fo shader.dxil` (or `-spirv` for Vulkan).
7. **Compiler / Interpreter Behavior**: DXC Clang/LLVM frontend emitting signed DXIL containers or SPIR-V; use `[unroll]` / `[loop]` attributes explicitly.
8. **Debugging & Observability**: PIX GPU Capture shader debugger, RenderDoc, and DXIL disassembly (`dxc -dumpbin`).
9. **Security Hardening**: Validate buffer bounds (`[numthreads]` tail threads) and avoid out-of-bounds descriptor table indexing.
10. **Performance Optimization**: Use Wave Intrinsics (`WaveIsFirstLane()` + `WaveActiveCountBits()`) to coalesce atomic updates from 32/64 threads down to a single `InterlockedAdd` per wave.
11. **Error Handling Discipline**: Enforce `-WX` (warnings as errors) in DXC to catch implicit vector truncation (`float4` -> `float3` warning).
12. **Testing Methodologies**: Verify 16-byte `ConstantBuffer<T>` layout parity with C++ `static_assert(sizeof(T) % 16 == 0)`.
13. **Interoperability & Cross-Platform ABI**: DirectX 12 Root Signatures, `ResourceDescriptorHeap[]` (SM 6.6 bindless), and Vulkan `-spirv`.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/hlsl-directx-shader-pipeline/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Shader Model 6.0 / 6.6 / 6.7 (DXC)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in HLSL**: Multiplying `v * M` instead of `mul(M, v)` (`*` in HLSL is component-wise!), straddling 16-byte boundaries in `cbuffer`, and implicit vector truncation.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
