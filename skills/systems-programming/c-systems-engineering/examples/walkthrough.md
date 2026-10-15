# Verified Example: `c-systems-engineering` (`c11_aligned_arena.c`)

```
#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    uint8_t *base;
    size_t capacity;
    size_t offset;
} c11_arena_t;

static int c11_arena_init(c11_arena_t *a, uint8_t *backing, size_t cap) {
    if (a == NULL || backing == NULL || cap == 0U) return -1;
    a->base = backing;
    a->capacity = cap;
    a->offset = 0U;
    return 0;
}

static void *c11_arena_alloc_aligned(c11_arena_t *a, size_t count, size_t elem_size, size_t align) {
    if (a == NULL || count == 0U || elem_size == 0U || align == 0U || (align & (align - 1U)) != 0U) return NULL;
    if (count > SIZE_MAX / elem_size) return NULL;
    size_t bytes = count * elem_size;
    uintptr_t cur = (uintptr_t)(a->base + a->offset);
    size_t mis = (size_t)(cur & (align - 1U));
    size_t pad = (mis == 0U) ? 0U : (align - mis);
    if (pad > a->capacity - a->offset) return NULL;
    size_t aligned_off = a->offset + pad;
    if (bytes > a->capacity - aligned_off) return NULL;
    void *ptr = a->base + aligned_off;
    memset(ptr, 0, bytes);
    a->offset = aligned_off + bytes;
    return ptr;
}

int main(void) {
    _Alignas(64) uint8_t backing[256];
    c11_arena_t arena = {0};
    assert(c11_arena_init(&arena, backing, sizeof(backing)) == 0);
    uint8_t *b1 = (uint8_t *)c11_arena_alloc_aligned(&arena, 1U, 1U, 1U);
    assert(b1 != NULL);
    uint64_t *v64 = (uint64_t *)c11_arena_alloc_aligned(&arena, 4U, sizeof(uint64_t), 64U);
    assert(v64 != NULL && (((uintptr_t)v64 & 63U) == 0U));
    assert(c11_arena_alloc_aligned(&arena, SIZE_MAX / 4U, 8U, 8U) == NULL);
    assert(c11_arena_alloc_aligned(&arena, 100U, 8U, 8U) == NULL);
    printf("C11 SYSTEMS ENGINEERING ARENA VERIFIED\n");
    return 0;
}

```
