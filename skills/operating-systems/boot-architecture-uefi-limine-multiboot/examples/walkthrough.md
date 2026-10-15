# Verified Example: `boot-architecture-uefi-limine-multiboot` (`boot_mmap_sanitizer.c`)

```
#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

#define MEM_USABLE   1U
#define MEM_RESERVED 2U

typedef struct {
    uint64_t base;
    uint64_t length;
    uint32_t type;
} boot_mmap_entry_t;

/* Sanitizes overlapping E820/UEFI memory map intervals:
 * If a [base, base+len) range overlaps any MEM_RESERVED region, it MUST NOT be allocated as usable RAM!
 */
static bool boot_range_is_strictly_usable(const boot_mmap_entry_t *map, size_t n, uint64_t req_base, uint64_t req_len) {
    if (!map || req_len == 0ULL || req_base > UINT64_MAX - req_len) return false;
    uint64_t req_end = req_base + req_len;
    bool covered_by_usable = false;
    for (size_t i = 0U; i < n; ++i) {
        uint64_t e_start = map[i].base;
        uint64_t e_end = e_start + map[i].length;
        bool overlaps = (req_base < e_end) && (req_end > e_start);
        if (overlaps && map[i].type != MEM_USABLE) {
            return false; /* Reserved/ACPI region takes strict precedence! */
        }
        if (map[i].type == MEM_USABLE && req_base >= e_start && req_end <= e_end) {
            covered_by_usable = true;
        }
    }
    return covered_by_usable;
}

int main(void) {
    boot_mmap_entry_t e820[2] = {
        {.base = 0x100000ULL, .length = 0x800000ULL, .type = MEM_USABLE},
        {.base = 0x400000ULL, .length = 0x010000ULL, .type = MEM_RESERVED} /* Overlapping firmware hole! */
    };
    assert(boot_range_is_strictly_usable(e820, 2U, 0x100000ULL, 0x200000ULL) == true);
    assert(boot_range_is_strictly_usable(e820, 2U, 0x3F0000ULL, 0x020000ULL) == false);
    puts("BOOT E820/UEFI MEMORY MAP OVERLAP SANITIZER VERIFIED");
    return 0;
}

```
