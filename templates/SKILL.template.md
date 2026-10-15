---
name: template-systems-skill
description: Actionable software, OS, Linux, kernel, or compiler engineering skill template. Use when implementing or verifying systems components in this specialization.
allowed-tools: execute_bash view_file write_to_file
---

# Template Systems Skill

## A. Identity

- **Skill Name**: `template-systems-skill`
- **Domain**: Target Domain
- **Specialization**: Target Specialization
- **Version**: `1.0.0`
- **Purpose**: Concrete software/systems problem solved and verified
- **Supported Tasks**: Implementation, static/dynamic verification, debugging, security audit
- **Required Knowledge**: Governing standards, ABI/ISA specifications, memory models
- **Dependencies**: Compilers, assemblers, linkers, or runtimes
- **Compatibility Requirements**: Model-agnostic Markdown + executable verification harness

## B. Activation Criteria

### When to Use

- Activate when implementing, refactoring, debugging, or verifying systems in this domain.

### Technical Triggers

- Domain-specific file extensions, headers, ABIs, or compiler flags.

### Prerequisites

- Target architecture, OS/runtime mode, and toolchain specification.

### When NOT to Use

- Do not activate for unrelated domains or when a narrower target skill applies.

## C. Problem Understanding

1. **Identify the Engineering Problem**: Define the exact software, kernel, or compiler invariant.
2. **Extract Explicit Requirements**: Record APIs, ABIs, and target constraints.
3. **Identify Hidden Technical Constraints**: Surface UB, race conditions, alignment, or calling-convention hazards.
4. **Determine Environmental Limitations**: Probe installed compilers, linkers, and runtimes.
5. **Identify Applicable Standards**: Reference ISO, POSIX, System V ABI, ELF64, or ISA manuals.
6. **Separate Known Facts from Assumptions**: Partition verified facts from disclosed assumptions.
7. **Identify Missing Critical Information**: State safe defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Define compiler, sanitizer, and test pass criteria.

## D. Technical Reasoning Protocol

Follow the disciplined `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` workflow across 10 steps:

1. **Define Invariants**: Formulate state, type, and memory lifetime invariants.
2. **Establish Target & ABI Assumptions**: Document word size, endianness, privilege level, and execution context.
3. **Select Models & Data Structures**: Choose deterministic, bounds-safe representations.
4. **Identify Alternatives**: Compare design options across latency, memory footprint, and safety.
5. **Evaluate Trade-Offs**: Quantify complexity ($O(\cdot)$) and resource bounds.
6. **Select Justified Approach**: Commit to the simplest verifiable design.
7. **Implement Solution**: Write clean, self-contained, warning-free code.
8. **Verify Intermediate Results**: Check intermediate types, offsets, and invariants.
9. **Validate Against Requirements**: Run compilers, sanitizers, and test suites.
10. **Document Limitations**: Record target-platform or cross-compilation scope.

## E. Verification Protocol

- Execute structural, compilation, unit, boundary, and sanitizer checks via `tests/run_verification.py`.
