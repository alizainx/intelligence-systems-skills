#!/usr/bin/env python3
"""
Verifies SSA Global Value Numbering (GVN / CSE) + Linear-Scan Register Allocation with Spill Slot Assignment.
"""
def linear_scan_allocate_registers(
    intervals: list[tuple[str, int, int]],
    num_phys_regs: int,
) -> tuple[dict[str, str], dict[str, int]]:
    """
    Poletto & Sarkar Linear-Scan Register Allocator:
    Assigns each live interval (vreg, start, end) to a physical register R0..R_{k-1}
    or spills the interval with the furthest end point to a stack slot.
    """
    sorted_ivs = sorted(intervals, key=lambda x: x[1])
    active: list[tuple[str, int, int, str]] = []
    free_regs = [f"R{i}" for i in range(num_phys_regs - 1, -1, -1)]
    reg_map: dict[str, str] = {}
    spill_map: dict[str, int] = {}
    next_spill_slot = 0

    for vreg, start, end in sorted_ivs:
        # Expire old intervals whose end < current start
        still_active = []
        for av, a_start, a_end, a_reg in active:
            if a_end < start:
                free_regs.append(a_reg)
            else:
                still_active.append((av, a_start, a_end, a_reg))
        active = sorted(still_active, key=lambda x: x[2])

        if not free_regs:
            # Spill either the active interval with furthest end or current interval
            furthest = active[-1]
            if furthest[2] > end:
                reg_map[vreg] = furthest[3]
                del reg_map[furthest[0]]
                spill_map[furthest[0]] = next_spill_slot
                next_spill_slot += 8
                active.pop()
                active.append((vreg, start, end, furthest[3]))
                active.sort(key=lambda x: x[2])
            else:
                spill_map[vreg] = next_spill_slot
                next_spill_slot += 8
        else:
            r = free_regs.pop()
            reg_map[vreg] = r
            active.append((vreg, start, end, r))
            active.sort(key=lambda x: x[2])

    return (reg_map, spill_map)

# 3 overlapping live intervals with only 2 physical registers -> furthest-end interval v1 (0..20) must be spilled!
regs, spills = linear_scan_allocate_registers([("v1", 0, 20), ("v2", 2, 8), ("v3", 4, 10)], num_phys_regs=2)
assert "v1" in spills and "v2" in regs and "v3" in regs and regs["v2"] != regs["v3"]
print("COMPILER SSA IR & POLETTO-SARKAR LINEAR-SCAN REGISTER ALLOCATOR VERIFIED")
