#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

#define PTE_PRESENT (1U << 0U)
#define PTE_WRITABLE (1U << 1U)
#define PTE_COW     (1U << 9U)

typedef struct {
    uint32_t refcount[16];
    uint32_t pte_flags[4];
    uint8_t  pTE_frame[4];
} cow_vmm_t;

/* Handles a Write Page Fault on a Copy-on-Write (CoW) page:
 * - If refcount > 1: allocate a fresh frame, decrement old frame refcount, map new frame RW.
 * - If refcount == 1: simply promote existing frame to PTE_WRITABLE and clear PTE_COW!
 */
static int vmm_handle_cow_fault(cow_vmm_t *vmm, size_t vpn, uint8_t fresh_frame) {
    if (!vmm || vpn >= 4U || fresh_frame >= 16U) return -1;
    uint32_t flags = vmm->pte_flags[vpn];
    if ((flags & PTE_PRESENT) == 0U || (flags & PTE_COW) == 0U) return -2;
    uint8_t old_frame = vmm->pTE_frame[vpn];
    assert(vmm->refcount[old_frame] >= 1U);
    if (vmm->refcount[old_frame] > 1U) {
        vmm->refcount[old_frame] -= 1U;
        vmm->pTE_frame[vpn] = fresh_frame;
        vmm->refcount[fresh_frame] = 1U;
    }
    vmm->pte_flags[vpn] = (flags & ~PTE_COW) | PTE_WRITABLE;
    return 0;
}

int main(void) {
    cow_vmm_t vmm = {0};
    /* Parent (vpn 0) and Child (vpn 1) share physical frame 5 after fork() */
    vmm.pTE_frame[0] = 5U; vmm.pte_flags[0] = PTE_PRESENT | PTE_COW;
    vmm.pTE_frame[1] = 5U; vmm.pte_flags[1] = PTE_PRESENT | PTE_COW;
    vmm.refcount[5] = 2U;

    /* Child writes to vpn 1 -> copies to frame 6, frame 5 refcount drops to 1 */
    assert(vmm_handle_cow_fault(&vmm, 1U, 6U) == 0);
    assert(vmm.pTE_frame[1] == 6U && (vmm.pte_flags[1] & PTE_WRITABLE) != 0U && vmm.refcount[5] == 1U);

    /* Parent writes to vpn 0 -> refcount[5] is now 1, so frame 5 is promoted in-place to RW! */
    assert(vmm_handle_cow_fault(&vmm, 0U, 7U) == 0);
    assert(vmm.pTE_frame[0] == 5U && (vmm.pte_flags[0] & PTE_WRITABLE) != 0U && vmm.refcount[5] == 1U);
    puts("OS VMM COPY-ON-WRITE (CoW) PAGE FAULT HANDLER VERIFIED");
    return 0;
}
