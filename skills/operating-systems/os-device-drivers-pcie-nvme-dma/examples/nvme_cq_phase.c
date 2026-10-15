#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    uint16_t cid;
    uint16_t status_and_phase; /* Bit 0 is Phase Tag (P) */
} nvme_cqe_t;

/* Polls NVMe Completion Queue (CQ) entry using the hardware Phase Tag (P) inversion protocol:
 * Phase bit flips (1 -> 0 -> 1) on every full wrap around the CQ ring!
 */
static bool nvme_cq_poll(const nvme_cqe_t *cq, size_t cq_len, size_t *inout_head, uint8_t *inout_expected_phase, uint16_t *out_cid) {
    size_t h = *inout_head;
    uint8_t exp_p = *inout_expected_phase;
    uint16_t cqe_p = (uint16_t)(cq[h].status_and_phase & 1U);
    if (cqe_p != exp_p) {
        return false; /* Entry not yet written by NVMe controller DMA */
    }
    *out_cid = cq[h].cid;
    h += 1U;
    if (h == cq_len) {
        h = 0U;
        *inout_expected_phase = (uint8_t)(exp_p ^ 1U); /* Invert expected phase on wrap-around! */
    }
    *inout_head = h;
    return true;
}

int main(void) {
    nvme_cqe_t cq[2] = {{0}, {0}};
    size_t head = 0U;
    uint8_t phase = 1U;
    uint16_t cid = 0U;

    assert(!nvme_cq_poll(cq, 2U, &head, &phase, &cid));
    cq[0].cid = 10U; cq[0].status_and_phase = 1U;
    cq[1].cid = 11U; cq[1].status_and_phase = 1U;
    assert(nvme_cq_poll(cq, 2U, &head, &phase, &cid) && cid == 10U);
    assert(nvme_cq_poll(cq, 2U, &head, &phase, &cid) && cid == 11U);
    /* Head wrapped to 0, expected phase flipped to 0! Old phase=1 entry at cq[0] must NOT be re-consumed! */
    assert(head == 0U && phase == 0U);
    assert(!nvme_cq_poll(cq, 2U, &head, &phase, &cid));
    /* Controller writes new completion at slot 0 with inverted phase=0 */
    cq[0].cid = 12U; cq[0].status_and_phase = 0U;
    assert(nvme_cq_poll(cq, 2U, &head, &phase, &cid) && cid == 12U);
    puts("OS NVME COMPLETION QUEUE PHASE-BIT WRAP PROTOCOL VERIFIED");
    return 0;
}
