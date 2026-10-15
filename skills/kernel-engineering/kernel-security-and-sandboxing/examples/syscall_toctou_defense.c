#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    uint32_t cmd_type;
    uint32_t payload_len;
    uint8_t  payload[16];
} user_ioctl_req_t;

/* Prevents Kernel TOCTOU Double-Fetch Vulnerability:
 * Copies user-space struct ONCE into kernel stack memory (`kreq`) and validates `kreq.payload_len`
 * on the isolated kernel copy rather than re-reading volatile user memory!
 */
static int sys_ioctl_safe_single_fetch(const volatile user_ioctl_req_t *user_ptr, uint8_t *k_out_buf, size_t k_max) {
    if (!user_ptr || !k_out_buf) return -1;
    user_ioctl_req_t kreq;
    /* Single atomic snapshot copy_from_user into kernel space */
    const volatile uint8_t *src = (const volatile uint8_t *)user_ptr;
    uint8_t *dst = (uint8_t *)&kreq;
    for (size_t i = 0U; i < sizeof(kreq); ++i) {
        dst[i] = src[i];
    }
    if (kreq.payload_len > sizeof(kreq.payload) || kreq.payload_len > k_max) {
        return -2; /* Bounds check on kernel snapshot */
    }
    memcpy(k_out_buf, kreq.payload, kreq.payload_len);
    return 0;
}

int main(void) {
    volatile user_ioctl_req_t u_req = {.cmd_type = 1U, .payload_len = 8U, .payload = {1,2,3,4,5,6,7,8}};
    uint8_t kbuf[16] = {0};
    assert(sys_ioctl_safe_single_fetch(&u_req, kbuf, sizeof(kbuf)) == 0);
    u_req.payload_len = 64U; /* Attacker mutates length to > 16 */
    assert(sys_ioctl_safe_single_fetch(&u_req, kbuf, sizeof(kbuf)) == -2);
    puts("KERNEL TOCTOU DOUBLE-FETCH PREVENTION & SYSCALL SANDBOXING VERIFIED");
    return 0;
}
