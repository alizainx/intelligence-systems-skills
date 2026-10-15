# Verified Example: `linux-userspace-libc-elf-and-wayland` (`wayland_wire_parser.c`)

```
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/* Wayland Wire Protocol Header Parser (Portable across glibc, musl, relibc without systemd dependencies):
 * Word 0: uint32_t object_id
 * Word 1: (uint32_t size << 16) | (uint16_t opcode)
 * Invariants: size >= 8 bytes (header size) and (size % 4) == 0 (32-bit word aligned).
 */
typedef struct {
    uint32_t object_id;
    uint16_t opcode;
    uint16_t size;
} wl_msg_hdr_t;

static int wl_parse_header(const uint8_t *buf, size_t buf_len, wl_msg_hdr_t *out) {
    if (!buf || !out || buf_len < 8U) return -1;
    uint32_t obj_id = 0U, word1 = 0U;
    memcpy(&obj_id, buf, 4U);
    memcpy(&word1, buf + 4U, 4U);
    uint16_t size = (uint16_t)(word1 >> 16U);
    uint16_t opcode = (uint16_t)(word1 & 0xFFFFU);
    if (size < 8U || (size % 4U) != 0U || (size_t)size > buf_len) {
        return -2; /* Malformed or truncated Wayland message frame! */
    }
    out->object_id = obj_id;
    out->opcode = opcode;
    out->size = size;
    return 0;
}

int main(void) {
    uint32_t raw_valid[3] = {1U, (12U << 16U) | 3U, 0x12345678U};
    wl_msg_hdr_t hdr = {0};
    assert(wl_parse_header((const uint8_t *)raw_valid, sizeof(raw_valid), &hdr) == 0);
    assert(hdr.object_id == 1U && hdr.opcode == 3U && hdr.size == 12U);

    /* Reject unaligned size (10 bytes is not a multiple of 4) and size < 8 */
    uint32_t raw_unaligned[3] = {1U, (10U << 16U) | 1U, 0U};
    assert(wl_parse_header((const uint8_t *)raw_unaligned, sizeof(raw_unaligned), &hdr) == -2);
    uint32_t raw_too_small[2] = {1U, (4U << 16U) | 1U};
    assert(wl_parse_header((const uint8_t *)raw_too_small, sizeof(raw_too_small), &hdr) == -2);
    puts("LINUX USERSPACE PORTABLE LIBC & WAYLAND WIRE PROTOCOL VERIFIED");
    return 0;
}

```
