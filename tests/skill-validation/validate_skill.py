#!/usr/bin/env python3
"""
Automated structural, frontmatter, and compliance validator for Engineering AI Skills.
Validates both platform skill-creator constraints and Universal Skill Architecture requirements.
"""

import json
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## A. Identity",
    "## B. Activation Criteria",
    "## C. Problem Understanding",
    "## D. Technical Reasoning Protocol",
    "## E. Verification Protocol",
]

REQUIRED_SUBDIRS = ["references", "examples", "tests"]


def validate_skill_dir(skill_dir: Path) -> dict:
    errors = []
    warnings = []
    skill_md = skill_dir / "SKILL.md"
    validation_md = skill_dir / "validation.md"

    if not skill_md.exists():
        return {"valid": False, "errors": ["Missing SKILL.md"], "warnings": []}

    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. Line count (< 500 lines)
    if len(lines) >= 500:
        errors.append(f"SKILL.md has {len(lines)} lines (must be < 500 lines).")

    # 2. Frontmatter validation
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter delimiter '---'.")
    else:
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            errors.append("Malformed YAML frontmatter (missing closing '---').")
        else:
            fm_text = parts[1]
            body_text = parts[2]
            fm = {}
            for line in fm_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()

            name = fm.get("name", "")
            desc = fm.get("description", "")
            if not re.match(r"^[a-z0-9]+(-[a-z0-9]+){0,5}$", name) or len(name) > 64:
                errors.append(
                    f"Invalid skill name '{name}': must be 1-6 words, lowercase a-z/0-9/hyphens, max 64 chars."
                )
            if name != skill_dir.name:
                errors.append(
                    f"Frontmatter name '{name}' does not match directory name '{skill_dir.name}'."
                )
            if not (20 <= len(desc) < 1024):
                errors.append(
                    f"Description length {len(desc)} out of bounds (must be 20..1023 chars)."
                )

            # 3. Forbidden characters (no em-dashes or en-dashes in SKILL.md)
            if "\u2014" in text or "\u2013" in text:
                errors.append("SKILL.md contains forbidden em-dash (—) or en-dash (–).")

            # 4. Blank line before lists check (outside code blocks)
            in_code_block = False
            for idx, line in enumerate(lines):
                if line.strip().startswith("```"):
                    in_code_block = not in_code_block
                    continue
                if in_code_block:
                    continue
                is_list_item = bool(re.match(r"^(\s*[-*+]\s+|\s*\d+\.\s+)", line))
                if is_list_item and idx > 0:
                    prev = lines[idx - 1]
                    prev_is_list = bool(
                        re.match(r"^(\s*[-*+]\s+|\s*\d+\.\s+)", prev)
                    )
                    if prev.strip() != "" and not prev_is_list and prev.strip() != "---":
                        errors.append(
                            f"Line {idx + 1}: Missing blank line before list item: '{line[:40]}...'"
                        )

            # 5. Required Universal Skill Architecture sections
            for sec in REQUIRED_SECTIONS:
                if sec not in body_text:
                    errors.append(f"Missing required architecture section: '{sec}'")

    # 6. Check multi-file structure
    for sub in REQUIRED_SUBDIRS:
        sub_path = skill_dir / sub
        if not sub_path.is_dir() or not any(sub_path.iterdir()):
            errors.append(f"Missing or empty required subdirectory: '{sub}/'")

    if not validation_md.exists():
        warnings.append("validation.md not found yet.")

    return {
        "skill_dir": str(skill_dir),
        "line_count": len(lines),
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <path-to-skill-dir>")
        sys.exit(2)
    target = Path(sys.argv[1])
    res = validate_skill_dir(target)
    print(json.dumps(res, indent=2))
    sys.exit(0 if res["valid"] else 1)
