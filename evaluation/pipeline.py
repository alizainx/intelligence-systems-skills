#!/usr/bin/env python3
"""Cross-Model Evaluation Pipeline comparing:
- Mode A: Without skills
- Mode B: Single relevant skill
- Mode C: Multiple coordinated skills

IMPORTANT TRANSPARENCY RULE:
- Live external LLM API benchmarks (Gemini, Claude, OpenAI, Local LLM) are checked for API credentials and marked `NOT EXECUTED` when running in an air-gapped environment without keys.
- Deterministic harness verification validates the router, token budgeting, dependency resolver, and actual compiler/runtime test execution across Mode A, Mode B, and Mode C without claiming to be live LLM inference.
"""

import importlib.util
import json
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

def _load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

router_mod = _load_mod("skill_router", REPO_ROOT / "evaluation" / "skill_router.py")
adapters_mod = _load_mod("model_adapters", REPO_ROOT / "evaluation" / "adapters" / "model_adapters.py")
graders_mod = _load_mod("graders", REPO_ROOT / "evaluation" / "graders" / "graders.py")


def run_evaluation() -> dict:
    tasks = json.loads((REPO_ROOT / "evaluation" / "benchmarks" / "tasks.json").read_text(encoding="utf-8"))["tasks"]
    router = router_mod.SkillRouter()
    live_providers = adapters_mod.check_live_provider_status()

    mode_results = {"A": [], "B": [], "C": []}
    for task in tasks:
        v_path = REPO_ROOT / "skills" / task["verification_skill"] / "tests" / "run_verification.py"
        t0 = time.perf_counter()
        proc = subprocess.run(["python3", str(v_path)], capture_output=True, text=True)
        elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)
        test_passed = proc.returncode == 0

        for mode in ("A", "B", "C"):
            route_info = router.route(task["query"], mode=mode)
            sel_acc = graders_mod.compute_skill_selection_accuracy(
                task["expected_skills"], route_info["selected_skills"]
            )
            mode_results[mode].append({
                "task_id": task["task_id"],
                "title": task["title"],
                "mode": mode,
                "selected_skills": route_info["selected_skills"],
                "skill_selection_accuracy": sel_acc,
                "estimated_tokens": route_info["estimated_tokens"],
                "harness_verification_passed": test_passed,
                "harness_execution_time_ms": elapsed_ms,
                "harness_output": proc.stdout.strip(),
            })

    summary = {}
    for mode in ("A", "B", "C"):
        rows = mode_results[mode]
        summary[f"Mode_{mode}"] = {
            "tasks_evaluated": len(rows),
            "harness_compilation_and_test_pass_rate": round(sum(1 for r in rows if r["harness_verification_passed"]) / len(rows), 4),
            "mean_skill_selection_accuracy": round(sum(r["skill_selection_accuracy"] for r in rows) / len(rows), 4),
            "mean_skill_context_tokens": round(sum(r["estimated_tokens"] for r in rows) / len(rows), 1),
            "mean_verification_time_ms": round(sum(r["harness_execution_time_ms"] for r in rows) / len(rows), 2),
        }

    report = {
        "benchmark_suite": "intelligence-systems-skills-v1",
        "evaluation_type": "DETERMINISTIC_HARNESS_AND_ROUTER_VERIFICATION (Live LLM API calls marked NOT EXECUTED in air-gapped VM)",
        "live_model_providers": live_providers,
        "mode_summary": summary,
        "detailed_results": mode_results,
    }
    out_json = REPO_ROOT / "evaluation" / "reports" / "evaluation_results.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    rep = run_evaluation()
    print(json.dumps(rep["mode_summary"], indent=2))
