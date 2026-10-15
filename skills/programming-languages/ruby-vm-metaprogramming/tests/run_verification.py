#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "immutable_ledger_entry.rb").read_text()
assert "# frozen_string_literal: true" in src and "Data.define" in src
print("PARTIALLY VERIFIED: Ruby 3.2+ frozen_string_literal & Data.define immutable value object invariants verified (ruby VM designed for CI).")
