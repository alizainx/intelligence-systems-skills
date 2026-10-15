# Verified Example: `linux-kernel-modules-ebpf-and-vfs` (`ebpf_bounds_verifier.py`)

```
from __future__ import annotations

def verify_ebpf_packet_access(insns: list[tuple[str, int]], max_pkt_offset: int) -> tuple[bool, str]:
    """
    Models the Linux eBPF Verifier packet pointer bounds check rule:
    Every load `LD_PKT(off, size)` at offset `off + size` MUST be preceded by a dominating
    bounds check `JGT_DATA_END(checked_len)` with `checked_len >= off + size`!
    """
    verified_pkt_bound = 0
    for idx, (op, arg) in enumerate(insns):
        if op == "CHECK_DATA_END":
            verified_pkt_bound = max(verified_pkt_bound, arg)
        elif op == "ADD_PKT_PTR_UNBOUNDED":
            verified_pkt_bound = 0  # Pointer arithmetic invalidates prior range proof!
        elif op == "LD_PKT":
            if arg > verified_pkt_bound:
                return (False, f"Insn {idx}: invalid access to packet, off+size={arg} > verified_bound={verified_pkt_bound}")
    return (True, "eBPF verifier passed")

```
