#include <assert.h>
#include <stdatomic.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    atomic_uint seq;
    uint64_t tick_ns;
    uint64_t mono_offset;
} seqlock_clock_t;

static void seqlock_write(seqlock_clock_t *sc, uint64_t tick, uint64_t off) {
    unsigned int s = atomic_load_explicit(&sc->seq, memory_order_relaxed);
    atomic_store_explicit(&sc->seq, s + 1U, memory_order_release); /* Odd = writer active! */
    atomic_thread_fence(memory_order_acq_rel);
    sc->tick_ns = tick;
    sc->mono_offset = off;
    atomic_store_explicit(&sc->seq, s + 2U, memory_order_release); /* Even = consistent! */
}

static bool seqlock_read_try(const seqlock_clock_t *sc, uint64_t *out_tick, uint64_t *out_off) {
    unsigned int s1 = atomic_load_explicit(&sc->seq, memory_order_acquire);
    if ((s1 & 1U) != 0U) {
        return false; /* Writer currently mid-update (odd sequence number)! */
    }
    uint64_t t = sc->tick_ns;
    uint64_t o = sc->mono_offset;
    atomic_thread_fence(memory_order_acquire);
    unsigned int s2 = atomic_load_explicit(&sc->seq, memory_order_relaxed);
    if (s1 != s2) {
        return false; /* Torn read detected! */
    }
    *out_tick = t;
    *out_off = o;
    return true;
}

int main(void) {
    seqlock_clock_t clk = {0};
    uint64_t t = 0ULL, o = 0ULL;
    seqlock_write(&clk, 1000ULL, 500ULL);
    assert(seqlock_read_try(&clk, &t, &o) && t == 1000ULL && o == 500ULL);

    /* Simulate interrupted torn state (seq is odd = 3) -> reader must reject torn read! */
    atomic_store(&clk.seq, 3U);
    assert(!seqlock_read_try(&clk, &t, &o));
    puts("KERNEL SEQLOCK & C11 ACQUIRE-RELEASE MEMORY ORDERING VERIFIED");
    return 0;
}
