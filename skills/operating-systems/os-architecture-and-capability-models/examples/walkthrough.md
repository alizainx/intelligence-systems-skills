# Verified Example: `os-architecture-and-capability-models` (`capability_attenuation.c`)

```
#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

#define CAP_RIGHT_READ  (1U << 0U)
#define CAP_RIGHT_WRITE (1U << 1U)
#define CAP_RIGHT_GRANT (1U << 2U)

typedef struct {
    uint64_t object_id;
    uint32_t rights_mask;
    uint32_t badge;
} capability_t;

/* Capability derivation rule (seL4/L4 monotonic attenuation):
 * A derived capability can NEVER gain rights not present in the parent capability!
 */
static int cap_mint_derived(const capability_t *parent, uint32_t requested_rights, uint32_t badge, capability_t *out) {
    if (!parent || !out) return -1;
    if ((requested_rights & ~parent->rights_mask) != 0U) {
        return -2; /* Escalation of privilege rejected! */
    }
    out->object_id = parent->object_id;
    out->rights_mask = requested_rights;
    out->badge = badge;
    return 0;
}

int main(void) {
    capability_t root = {.object_id = 0x100ULL, .rights_mask = CAP_RIGHT_READ | CAP_RIGHT_WRITE, .badge = 0U};
    capability_t ro_child = {0};
    assert(cap_mint_derived(&root, CAP_RIGHT_READ, 42U, &ro_child) == 0);
    assert(ro_child.rights_mask == CAP_RIGHT_READ && ro_child.badge == 42U);
    /* Attempt privilege escalation (requesting GRANT right not in root) -> must be rejected (-2) */
    assert(cap_mint_derived(&ro_child, CAP_RIGHT_READ | CAP_RIGHT_WRITE, 1U, &ro_child) == -2);
    puts("OS CAPABILITY MONOTONIC ATTENUATION VERIFIED");
    return 0;
}

```
