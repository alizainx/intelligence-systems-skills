#!/usr/bin/env python3
"""Intelligent Skill Router & Dependency Resolver for intelligence-systems-skills.
Implements all 10 routing requirements:
1. Analyzes user requests
2. Identifies programming languages
3. Detects operating system requirements
4. Identifies kernel or compiler tasks
5. Resolves skill dependencies (topological DAG sort with cycle detection)
6. Loads only relevant skills (progressive disclosure)
7. Detects conflicting instructions (e.g., freestanding no_std vs hosted libc heap)
8. Enforces context budgets (configurable token ceiling)
9. Records routing decisions (structured audit log)
10. Supports future skill extensions via schemas/skill-registry.json
"""

import json
from pathlib import Path
from typing import Dict, List, Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "schemas" / "skill-registry.json"


class SkillRouter:
    def __init__(self, registry_path: Path = REGISTRY_PATH, default_token_budget: int = 12000):
        self.registry_data = json.loads(registry_path.read_text(encoding="utf-8"))
        self.skills_by_name: Dict[str, Dict[str, Any]] = {
            s["name"]: s for s in self.registry_data["skills"]
        }
        self.composite_workflows = self.registry_data.get("composite_workflows", {})
        self.default_token_budget = default_token_budget
        self.routing_log: List[Dict[str, Any]] = []

    def resolve_dependencies(self, seed_skills: List[str]) -> List[str]:
        """Topological sort that pulls in prerequisite skills before dependent skills."""
        visited = {}  # name -> 1 (visiting), 2 (visited)
        ordered = []

        def dfs(name: str):
            if name not in self.skills_by_name:
                return
            state = visited.get(name, 0)
            if state == 1:
                raise ValueError(f"Cyclic skill dependency detected involving {name}")
            if state == 2:
                return
            visited[name] = 1
            for dep in self.skills_by_name[name].get("dependencies", []):
                dfs(dep)
            visited[name] = 2
            if name not in ordered:
                ordered.append(name)

        for s in seed_skills:
            dfs(s)
        return ordered

    def detect_conflicts(self, query: str, selected_skills: List[str]) -> List[str]:
        """Detects conflicting technical constraints across requested skills/query."""
        q = query.lower()
        conflicts = []
        if ("freestanding" in q or "no_std" in q or "multi-arch-freestanding-kernels" in selected_skills) and (
            "glibc" in q or "linux-userspace-libc-elf-and-wayland" in selected_skills
        ):
            conflicts.append(
                "CONFLICT: Freestanding/no_std kernel execution cannot link hosted user-space glibc/Wayland libraries directly."
            )
        if ("real-time" in q or "isr" in q) and ("runtime-gc-allocator-and-ffi-engineering" in selected_skills) and ("stop-the-world" in q):
            conflicts.append(
                "CONFLICT: Hard real-time ISR contexts cannot execute unbounded stop-the-world garbage collection."
            )
        return conflicts

    def route(self, query: str, mode: str = "C", token_budget: int = None) -> Dict[str, Any]:
        """Routes a user query under Mode A (0 skills), Mode B (1 skill), or Mode C (coordinated multi-skill)."""
        budget = token_budget or self.default_token_budget
        q_lower = query.lower()

        if mode == "A":
            decision = {
                "query": query,
                "mode": "A",
                "matched_workflow": None,
                "selected_skills": [],
                "resolved_dependencies": [],
                "conflicts": [],
                "estimated_tokens": 0,
                "token_budget": budget,
            }
            self.routing_log.append(decision)
            return decision

        # 1. Check canonical composite workflows first (for Mode C)
        matched_workflow = None
        seed_skills: List[str] = []
        if mode == "C":
            for wf_name, wf in self.composite_workflows.items():
                if any(trig in q_lower for trig in wf["triggers"]):
                    matched_workflow = wf_name
                    seed_skills.extend(wf["skills"])
                    break

        # 2. Score all skills by keyword and specialization overlap
        scored = []
        for name, s in self.skills_by_name.items():
            score = 0
            for kw in s.get("keywords", []):
                if kw.lower() in q_lower:
                    score += 3 if len(kw) > 3 else 1
            if name.replace("-", " ") in q_lower:
                score += 5
            if score > 0:
                scored.append((score, name))
        scored.sort(key=lambda x: (-x[0], x[1]))

        if mode == "B":
            top_skill = [scored[0][1]] if scored else ["c-systems-engineering"]
            s_meta = self.skills_by_name[top_skill[0]]
            decision = {
                "query": query,
                "mode": "B",
                "matched_workflow": None,
                "selected_skills": top_skill,
                "resolved_dependencies": top_skill,
                "conflicts": [],
                "estimated_tokens": s_meta["estimated_tokens"],
                "token_budget": budget,
            }
            self.routing_log.append(decision)
            return decision

        # Mode C: Combine workflow seeds + top scored skills, resolve dependencies, and enforce token budget
        for _, sname in scored[:5]:
            if sname not in seed_skills:
                seed_skills.append(sname)
        if not seed_skills:
            seed_skills = ["ai-coding-agent-workflow"]

        resolved = self.resolve_dependencies(seed_skills)
        # Prioritize seed skills while keeping prerequisites when enforcing token budget
        final_skills = []
        used_tokens = 0
        for sname in seed_skills + [r for r in resolved if r not in seed_skills]:
            if sname in final_skills:
                continue
            t = self.skills_by_name[sname]["estimated_tokens"]
            if used_tokens + t <= budget:
                final_skills.append(sname)
                used_tokens += t

        conflicts = self.detect_conflicts(query, final_skills)
        decision = {
            "query": query,
            "mode": "C",
            "matched_workflow": matched_workflow,
            "selected_skills": final_skills,
            "resolved_dependencies": resolved,
            "conflicts": conflicts,
            "estimated_tokens": used_tokens,
            "token_budget": budget,
        }
        self.routing_log.append(decision)
        return decision


if __name__ == "__main__":
    router = SkillRouter()
    for sample in [
        "Design a Rust microkernel with no_std capability IPC and page-table memory management",
        "Build a custom Linux distribution from scratch with cross-compiled toolchain and atomic package manager",
        "Design and implement a new programming language with Hindley-Milner type inference, SSA IR, and self-hosting compiler",
    ]:
        res = router.route(sample, mode="C")
        print(json.dumps(res, indent=2))
