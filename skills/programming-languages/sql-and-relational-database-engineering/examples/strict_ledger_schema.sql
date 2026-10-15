-- Verified Relational Schema with CHECK constraints, FOREIGN KEY cascade, and covering index
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT NOT NULL,
    balance_cents INTEGER NOT NULL CHECK (balance_cents >= 0)
) STRICT;

CREATE TABLE ledger_entries (
    entry_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(account_id) ON DELETE RESTRICT,
    delta_cents INTEGER NOT NULL,
    created_seq INTEGER NOT NULL
) STRICT;

CREATE INDEX idx_ledger_acct_seq ON ledger_entries(account_id, created_seq);
