#!/usr/bin/env python3
"""Objective Benchmark Grader for intelligence-systems-skills."""

from typing import Dict, Any, List


def compute_skill_selection_accuracy(expected: List[str], selected: List[str]) -> float:
    if not expected:
        return 1.0
    hits = sum(1 for e in expected if e in selected)
    return round(hits / len(expected), 4)
