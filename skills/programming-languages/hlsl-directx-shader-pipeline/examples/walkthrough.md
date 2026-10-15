# Nontrivial Implementation & Multi-File Engineering Walkthrough: `hlsl-directx-shader-pipeline`

- **Target File**: `examples/wave_coalesced_atomic.hlsl`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
// HLSL SM 6.6 compute shader using Wave intrinsics to coalesce atomic increments
struct DispatchParams {
    uint element_count;
    float threshold;
    float2 _pad0; // Explicit 16-byte cbuffer alignment
};

ConstantBuffer<DispatchParams> g_params : register(b0);
StructuredBuffer<float>        g_input  : register(t0);
RWByteAddressBuffer            g_counter: register(u0);

[numthreads(64, 1, 1)]
void CSMain(uint3 dtid : SV_DispatchThreadID) {
    if (dtid.x >= g_params.element_count) return;
    bool active = (g_input[dtid.x] > g_params.threshold);
    uint wave_hits = WaveActiveCountBits(active);
    if (WaveIsFirstLane() && wave_hits > 0U) {
        g_counter.InterlockedAdd(0U, wave_hits);
    }
}

```
