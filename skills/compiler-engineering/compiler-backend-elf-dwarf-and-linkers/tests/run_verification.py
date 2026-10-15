#!/usr/bin/env python3
"""
Verification runner for `advanced-systems-and-llvm-ir`.
"""
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
MOD_PATH = HERE / "examples" / "elf64_reloc_and_cfg.py"

def main() -> int:
    ns: dict = {}
    exec(MOD_PATH.read_text(), ns)
    compute_dom = ns["compute_cfg_dominators"]
    dom_oracle = ns["dominators_reachability_oracle"]
    compute_live = ns["compute_backward_liveness"]
    apply_reloc = ns["apply_elf64_relocation"]
    PeriodicTask = ns["PeriodicTask"]
    rtos_rta = ns["rtos_exact_response_time_analysis"]

    # 1. CFG Dominators on loop + diamond graph vs independent vertex-removal reachability oracle
    cfg = {
        "B0": ["B1"],
        "B1": ["B2", "B3"],
        "B2": ["B4"],
        "B3": ["B4"],
        "B4": ["B1", "B5"],
        "B5": [],
    }
    dom_fp = compute_dom("B0", cfg)
    dom_ref = dom_oracle("B0", cfg)
    assert dom_fp == dom_ref, f"Dominator mismatch: {dom_fp} != {dom_ref}"

    # 2. Backward liveness across loop back-edge B4 -> B1
    use_sets = {"B0": set(), "B1": {"i"}, "B2": {"x"}, "B3": {"y"}, "B4": {"i", "acc"}, "B5": {"acc"}}
    def_sets = {"B0": {"i", "x", "y", "acc"}, "B1": set(), "B2": {"acc"}, "B3": {"acc"}, "B4": {"i"}, "B5": set()}
    live_in, live_out = compute_live(cfg, use_sets, def_sets)
    assert {"i", "x", "y"}.issubset(live_in["B1"])
    assert "acc" in live_out["B4"]

    # 3. ELF64 R_X86_64_PC32 relocation & >2 GiB overflow rejection
    buf = bytearray(16)
    apply_reloc(buf, reloc_offset=4, base_vaddr=0x401000, sym_vaddr=0x402000, addend=-4, reloc_type="R_X86_64_PC32")
    disp = struct.unpack("<i", buf[4:8])[0]
    assert disp == (0x402000 - 4 - 0x401004)

    ovf_caught = False
    try:
        apply_reloc(buf, reloc_offset=4, base_vaddr=0x401000, sym_vaddr=0x100401000, addend=0, reloc_type="R_X86_64_PC32")
    except OverflowError:
        ovf_caught = True
    assert ovf_caught, "Failed to catch >2 GiB R_X86_64_PC32 relocation overflow"

    # 4. RTOS Exact RTA: Harmonic task set with U = 0.90 (> Liu-Layland 0.7798) is schedulable!
    harmonic_tasks = [
        PeriodicTask("T1", wcet=3, period=10, deadline=10),
        PeriodicTask("T2", wcet=6, period=20, deadline=20),
        PeriodicTask("T3", wcet=12, period=40, deadline=40),
    ]
    sched_ok, r_times = rtos_rta(harmonic_tasks)
    assert sched_ok and r_times == {"T1": 3, "T2": 9, "T3": 36}

    # Overloaded task set fails deadline
    bad_tasks = [
        PeriodicTask("T1", wcet=6, period=10, deadline=10),
        PeriodicTask("T2", wcet=7, period=15, deadline=15),
    ]
    sched_bad, _ = rtos_rta(bad_tasks)
    assert not sched_bad

    print(f"ALL ADVANCED SYSTEMS CFG DOMINATOR, ELF64 RELOCATION & RTOS RTA TESTS PASSED (RTA={r_times})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
