# Cross-Model Compatibility & Integration Guide

`intelligence-systems-skills` is designed for model-agnostic portability across Gemini, Claude, OpenAI GPT, and Local LLMs without relying on vendor-specific prompt syntax or automatic skill discovery.

## 1. Explicit Loading & Routing Workflow

For agents that do not support automatic skill discovery, run the deterministic router to resolve and load the exact `SKILL.md` files for a task:

```bash
python3 evaluation/skill_router.py
```

## 2. Provider-Specific Integration Instructions

- **Google Gemini**: Register skills via `skills:save_skill` (`skill_dir`) or load via `lookup_skills` and `get_skill_resources`; execute `tests/run_verification.py` via `execute_bash`.
- **Anthropic Claude (Claude Code / API)**: Mount `skills/` under `.claude/skills/` or pass the router-selected `SKILL.md` files in the system prompt; bind verification to the `bash` tool.
- **OpenAI GPT (Codex / Responses API)**: Load `schemas/skill-registry.json` as the discovery index and inject selected `SKILL.md` files into `developer` instructions.
- **Local LLMs (Ollama / vLLM / llama.cpp)**: Use `SkillRouter(default_token_budget=6000).route(query, mode="C")` to enforce strict context-window budgets on smaller local models.
