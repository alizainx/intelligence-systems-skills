#!/usr/bin/env python3
"""Master Verification Runner for intelligence-systems-skills.
Reads schemas/skill-registry.json, validates all 42 skills via validate_skill.py,
executes all 42 tests/run_verification.py scripts, and writes docs/verification/master_verification_results.json.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "schemas" / "skill-registry.json"
VALIDATOR_PATH = REPO_ROOT / "tests" / "skill-validation" / "validate_skill.py"


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    skills = registry["skills"]
    results = []
    passed = 0
    verified_count = 0
    partial_count = 0

    for s in skills:
        sdir = REPO_ROOT / "skills" / s["category"] / s["name"]
        t0 = time.perf_counter()
        r_val = subprocess.run(["python3", str(VALIDATOR_PATH), str(sdir)], capture_output=True, text=True)
        r_test = subprocess.run(["python3", str(sdir / "tests" / "run_verification.py")], capture_output=True, text=True)
        elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)

        ok = (r_val.returncode == 0) and (r_test.returncode == 0)
        out = r_test.stdout.strip()
        status = "PARTIALLY VERIFIED" if "PARTIALLY VERIFIED" in out else ("VERIFIED" if ok else "FAILED")
        if ok:
            passed += 1
            if status == "VERIFIED":
                verified_count += 1
            else:
                partial_count += 1

        results.append({
            "id": s["id"],
            "name": s["name"],
            "category": s["category"],
            "structural_valid": r_val.returncode == 0,
            "test_passed": r_test.returncode == 0,
            "status": status,
            "elapsed_ms": elapsed_ms,
            "output": out,
        })

    summary = {
        "repository": "intelligence-systems-skills",
        "total_skills": len(skills),
        "total_passed": passed,
        "fully_verified_native_execution": verified_count,
        "partially_verified_host_model_checked": partial_count,
        "failed": len(skills) - passed,
        "results": results,
    }
    out_file = REPO_ROOT / "docs" / "verification" / "master_verification_results.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"MASTER VERIFICATION SUMMARY: {passed}/{len(skills)} PASSED ({verified_count} VERIFIED, {partial_count} PARTIALLY VERIFIED)")
    return 0 if passed == len(skills) else 1


if __name__ == "__main__":
    sys.exit(main())
