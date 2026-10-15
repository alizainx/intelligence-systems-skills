#!/usr/bin/env python3
import sqlite3
from pathlib import Path

SQL_PATH = Path(__file__).resolve().parents[1] / "examples" / "strict_ledger_schema.sql"
conn = sqlite3.connect(":memory:")
conn.executescript(SQL_PATH.read_text())

with conn:
    conn.execute("INSERT INTO accounts VALUES (1, 'Alice', 10000), (2, 'Bob', 5000)")
    conn.execute("INSERT INTO transfers VALUES (101, 1, 2, 2500, 1700000000)")
    conn.execute("UPDATE accounts SET balance_cents = balance_cents - 2500 WHERE account_id = ?", (1,))
    conn.execute("UPDATE accounts SET balance_cents = balance_cents + 2500 WHERE account_id = ?", (2,))

# Verify CHECK constraint rejects negative balance
try:
    with conn:
        conn.execute("UPDATE accounts SET balance_cents = -1 WHERE account_id = ?", (1,))
    raise AssertionError("Expected IntegrityError")
except sqlite3.IntegrityError:
    pass

# Verify composite index usage via EXPLAIN QUERY PLAN
plan = conn.execute("EXPLAIN QUERY PLAN SELECT transfer_id FROM transfers WHERE from_account = ? ORDER BY created_epoch DESC", (1,)).fetchall()
assert any("idx_transfers_from_created" in str(row) for row in plan), f"Expected index scan, got {plan}"
print("VERIFIED: Native SQLite3 STRICT tables, ACID CHECK constraints & composite index EXPLAIN QUERY PLAN passed")
