# Deep Engineering Reference: SQL (ISO SQL:2023 / PostgreSQL / SQLite3) ACID Transactions, Indexing, Window Functions & SQLi Defense (`sql-and-relational-database-engineering`)

- **Language / Representation**: **SQL**
- **Taxonomic Classification**: `Declarative Relational Query & Schema Language`
- **Technical Relationship**: ISO/IEC 9075 declarative query and DDL/DML transactional language executed by relational engines (SQLite3, PostgreSQL, MySQL) with ACID guarantees.
- **Governing Standards & Versions**: ISO/IEC 9075:2023 (SQL:2023), PostgreSQL 16/17 & SQLite 3.40+ Specifications (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+))

## 20-Point Language-Specific Engineering Intelligence Matrix

| # | Engineering Dimension | Actionable Engineering Rules for **SQL** |
| :--- | :--- | :--- |
| 1 | **Language Syntax & Semantics** | Declarative set-based semantics, three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`/`NULL` — always use `IS NULL` / `IS NOT DISTINCT FROM`), CTEs (`WITH`), and Window Functions (`OVER (PARTITION BY ... ORDER BY ...)`). |
| 2 | **Type System & Inference** | Strict column types (`STRICT` tables in SQLite 3.37+, `BIGINT`, `NUMERIC(18,4)` for exact currency—never `FLOAT`/`REAL` for money), `CHECK` constraints, and `FOREIGN KEY` cascading rules. |
| 3 | **Memory Management** | Work-memory sorting/hash-join budgets (`work_mem`), keyset cursor pagination (`WHERE (created_at, id) < (?, ?)`) instead of $O(N)$ `OFFSET` scans. |
| 4 | **Concurrency & Async Programming** | MVCC snapshot isolation, explicit `BEGIN IMMEDIATE` (SQLite) or `SELECT ... FOR UPDATE SKIP LOCKED` (PostgreSQL), and deterministic primary-key ordering on multi-row updates to prevent deadlocks. |
| 5 | **Standard Library & Ecosystem** | SQLite3 (`sqlite3` stdlib), PostgreSQL (`psql`, `pg_stat_statements`), `sqlfluff`, Flyway/Sqitch migrations. |
| 6 | **Build Systems & Package Management** | Idempotent forward/rollback DDL migration scripts verified in transactions. |
| 7 | **Compiler / Interpreter Behavior** | Cost-based query planner: inspect index vs full-table scans via `EXPLAIN QUERY PLAN` / `EXPLAIN (ANALYZE, BUFFERS)`; preserve sargability (never wrap indexed columns in functions like `WHERE LOWER(col) = ?` without an expression index). |
| 8 | **Debugging** | `EXPLAIN QUERY PLAN`, slow-query logs, lock-wait graphs (`pg_locks`). |
| 9 | **Security** | 100% bound parameters (`?` / `$1`); zero string interpolation in SQL text; least-privilege DB roles and Row-Level Security (RLS). |
| 10 | **Performance Optimization** | Composite index left-prefix rule (`(tenant_id, status, created_at)`), covering indexes (`INCLUDE`), and batch `INSERT` within a single transaction. |
| 11 | **Error Handling** | Handle `SQLITE_BUSY` / serialization failures (`SQLSTATE 40001`) with bounded exponential backoff retries and atomic `ROLLBACK`. |
| 12 | **Testing Methodologies** | Execute schema creation, constraint rejection, injection resistance, and `EXPLAIN QUERY PLAN` assertions against a real SQLite3 engine. |
| 13 | **Code Quality & Linting** | Enforce automated formatting, strict compiler warnings-as-errors, and zero dead/unreachable code. |
| 14 | **Architecture Patterns** | Isolate domain logic from I/O, enforce explicit dependency injection, and maintain acyclic module graphs. |
| 15 | **Cross-Platform Compatibility** | Explicitly handle endianness, pointer width (`32-bit` vs `64-bit`), path separators, and OS syscall differences. |
| 16 | **Version-Specific Limitations** | Respect version gates (SQL:2016 / SQL:2023 (SQLite 3.40+ / PostgreSQL 16+)); avoid deprecated syntax and guard newer stdlib APIs behind feature checks. |
| 17 | **Language Interoperability** | DB-API 2.0 (`sqlite3`/`psycopg`), JDBC, ODBC, and JSONB boundary validation. |
| 18 | **Common Engineering Mistakes** | `NOT IN (SELECT nullable_col ...)` returning 0 rows when any `NULL` is present (use `NOT EXISTS`), `FLOAT` currency rounding drift, and non-sargable predicates. |
| 19 | **Production Best Practices** | Pin dependency lockfiles, emit structured telemetry, bound all queues/buffers, and verify graceful shutdown. |
| 20 | **Independent Verification Procedures** | Execute `python3 skills/programming-languages/sql-and-relational-database-engineering/tests/run_verification.py` and validate against `validate_skill.py`. |

## 14 Advanced Coding Capabilities Playbook for **SQL**

1. **Production-Quality Code Generation**: Emit complete, warning-free modules with explicit error handling and resource cleanup.
2. **Existing Code Analysis**: Trace dataflow, ownership/lifetime boundaries, and hidden side effects before editing.
3. **Multi-File Implementation**: Keep public headers/interfaces minimal and enforce clean compilation units.
4. **Complex Debugging**: Reproduce faults deterministically with minimal test cases and inspect stack/memory state via ``EXPLAIN QUERY PLAN`, slow-query logs, lock-wait graphs (`pg_locks`).`.
5. **Refactoring**: Establish characterization tests first, apply semantics-preserving transformations, and re-verify.
6. **Dependency Troubleshooting**: Audit diamond version conflicts, ABI mismatches, and lockfile integrity via `Idempotent forward/rollback DDL migration scripts verified in transactions.`.
7. **Compilation Error Resolution**: Decode type unification, lifetime, linker symbol, or template/macro instantiation diagnostics at the root cause.
8. **Performance Improvement**: Profile hotspots before optimizing; prioritize cache locality and allocation elimination (Composite index left-prefix rule (`(tenant_id, status, created_at)`), covering indexes (`INCLUDE`), and batch `INSERT` within a single transaction.).
9. **Security Auditing**: Audit untrusted inputs, arithmetic overflow, injection vectors, and unsafe/FFI blocks (100% bound parameters (`?` / `$1`); zero string interpolation in SQL text; least-privilege DB roles and Row-Level Security (RLS).).
10. **Algorithm Implementation**: Preserve loop invariants, termination proofs, and explicit time/space complexity bounds.
11. **Unit Testing**: Test nominal, boundary (`0`, empty, max-limit), and error-return paths (Execute schema creation, constraint rejection, injection resistance, and `EXPLAIN QUERY PLAN` assertions against a real SQLite3 engine.).
12. **Integration Testing**: Verify cross-module contracts, serialization schemas, and FFI/ABI boundaries (DB-API 2.0 (`sqlite3`/`psycopg`), JDBC, ODBC, and JSONB boundary validation.).
13. **Build-System Troubleshooting**: Resolve include/import search paths, cross-compilation triples, and reproducible flags.
14. **Large-Project Maintenance**: Enforce incremental compilation hygiene, API deprecation cycles, and continuous regression gating.
