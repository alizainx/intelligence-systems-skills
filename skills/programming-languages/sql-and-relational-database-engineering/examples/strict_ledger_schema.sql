PRAGMA foreign_keys = ON;

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT NOT NULL,
    balance_cents INTEGER NOT NULL CHECK (balance_cents >= 0)
) STRICT;

CREATE TABLE transfers (
    transfer_id INTEGER PRIMARY KEY,
    from_account INTEGER NOT NULL REFERENCES accounts(account_id),
    to_account INTEGER NOT NULL REFERENCES accounts(account_id),
    amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
    created_epoch INTEGER NOT NULL,
    CHECK (from_account != to_account)
) STRICT;

CREATE INDEX idx_transfers_from_created ON transfers(from_account, created_epoch DESC);
