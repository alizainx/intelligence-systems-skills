# Contributing to `intelligence-systems-skills`

1. Follow the workflow: `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW`.
2. Ensure every skill under `skills/<category>/<skill-name>/` includes `SKILL.md` (< 500 lines), `references/`, `examples/`, `tests/run_verification.py`, and `validation.md`.
3. Run `python3 tests/skill-validation/validate_skill.py <skill-dir>` and `python3 tests/run_all_verifications.py` before submitting a pull request.
