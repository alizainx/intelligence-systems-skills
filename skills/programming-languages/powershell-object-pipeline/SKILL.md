---
name: powershell-object-pipeline
description: Develop, audit, and verify cross-platform PowerShell 7.4+ modules and automation scripts using Set-StrictMode -Version Latest, [CmdletBinding(SupportsShouldProcess)], typed parameter validation attributes, and Pester v5.
allowed-tools: execute_bash view_file write_to_file
---

# PowerShell (7.4 LTS+) CmdletBinding, StrictMode, Object Pipelines & ShouldProcess Safety

Develop, audit, and verify cross-platform PowerShell 7.4+ modules and automation scripts using Set-StrictMode -Version Latest, [CmdletBinding(SupportsShouldProcess)], typed parameter validation attributes, and Pester v5.

## A. Identity

- **Skill Name**: `powershell-object-pipeline`
- **Domain**: `programming-languages`
- **Language / Representation**: **PowerShell** (`Object-Pipeline Shell & Automation Language (.NET CLR)`)
- **Technical Relationship**: Cross-platform (`pwsh 7.4+`) command shell and scripting language built on .NET 8 that passes structured typed .NET objects (not raw text) through pipelines.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **PowerShell**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: PowerShell 7.4 LTS Language Specification, PSScriptAnalyzer Rules (PowerShell 7.2 LTS / 7.4 LTS+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Module manifest (`.psd1`) with explicit `FunctionsToExport` (never `'*'`), `.psm1` implementation.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **PowerShell** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **PowerShell**.

### Technical Triggers

- Files, build manifests, or prompts targeting **PowerShell** (`Invoke-SafeServiceAction.ps1`, `Module manifest (`.psd1`) with explicit `FunctionsToExport` (never `'*'`), `.psm1` implementation.`).

### Prerequisites

- Target language version (PowerShell 7.2 LTS / 7.4 LTS+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **PowerShell** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (PowerShell 7.2 LTS / 7.4 LTS+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Avoid `$arr += $item` inside loops ($O(N^2)$ array reallocation); assign pipeline output directly (`$res = foreach ($x in $items) { ... }`) or use `[System.Collections.Generic.List[object]]`.), type soundness limits (.NET type accelerators (`[int]`, `[string]`, `[datetime]`, `[System.IO.FileInfo]`) and parameter validation (`[ValidateNotNullOrEmpty()]`, `[ValidateSet(...)]`).), and concurrency hazards (`ForEach-Object -Parallel` runspace pools and `Start-ThreadJob`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce PowerShell 7.4 LTS Language Specification, PSScriptAnalyzer Rules.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, `begin`/`process`/`end` pipeline blocks, and `[PSCustomObject]@{ ... }`.
2. **Type System & Inference**: .NET type accelerators (`[int]`, `[string]`, `[datetime]`, `[System.IO.FileInfo]`) and parameter validation (`[ValidateNotNullOrEmpty()]`, `[ValidateSet(...)]`).
3. **Memory Management**: Avoid `$arr += $item` inside loops ($O(N^2)$ array reallocation); assign pipeline output directly (`$res = foreach ($x in $items) { ... }`) or use `[System.Collections.Generic.List[object]]`.
4. **Concurrency & Async Programming**: `ForEach-Object -Parallel` runspace pools and `Start-ThreadJob`.
5. **Standard Library & Ecosystem**: PowerShell Gallery (`PSResourceGet`), `PSScriptAnalyzer`, `Pester` v5, `SecretManagement`.
6. **Build Systems & Package Management**: Module manifest (`.psd1`) with explicit `FunctionsToExport` (never `'*'`), `.psm1` implementation.
7. **Compiler / Interpreter Behavior**: DLR AST compilation to .NET LINQ expression trees and JIT bytecode; inspect AST via `[System.Management.Automation.Language.Parser]::ParseInput`.
8. **Debugging & Observability**: `Set-PSBreakpoint`, `Wait-Debugger`, `Trace-Command`, and `$Error[0].ScriptStackTrace`.
9. **Security Hardening**: Never use `Invoke-Expression` (`iex`), use `[PSCredential]`/`SecureString`, enforce ExecutionPolicy / Authenticode signing, and support `-WhatIf`/`-Confirm` via `$PSCmdlet.ShouldProcess`.
10. **Performance Optimization**: Filter left at the provider/cmdlet (`Get-ChildItem -Filter *.log` instead of piping to `Where-Object`), and use `.Where({})`/`.ForEach({})` methods on in-memory collections.
11. **Error Handling Discipline**: Distinguish non-terminating errors (`Write-Error`) from terminating errors (`$PSCmdlet.ThrowTerminatingError` / `throw`) and pass `-ErrorAction Stop` inside `try`/`catch`.
12. **Testing Methodologies**: Pester v5 (`Describe`, `Context`, `It`, `Should -Be`, `Should -Throw`).
13. **Interoperability & Cross-Platform ABI**: Direct .NET class instantiation (`[System.Text.Encoding]::UTF8`) and native binary exit-code checking (`$LASTEXITCODE` / `$PSNativeCommandUseErrorActionPreference = $true`).
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/powershell-object-pipeline/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (PowerShell 7.2 LTS / 7.4 LTS+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in PowerShell**: Polluting the output pipeline with accidental uncaptured return values (e.g., `ArrayList.Add()` returning an index; use `[void]` or `$null =`), and `==` instead of `-eq`.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
