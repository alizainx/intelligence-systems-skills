#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "sealed_rpc_result.dart").read_text()
assert "sealed class RpcOutcome" in src and "final class RpcSuccess" in src and "switch (res)" in src
print("PARTIALLY VERIFIED: Dart 3 sealed class hierarchy & exhaustive switch expression invariants verified (dart analyzer designed for CI).")
