__kernel void reduce_sum_f32(
    __global const float * restrict input,
    __global float * restrict partial_sums,
    __local float * restrict scratch,
    const unsigned int n)
{
    const unsigned int gid = get_global_id(0);
    const unsigned int lid = get_local_id(0);
    const unsigned int lsize = get_local_size(0);

    scratch[lid] = (gid < n) ? input[gid] : 0.0f;
    barrier(CLK_LOCAL_MEM_FENCE);

    for (unsigned int stride = lsize >> 1; stride > 0U; stride >>= 1) {
        if (lid < stride) {
            scratch[lid] += scratch[lid + stride];
        }
        barrier(CLK_LOCAL_MEM_FENCE);
    }

    if (lid == 0U) {
        partial_sums[get_group_id(0)] = scratch[0];
    }
}
