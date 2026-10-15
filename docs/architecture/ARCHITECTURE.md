# Universal Software Intelligence Architecture (`intelligence-systems-skills`)

## 1. Architectural Overview (15 Core Components)

`intelligence-systems-skills` is an independent, model-agnostic software intelligence and low-level computer engineering skills ecosystem built around 15 modular components:

| # | Component | Repository Implementation Path |
| :--- | :--- | :--- |
| 1 | **Universal Skill Registry** | `schemas/skill-registry.json` (42 skills, dependencies, token estimates, composite workflows) |
| 2 | **Intelligent Skill Router** | `evaluation/skill_router.py` (language/OS/kernel/compiler detection, conflict checking, token budgeting) |
| 3 | **Programming Language Skill Engine** | `skills/systems-programming/` (7 skills) & `skills/programming-languages/` (9 skills) covering 50 languages |
| 4 | **Software Architecture Intelligence** | `skills/software-engineering/` (architecture, API idempotency, concurrency, static/dynamic analysis, legacy modernization) |
| 5 | **Compiler Engineering Intelligence** | `skills/compiler-engineering/` (frontend HM type inference, SSA IR/dataflow, register allocation, ELF64/DWARF backends, translation validation) |
| 6 | **Operating System Development Intelligence** | `skills/operating-systems/` (monolithic/microkernel/capability models, UEFI/Limine/Multiboot2, VMM/CoW/slab, SMP scheduler, VFS/WAL, PCIe/NVMe/DMA, init/security) |
| 7 | **Linux Development Intelligence** | `skills/linux-development/` (Kbuild/eBPF/VFS, Linux From Scratch 3-stage bootstrap, immutable distros/SAT solver, glibc/musl/relibc/Wayland) |
| 8 | **Kernel Engineering Intelligence** | `skills/kernel-engineering/` (`x86_64`/`AArch64`/`RISC-V` freestanding contracts, interrupt-safe seqlocks/RCU, seccomp-BPF/TOCTOU defense) |
| 9 | **Runtime and ABI Intelligence** | `skills/runtime-engineering/` & `shared/compiler/abi-and-calling-conventions.md` (tri-color GC, write barriers, System V/AAPCS64/RISC-V LP64 ABIs) |
| 10 | **Software Verification Engine** | `tests/run_all_verifications.py` & `tests/skill-validation/validate_skill.py` |
| 11 | **Cross-Model Evaluation Framework** | `evaluation/pipeline.py`, `evaluation/benchmarks/tasks.json`, `evaluation/graders/graders.py` |
| 12 | **Skill Dependency Resolver** | `SkillRouter.resolve_dependencies()` in `evaluation/skill_router.py` (topological sort + cycle detection) |
| 13 | **Automated Regression Testing** | `tests/regression/test_intelligence_systems.py` & `tests/integration/test_router_and_workflows.py` |
| 14 | **Controlled Skill Improvement Framework** | `shared/verification/verification-levels.md` & 10-step closed-loop regression gating |
| 15 | **Documentation and Reference System** | `docs/architecture/`, `docs/skill-catalog/`, `docs/integration/`, `docs/verification/` |

## 2. Progressive Disclosure & Context-Budget Architecture

- **Tier 0 (Registry & Frontmatter, ~80 tokens/skill)**: Indexed in `schemas/skill-registry.json` for fast routing.
- **Tier 1 (`SKILL.md`, ~104 lines / ~1,140 tokens/skill)**: Loaded only when activated by `SkillRouter.route()`; contains Sections A-E (Identity, Activation Criteria, Problem Understanding, Technical Reasoning Protocol, Verification Protocol).
- **Tier 2 (`references/` & `examples/`)**: Loaded on demand when deep ABI tables, memory models, or reference implementations are required.
- **Tier 3 (`tests/run_verification.py` & `validation.md`)**: Executed out-of-context in the verification sandbox.
