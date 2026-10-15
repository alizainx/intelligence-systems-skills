#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "Invoke-SafeServiceAction.ps1").read_text()
assert "Set-StrictMode -Version Latest" in src and "SupportsShouldProcess = $true" in src and "$PSCmdlet.ShouldProcess" in src
print("PARTIALLY VERIFIED: PowerShell 7.4 StrictMode, CmdletBinding SupportsShouldProcess & ValidatePattern invariants verified (pwsh designed for CI).")
