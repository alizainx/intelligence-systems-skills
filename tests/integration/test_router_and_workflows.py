#!/usr/bin/env python3
"""Integration tests for the Intelligent Skill Router, Dependency Resolver, and Conflict Detector."""

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("skill_router", str(REPO_ROOT / "evaluation" / "skill_router.py"))
router_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router_mod)


def main():
    router = router_mod.SkillRouter()

    # 1. Verify Rust microkernel workflow activation
    r1 = router.route("Build a Rust microkernel with no_std and page tables", mode="C")
    assert r1["matched_workflow"] == "rust_microkernel"
    assert "rust-ownership-and-nostd" in r1["selected_skills"]
    assert "os-architecture-and-capability-models" in r1["selected_skills"]
    assert "multi-arch-freestanding-kernels" in r1["selected_skills"]

    # 2. Verify Linux distribution workflow activation
    r2 = router.route("Create a custom Linux distribution from scratch with toolchain bootstrap", mode="C")
    assert r2["matched_workflow"] == "linux_distribution"
    assert "linux-from-scratch-toolchain-bootstrap" in r2["selected_skills"]
    assert "linux-distribution-and-immutable-os" in r2["selected_skills"]

    # 3. Verify New programming language workflow activation
    r3 = router.route("Design a new programming language with type inference and SSA IR", mode="C")
    assert r3["matched_workflow"] == "new_programming_language"
    assert "language-design-and-ownership-semantics" in r3["selected_skills"]
    assert "compiler-frontend-lexer-parser-typechecker" in r3["selected_skills"]

    # 4. Verify conflict detection between freestanding no_std and hosted glibc
    r4 = router.route("Write a freestanding no_std kernel that calls glibc and Wayland client APIs", mode="C")
    assert len(r4["conflicts"]) >= 1

    # 5. Verify context token budget enforcement
    r5 = router.route("Design a new programming language with type inference", mode="C", token_budget=2500)
    assert r5["estimated_tokens"] <= 2500 and len(r5["selected_skills"]) >= 1

    print("INTEGRATION TESTS PASSED: Skill Router, Dependency DAG, Conflict Detector & Token Budgets verified.")


if __name__ == "__main__":
    main()
