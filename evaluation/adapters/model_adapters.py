#!/usr/bin/env python3
"""Model-Agnostic Evaluation Adapters for intelligence-systems-skills.
Supports:
- Google Gemini (GEMINI_API_KEY)
- Anthropic Claude (ANTHROPIC_API_KEY)
- OpenAI GPT (OPENAI_API_KEY)
- Local LLMs (Ollama / vLLM via LOCAL_LLM_BASE_URL)
- Deterministic Harness Verification Fixture (clearly labeled as infrastructure validation, never fake live LLM output)
"""

import os
from typing import Dict, Any, List


def check_live_provider_status() -> List[Dict[str, Any]]:
    providers = [
        {"provider": "Google Gemini", "env_var": "GEMINI_API_KEY", "default_model": "gemini-2.5-pro"},
        {"provider": "Anthropic Claude", "env_var": "ANTHROPIC_API_KEY", "default_model": "claude-3-7-sonnet"},
        {"provider": "OpenAI GPT", "env_var": "OPENAI_API_KEY", "default_model": "gpt-4.1"},
        {"provider": "Local LLM (Ollama/vLLM)", "env_var": "LOCAL_LLM_BASE_URL", "default_model": "qwen2.5-coder:32b"},
    ]
    results = []
    for p in providers:
        has_creds = bool(os.environ.get(p["env_var"], "").strip())
        results.append({
            "provider": p["provider"],
            "model": p["default_model"],
            "credential_env": p["env_var"],
            "credentials_present": has_creds,
            "execution_status": "READY" if has_creds else "NOT EXECUTED (Air-Gapped Sandbox / No API Key Configured)",
        })
    return results
