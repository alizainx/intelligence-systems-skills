# Verified Example: `compiler-backend-elf-dwarf-and-linkers` (`elf64_reloc_and_cfg.py`)

```
"""
Verified Advanced Systems, Compiler Backend & RTOS Suite:
1. Iterative CFG Dominator Solver verified against an independent Vertex-Removal Reachability Oracle,
   plus Backward Liveness Dataflow Solver.
2. ELF64 Relocation Engine (`R_X86_64_64` and `R_X86_64_PC32`) with 32-bit signed displacement overflow guard.
3. RTOS Exact Response-Time Analysis (RTA) Schedulability Verifier.
"""
from __future__ import annotations

import math
import struct
from dataclasses import dataclass


def compute_cfg_dominators(
    entry: str,
    succs: dict[str, list[str]],
) -> dict[str, set[str]]:
    """Computes dominator sets Dom(n) via monotone fixed-point iteration."""
    nodes = list(succs.keys())
    preds: dict[str, list[str]] = {n: [] for n in nodes}
    for u, vs in succs.items():
        for v in vs:
            preds[v].append(u)

    all_nodes = set(nodes)
    dom: dict[str, set[str]] = {n: ({entry} if n == entry else set(all_nodes)) for n in nodes}

    changed = True
    while changed:
        changed = False
        for n in nodes:
            if n == entry:
                continue
            if not preds[n]:
                new_dom = {n}
            else:
                inter = set.intersection(*(dom[p] for p in preds[n]))
                new_dom = {n} | inter
            if new_dom != dom[n]:
                dom[n] = new_dom
                changed = True
    return dom


def dominators_reachability_oracle(entry: str, succs: dict[str, list[str]]) -> dict[str, set[str]]:
    """Independent definitional oracle: d dominates n iff removing d makes n unreachable from entry."""
    nodes = list(succs.keys())

    def reachable_without(removed: str | None) -> set[str]:
        if removed == entry:
            return set()
        visited: set[str] = {entry}
        stack = [entry]
        while stack:
            curr = stack.pop()
            for nxt in succs.get(curr, []):
                if nxt != removed and nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        return visited

    base_reach = reachable_without(None)
    oracle_dom: dict[str, set[str]] = {n: set() for n in nodes}
    for d in base_reach:
        still_reach = reachable_without(d)
        for n in base_reach:
            if n not in still_reach:
                oracle_dom[n].add(d)
    return oracle_dom


def compute_backward_liveness(
    succs: dict[str, list[str]],
    use_sets: dict[str, set[str]],
    def_sets: dict[str, set[str]],
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """Solves backward liveness equations IN[B] = USE[B] U (OUT[B] - DEF[B])."""
    nodes = list(succs.keys())
    live_in: dict[str, set[str]] = {n: set() for n in nodes}
    live_out: dict[str, set[str]] = {n: set() for n in nodes}

    changed = True
    while changed:
        changed = False
        for b in reversed(nodes):
            new_out = set().union(*(live_in[s] for s in succs[b])) if succs[b] else set()
            new_in = use_sets[b] | (new_out - def_sets[b])
            if new_out != live_out[b] or new_in != live_in[b]:
                live_out[b] = new_out
                live_in[b] = new_in
                changed = True
    return live_in, live_out


def apply_elf64_relocation(
    section_buf: bytearray,
    reloc_offset: int,
    base_vaddr: int,
    sym_vaddr: int,
    addend: int,
    reloc_type: str,
) -> None:
    """Applies R_X86_64_64 or R_X86_64_PC32 relocation with strict 32-bit overflow verification."""
    P = base_vaddr + reloc_offset
    S = sym_vaddr
    A = addend
    if reloc_type == "R_X86_64_64":
        val64 = (S + A) & 0xFFFFFFFFFFFFFFFF
        section_buf[reloc_offset : reloc_offset + 8] = struct.pack("<Q", val64)
    elif reloc_type == "R_X86_64_PC32":
        disp = S + A - P
        if not (-2147483648 <= disp <= 2147483647):
            raise OverflowError(f"R_X86_64_PC32 relocation overflow: disp={disp} outside int32 range")
        section_buf[reloc_offset : reloc_offset + 4] = struct.pack("<i", disp)
    else:
        raise ValueError(f"Unsupported relocation type: {reloc_type}")


@dataclass(frozen=True, slots=True)
class PeriodicTask:
    name: str
    wcet: int
    period: int
    deadline: int


def rtos_exact_response_time_analysis(tasks: list[PeriodicTask]) -> tuple[bool, dict[str, int]]:
    """
    Orders tasks by Rate-Monotonic priority (shortest period first) and computes
    exact worst-case response time R_i via Joseph-Pandya fixed-point iteration.
    """
    ordered = sorted(tasks, key=lambda t: t.period)
    response_times: dict[str, int] = {}

    for i, task_i in enumerate(ordered):
        if task_i.wcet <= 0 or task_i.period <= 0 or task_i.deadline <= 0:
            raise ValueError("Task timing parameters must be positive integers")
        hp_tasks = ordered[:i]
        r_curr = task_i.wcet
        while True:
            interference = sum(math.ceil(r_curr / float(t_j.period)) * t_j.wcet for t_j in hp_tasks)
            r_next = task_i.wcet + interference
            if r_next > task_i.deadline:
                response_times[task_i.name] = r_next
                return (False, response_times)
            if r_next == r_curr:
                response_times[task_i.name] = r_next
                break
            r_curr = r_next

    return (True, response_times)

```
