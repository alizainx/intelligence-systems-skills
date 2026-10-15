# Deep Engineering Reference: PowerShell (7.4 LTS+) CmdletBinding, StrictMode, Object Pipelines & ShouldProcess Safety (`powershell-object-pipeline`)

- **Language / Representation**: **PowerShell**
- **Taxonomic Classification**: `Object-Pipeline Shell & Automation Language (.NET CLR)`
- **Technical Relationship**: Cross-platform (`pwsh 7.4+`) command shell and scripting language built on .NET 8 that passes structured typed .NET objects (not raw text) through pipelines.
- **Governing Standards & Versions**: PowerShell 7.4 LTS Language Specification, PSScriptAnalyzer Rules (PowerShell 7.2 LTS / 7.4 LTS+)

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **PowerShell** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, `begin`/`process`/`end` pipeline blocks, and `[PSCustomObject]@{ ... }`. |
| 2 | **Type System & Inference** | .NET type accelerators (`[int]`, `[string]`, `[datetime]`, `[System.IO.FileInfo]`) and parameter validation (`[ValidateNotNullOrEmpty()]`, `[ValidateSet(...)]`). |
| 3 | **Memory Management** | Avoid `$arr += $item` inside loops ($O(N^2)$ array reallocation); assign pipeline output directly (`$res = foreach ($x in $items) { ... }`) or use `[System.Collections.Generic.List[object]]`. |
| 4 | **Concurrency & Async Programming** | `ForEach-Object -Parallel` runspace pools and `Start-ThreadJob`. |
| 5 | **Standard Library & Ecosystem** | PowerShell Gallery (`PSResourceGet`), `PSScriptAnalyzer`, `Pester` v5, `SecretManagement`. |
| 6 | **Build Systems & Package Management** | Module manifest (`.psd1`) with explicit `FunctionsToExport` (never `'*'`), `.psm1` implementation. |
| 7 | **Compiler / Interpreter Behavior** | DLR AST compilation to .NET LINQ expression trees and JIT bytecode; inspect AST via `[System.Management.Automation.Language.Parser]::ParseInput`. |
| 8 | **Debugging** | `Set-PSBreakpoint`, `Wait-Debugger`, `Trace-Command`, and `$Error[0].ScriptStackTrace`. |
| 9 | **Security** | Never use `Invoke-Expression` (`iex`), use `[PSCredential]`/`SecureString`, enforce ExecutionPolicy / Authenticode signing, and support `-WhatIf`/`-Confirm` via `$PSCmdlet.ShouldProcess`. |
| 10 | **Performance Optimization** | Filter left at the provider/cmdlet (`Get-ChildItem -Filter *.log` instead of piping to `Where-Object`), and use `.Where({})`/`.ForEach({})` methods on in-memory collections. |
| 11 | **Error Handling** | Distinguish non-terminating errors (`Write-Error`) from terminating errors (`$PSCmdlet.ThrowTerminatingError` / `throw`) and pass `-ErrorAction Stop` inside `try`/`catch`. |
| 12 | **Testing Methodologies** | Pester v5 (`Describe`, `Context`, `It`, `Should -Be`, `Should -Throw`). |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (PowerShell 7.2 LTS / 7.4 LTS+); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | Direct .NET class instantiation (`[System.Text.Encoding]::UTF8`) and native binary exit-code checking (`$LASTEXITCODE` / `$PSNativeCommandUseErrorActionPreference = $true`). |
| 18 | **Common Engineering Mistakes** | Polluting the output pipeline with accidental uncaptured return values (e.g., `ArrayList.Add()` returning an index; use `[void]` or `$null =`), and `==` instead of `-eq`. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/powershell-object-pipeline/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **PowerShell**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``Set-PSBreakpoint`, `Wait-Debugger`, `Trace-Command`, and `$Error[0].ScriptStackTrace`.`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Module manifest (`.psd1`) with explicit `FunctionsToExport` (never `'*'`), `.psm1` implementation.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Filter left at the provider/cmdlet (`Get-ChildItem -Filter *.log` instead of piping to `Where-Object`), and use `.Where({})`/`.ForEach({})` methods on in-memory collections.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (Never use `Invoke-Expression` (`iex`), use `[PSCredential]`/`SecureString`, enforce ExecutionPolicy / Authenticode signing, and support `-WhatIf`/`-Confirm` via `$PSCmdlet.ShouldProcess`.).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Pester v5 (`Describe`, `Context`, `It`, `Should -Be`, `Should -Throw`).).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (Direct .NET class instantiation (`[System.Text.Encoding]::UTF8`) and native binary exit-code checking (`$LASTEXITCODE` / `$PSNativeCommandUseErrorActionPreference = $true`).).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
