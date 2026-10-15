#!/usr/bin/env python3
"""End-to-End Regression Test Suite for intelligence-systems-skills."""

import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def main():
    # 1. Verify registry and language coverage matrix
    reg = json.loads((REPO_ROOT / "schemas" / "skill-registry.json").read_text(encoding="utf-8"))
    assert reg["total_skills"] == 42
    lang_cov = json.loads((REPO_ROOT / "schemas" / "language-coverage-matrix.json").read_text(encoding="utf-8"))
    assert len(lang_cov["languages"]) == 50

    # 2. Run integration tests
    subprocess.run(["python3", str(REPO_ROOT / "tests" / "integration" / "test_router_and_workflows.py")], check=True)

    # 3. Verify zero hardcoded API keys across repository
    forbidden_patterns = ["AIzaSy", "sk-ant-", "sk-proj-"]
    for s in reg["skills"]:
        skill_md = (REPO_ROOT / s["path"]).read_text(encoding="utf-8")
        for pat in forbidden_patterns:
            assert pat not in skill_md, f"Secret pattern {pat} found in {s['path']}"

    print("REGRESSION SUITE PASSED: 42 skills, 50 languages, router workflows, and secret scan verified.")


if __name__ == "__main__":
    main()
