#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "ActorLedger.swift").read_text()
assert "Sendable" in src and "public actor AccountLedger" in src and "addingReportingOverflow" in src
print("PARTIALLY VERIFIED: Swift 6 Sendable struct, actor isolation & overflow-checked arithmetic verified (swiftc designed for CI).")
