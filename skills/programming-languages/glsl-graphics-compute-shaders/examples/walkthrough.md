# Nontrivial Implementation & Multi-File Engineering Walkthrough: `glsl-graphics-compute-shaders`

- **Target File**: `examples/pbr_exposure_pass.comp`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
#version 450
layout(local_size_x = 16, local_size_y = 16, local_size_z = 1) in;

// std140 UBO uses vec4 alignment (avoiding vec3 16-byte padding mismatch)
layout(std140, set = 0, binding = 0) uniform ExposureParams {
    vec4 exposure_gamma_pad; // .x = exposure, .y = inv_gamma, .zw = pad
    uvec4 viewport_size;     // .x = width, .y = height
} u_params;

layout(set = 0, binding = 1, rgba16f) uniform readonly image2D in_hdr;
layout(set = 0, binding = 2, rgba8)   uniform writeonly image2D out_ldr;

void main() {
    uvec2 gid = gl_GlobalInvocationID.xy;
    if (gid.x >= u_params.viewport_size.x || gid.y >= u_params.viewport_size.y) {
        return;
    }
    vec4 hdr = imageLoad(in_hdr, ivec2(gid));
    vec3 mapped = vec3(1.0) - exp(-max(hdr.rgb, vec3(0.0)) * u_params.exposure_gamma_pad.x);
    vec3 srgb = pow(max(mapped, vec3(1e-6)), vec3(u_params.exposure_gamma_pad.y));
    imageStore(out_ldr, ivec2(gid), vec4(srgb, hdr.a));
}

```
