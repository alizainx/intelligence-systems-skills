# `intelligence-systems-skills`

**Universal Programming, Operating Systems, Linux, Kernel & Compiler Engineering Intelligence**

`intelligence-systems-skills` is an independent, standalone, model-agnostic AI Skills Ecosystem engineered for systems programming, 50 programming/specialized languages, operating system kernels, Linux distributions (including Linux From Scratch and non-systemd/musl/relibc systems), multi-architecture kernel engineering (`x86_64`, `AArch64`, `RISC-V`), compiler toolchains, programming language design, runtime garbage collection, and disciplined AI coding workflows (`UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW`).


## Key Metrics & Verification Summary

- **Total Implemented Skills**: `42` across 11 specialized domains (`0` placeholders, `100%` passing structural & test verification)
  - **`VERIFIED` (Native Compiler/Runtime Executed on x86_64 Linux)**: `34` skills (`gcc -std=c11 -fanalyzer -fsanitize=address,undefined`, `g++ -std=c++20`, GNU `as` `x86_64` Assembly, Node.js V8/WebAssembly binary execution, SQLite3 ACID/EXPLAIN, Bash `set -euo pipefail`, Perl 5, Python 3.11)
  - **`PARTIALLY VERIFIED` (Host AST/Semantic/Memory-Model Verified; Target Compiler Designed for CI)**: `8` skills
- **Language & Representation Coverage**: `50` languages explicitly classified across Systems, General-Purpose, Scientific, Query, Shell, GPU Compute, Shaders, HDLs, and Low-Level IRs (`docs/skill-catalog/SKILL_CATALOG_AND_COVERAGE_MATRIX.md`)

## Quickstart: Run Full Verification & Benchmarks

```bash
# 1. Validate all 42 skills and run all 42 executable verification harnesses
python3 tests/run_all_verifications.py

# 2. Run Intelligent Skill Router & Dependency Resolver integration tests
python3 tests/integration/test_router_and_workflows.py

# 3. Run Mode A / Mode B / Mode C evaluation pipeline
python3 evaluation/pipeline.py

# 4. Run full regression suite
python3 tests/regression/test_intelligence_systems.py
```


## License

Licensed under the **Apache License 2.0** (`LICENSE`).
