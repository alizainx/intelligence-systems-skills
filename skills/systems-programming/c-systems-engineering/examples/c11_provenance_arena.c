#include <assert.h>
#include <stdatomic.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    _Alignas(64) uint8_t *buf;
    size_t cap;
    _Atomic size_t offset;
} c11_atomic_arena_t;

static bool arena_alloc_checked(c11_atomic_arena_t *a, size_t count, size_t stride, size_t align, void **out) {
    if (!a || !a->buf || !out || stride == 0U || align == 0U || (align & (align - 1U)) != 0U) return false;
    if (count > SIZE_MAX / stride) return false;
    size_t bytes = count * stride;
    size_t cur = atomic_load_explicit(&a->offset, memory_order_relaxed);
    for (;;) {
        size_t mask = align - 1U;
        if (cur > SIZE_MAX - mask) return false;
        size_t aligned = (cur + mask) & ~mask;
        if (aligned > a->cap || bytes > a->cap - aligned) return false;
        if (atomic_compare_exchange_weak_explicit(&a->offset, &cur, aligned + bytes,
                                                 memory_order_acq_rel, memory_order_relaxed)) {
            *out = a->buf + aligned;
            memset(*out, 0, bytes);
            return true;
        }
    }
}

int main(void) {
    _Alignas(64) uint8_t backing[256];
    c11_atomic_arena_t arena = {.buf = backing, .cap = sizeof(backing), .offset = 0U};
    void *p1 = NULL;
    assert(arena_alloc_checked(&arena, 8U, sizeof(uint64_t), _Alignof(uint64_t), &p1));
    assert(((uintptr_t)p1 % _Alignof(uint64_t)) == 0U);
    assert(!arena_alloc_checked(&arena, SIZE_MAX, 4U, 8U, &p1));
    puts("VERIFIED: C11 atomic arena, alignment, provenance & overflow checks passed");
    return 0;
}
