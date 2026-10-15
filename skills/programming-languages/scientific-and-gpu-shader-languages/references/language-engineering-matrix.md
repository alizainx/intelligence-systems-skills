# GPU SIMT Coalescing, Bank Conflicts & Shader Alignment Reference

In GLSL `std140` uniform buffers, a `vec3` has base alignment `16 bytes` (4 floats), so placing a `float` immediately after `vec3` requires explicit offset awareness.
