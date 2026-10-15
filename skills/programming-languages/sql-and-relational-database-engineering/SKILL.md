---
name: sql-and-relational-database-engineering
description: Design, optimize, audit, and verify relational SQL schemas, migrations, and queries using strict constraints, B-tree composite index selectivity, CTEs/window functions, ACID isolation levels, parameterized queries, and native SQLite3 execution.
allowed-tools: execute_bash view_file write_to_file
---

# SQL (ISO SQL:2023 / PostgreSQL / SQLite3) ACID Transactions, Indexing, Window Functions & SQLi Defense

Design, optimize, audit, and verify relational SQL schemas, migrations, and queries using strict constraints, B-tree composite index selectivity, CTEs/window functions, ACID isolation levels, parameterized queries, and native SQLite3 execution.

## A. Identity

- **Skill Name**: `sql-and-relational-database-engineering`
- **Domain**: `programming-languages`
- **Language / Representation**: **SQL** (`Declarative Relational Query & Schema Language`)
- **Technical Relationship**: ISO/IEC 9075 declarative query and DDL/DML transactional language executed by relational engines (SQLite3, PostgreSQL, MySQL) with ACID guarantees.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **SQL**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: ISO/IEC 9075:2023 (SQL:2023), PostgreSQL 16/17 & SQLite 3.40+ Specifications (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+))
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Idempotent forward/rollback DDL migration scripts verified in transactions.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **SQL** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **SQL**.

### Technical Triggers

- Files, build manifests, or prompts targeting **SQL** (`strict_ledger_schema.sql`, `Idempotent forward/rollback DDL migration scripts verified in transactions.`).

### Prerequisites

- Target language version (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+)), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **SQL** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+)), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Work-memory sorting/hash-join budgets (`work_mem`), keyset cursor pagination (`WHERE (created_at, id) < (?, ?)`) instead of $O(N)$ `OFFSET` scans.), type soundness limits (Strict column types (`STRICT` tables in SQLite 3.37+, `BIGINT`, `NUMERIC(18,4)` for exact currency-never `FLOAT`/`REAL` for money), `CHECK` constraints, and `FOREIGN KEY` cascading rules.), and concurrency hazards (MVCC snapshot isolation, explicit `BEGIN IMMEDIATE` (SQLite) or `SELECT ... FOR UPDATE SKIP LOCKED` (PostgreSQL), and deterministic primary-key ordering on multi-row updates to prevent deadlocks.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce ISO/IEC 9075:2023 (SQL:2023), PostgreSQL 16/17 & SQLite 3.40+ Specifications.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Declarative set-based semantics, three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`/`NULL` - always use `IS NULL` / `IS NOT DISTINCT FROM`), CTEs (`WITH`), and Window Functions (`OVER (PARTITION BY ... ORDER BY ...)`).
2. **Type System & Inference**: Strict column types (`STRICT` tables in SQLite 3.37+, `BIGINT`, `NUMERIC(18,4)` for exact currency-never `FLOAT`/`REAL` for money), `CHECK` constraints, and `FOREIGN KEY` cascading rules.
3. **Memory Management**: Work-memory sorting/hash-join budgets (`work_mem`), keyset cursor pagination (`WHERE (created_at, id) < (?, ?)`) instead of $O(N)$ `OFFSET` scans.
4. **Concurrency & Async Programming**: MVCC snapshot isolation, explicit `BEGIN IMMEDIATE` (SQLite) or `SELECT ... FOR UPDATE SKIP LOCKED` (PostgreSQL), and deterministic primary-key ordering on multi-row updates to prevent deadlocks.
5. **Standard Library & Ecosystem**: SQLite3 (`sqlite3` stdlib), PostgreSQL (`psql`, `pg_stat_statements`), `sqlfluff`, Flyway/Sqitch migrations.
6. **Build Systems & Package Management**: Idempotent forward/rollback DDL migration scripts verified in transactions.
7. **Compiler / Interpreter Behavior**: Cost-based query planner: inspect index vs full-table scans via `EXPLAIN QUERY PLAN` / `EXPLAIN (ANALYZE, BUFFERS)`; preserve sargability (never wrap indexed columns in functions like `WHERE LOWER(col) = ?` without an expression index).
8. **Debugging & Observability**: `EXPLAIN QUERY PLAN`, slow-query logs, lock-wait graphs (`pg_locks`).
9. **Security Hardening**: 100% bound parameters (`?` / `$1`); zero string interpolation in SQL text; least-privilege DB roles and Row-Level Security (RLS).
10. **Performance Optimization**: Composite index left-prefix rule (`(tenant_id, status, created_at)`), covering indexes (`INCLUDE`), and batch `INSERT` within a single transaction.
11. **Error Handling Discipline**: Handle `SQLITE_BUSY` / serialization failures (`SQLSTATE 40001`) with bounded exponential backoff retries and atomic `ROLLBACK`.
12. **Testing Methodologies**: Execute schema creation, constraint rejection, injection resistance, and `EXPLAIN QUERY PLAN` assertions against a real SQLite3 engine.
13. **Interoperability & Cross-Platform ABI**: DB-API 2.0 (`sqlite3`/`psycopg`), JDBC, ODBC, and JSONB boundary validation.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/sql-and-relational-database-engineering/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+)), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in SQL**: `NOT IN (SELECT nullable_col ...)` returning 0 rows when any `NULL` is present (use `NOT EXISTS`), `FLOAT` currency rounding drift, and non-sargable predicates.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
