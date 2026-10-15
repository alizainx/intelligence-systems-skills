# Verified Example: `cpu-microarchitecture-isa-and-mesi` (`isa_pipeline_mesi.c`)

```
/**
 * @file isa_pipeline_mesi.c
 * @brief Verified ISO C11 RISC-V B-Type Immediate Decoder, 5-Stage Pipeline Hazard/Forwarding Unit,
 *        and 4-Core MESI Cache Coherence Verifier enforcing the SWMR Invariant.
 */

#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

/* 1. RISC-V RV32I B-Type Immediate Decoder (imm[12|10:5|4:1|11], sign-extended from bit 12) */
static int32_t rv32i_decode_b_imm(uint32_t inst) {
    uint32_t bit12   = (inst >> 31U) & 0x1U;
    uint32_t bit11   = (inst >> 7U)  & 0x1U;
    uint32_t bits10_5 = (inst >> 25U) & 0x3FU;
    uint32_t bits4_1  = (inst >> 8U)  & 0xFU;

    uint32_t u_imm = (bit12 << 12U) | (bit11 << 11U) | (bits10_5 << 5U) | (bits4_1 << 1U);
    /* Arithmetic sign extension from 13-bit signed value without UB */
    if ((u_imm & (1U << 12U)) != 0U) {
        u_imm |= 0xFFFFE000U;
    }
    return (int32_t)u_imm;
}

/* 2. 5-Stage Pipeline Forwarding & Load-Use Hazard Detector */
typedef enum {
    FWD_NONE = 0,
    FWD_FROM_MEM_WB = 1,
    FWD_FROM_EX_MEM = 2
} fwd_sel_t;

static fwd_sel_t pipeline_resolve_forward(
    uint8_t id_ex_rs,
    bool ex_mem_reg_write,
    uint8_t ex_mem_rd,
    bool mem_wb_reg_write,
    uint8_t mem_wb_rd
) {
    /* Younger EX/MEM stage takes strict priority; x0 (rd == 0) is NEVER forwarded */
    if (ex_mem_reg_write && (ex_mem_rd != 0U) && (ex_mem_rd == id_ex_rs)) {
        return FWD_FROM_EX_MEM;
    }
    if (mem_wb_reg_write && (mem_wb_rd != 0U) && (mem_wb_rd == id_ex_rs)) {
        return FWD_FROM_MEM_WB;
    }
    return FWD_NONE;
}

static bool pipeline_detect_load_use_stall(
    bool id_ex_mem_read,
    uint8_t id_ex_rd,
    uint8_t if_id_rs1,
    uint8_t if_id_rs2
) {
    if (!id_ex_mem_read || id_ex_rd == 0U) {
        return false;
    }
    return (id_ex_rd == if_id_rs1) || (id_ex_rd == if_id_rs2);
}

/* 3. 4-Core Snooping MESI Cache Coherence Protocol State Machine */
typedef enum {
    MESI_I = 0,
    MESI_S = 1,
    MESI_E = 2,
    MESI_M = 3
} mesi_state_t;

typedef struct {
    mesi_state_t state[4];
    uint32_t line_data[4];
    uint32_t mem_data;
} mesi_cluster_t;

static void mesi_assert_swmr_invariant(const mesi_cluster_t *c) {
    size_t m_count = 0U;
    size_t e_count = 0U;
    size_t s_count = 0U;
    for (size_t i = 0U; i < 4U; ++i) {
        if (c->state[i] == MESI_M) m_count++;
        if (c->state[i] == MESI_E) e_count++;
        if (c->state[i] == MESI_S) s_count++;
    }
    /* SWMR Invariant: At most one M or E, and if M or E > 0 then S must be 0 */
    assert(m_count <= 1U && e_count <= 1U);
    assert((m_count + e_count) <= 1U);
    if ((m_count + e_count) == 1U) {
        assert(s_count == 0U);
    }
    /* All Shared copies must equal clean backing memory */
    for (size_t i = 0U; i < 4U; ++i) {
        if (c->state[i] == MESI_S || c->state[i] == MESI_E) {
            assert(c->line_data[i] == c->mem_data);
        }
    }
}

static uint32_t mesi_cpu_read(mesi_cluster_t *c, size_t core) {
    assert(core < 4U);
    if (c->state[core] == MESI_I) {
        /* Broadcast BusRd */
        bool other_cached = false;
        for (size_t i = 0U; i < 4U; ++i) {
            if (i != core && c->state[i] != MESI_I) {
                other_cached = true;
                if (c->state[i] == MESI_M) {
                    /* Flush dirty line to memory and downgrade to S */
                    c->mem_data = c->line_data[i];
                }
                c->state[i] = MESI_S;
            }
        }
        c->line_data[core] = c->mem_data;
        c->state[core] = other_cached ? MESI_S : MESI_E;
    }
    mesi_assert_swmr_invariant(c);
    return c->line_data[core];
}

static void mesi_cpu_write(mesi_cluster_t *c, size_t core, uint32_t val) {
    assert(core < 4U);
    /* Broadcast BusRdX / BusUpgr: invalidate all other cores (flushing M if present) */
    for (size_t i = 0U; i < 4U; ++i) {
        if (i != core) {
            if (c->state[i] == MESI_M) {
                c->mem_data = c->line_data[i];
            }
            c->state[i] = MESI_I;
        }
    }
    c->line_data[core] = val;
    c->state[core] = MESI_M;
    mesi_assert_swmr_invariant(c);
}

int main(void) {
    /* 1. Test RV32I B-type negative branch offset (-4 bytes: all 1s in imm[12:1]) */
    uint32_t beq_minus_4 = (1U << 31U) | (0x3FU << 25U) | (0xEU << 8U) | (1U << 7U) | 0x63U;
    assert(rv32i_decode_b_imm(beq_minus_4) == -4);

    /* 2. Test Pipeline Forwarding: x0 suppression & EX/MEM priority over MEM/WB */
    assert(pipeline_resolve_forward(0U, true, 0U, true, 0U) == FWD_NONE);
    assert(pipeline_resolve_forward(5U, true, 5U, true, 5U) == FWD_FROM_EX_MEM);
    assert(pipeline_resolve_forward(5U, true, 3U, true, 5U) == FWD_FROM_MEM_WB);
    assert(pipeline_detect_load_use_stall(true, 4U, 4U, 1U) == true);
    assert(pipeline_detect_load_use_stall(true, 0U, 0U, 1U) == false);

    /* 3. Test 4-Core MESI Coherence Protocol transitions & SWMR invariant */
    mesi_cluster_t cluster = {.mem_data = 100U};
    /* First read on Core 0 -> Exclusive (E) */
    assert(mesi_cpu_read(&cluster, 0U) == 100U && cluster.state[0] == MESI_E);
    /* Read on Core 1 -> Both downgrade/transition to Shared (S) */
    assert(mesi_cpu_read(&cluster, 1U) == 100U);
    assert(cluster.state[0] == MESI_S && cluster.state[1] == MESI_S);
    /* Write on Core 2 -> Core 2 becomes M, Cores 0 and 1 invalidated (I) */
    mesi_cpu_write(&cluster, 2U, 0xCAFEBABEU);
    assert(cluster.state[2] == MESI_M && cluster.state[0] == MESI_I && cluster.state[1] == MESI_I);
    /* Read on Core 3 -> Core 2 flushes 0xCAFEBABE to memory and transitions to S; Core 3 gets 0xCAFEBABE in S */
    assert(mesi_cpu_read(&cluster, 3U) == 0xCAFEBABEU);
    assert(cluster.state[2] == MESI_S && cluster.state[3] == MESI_S && cluster.mem_data == 0xCAFEBABEU);

    printf("ALL COMPUTER ARCHITECTURE RV32I, PIPELINE HAZARD & MESI COHERENCE TESTS PASSED\n");
    return 0;
}

```
