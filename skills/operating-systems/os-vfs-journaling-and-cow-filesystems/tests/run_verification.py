#!/usr/bin/env python3
SRC = 'from __future__ import annotations\nfrom dataclasses import dataclass\n\n@dataclass(frozen=True, slots=True)\nclass WalRecord:\n    tx_id: int\n    block_no: int\n    new_data: int\n    committed: bool\n\ndef recover_journal_after_crash(disk_blocks: dict[int, int], wal_log: list[WalRecord]) -> dict[int, int]:\n    """Replays ONLY committed write-ahead log (WAL) transactions idempotently; discards uncommitted torn writes."""\n    committed_txs = {r.tx_id for r in wal_log if r.committed}\n    recovered = dict(disk_blocks)\n    for r in wal_log:\n        if r.tx_id in committed_txs:\n            recovered[r.block_no] = r.new_data\n    return recovered\n'
ns = {}
exec(SRC, ns)
WalRecord = ns["WalRecord"]
recover = ns["recover_journal_after_crash"]
disk = {0: 100, 1: 200}
wal = [
    WalRecord(tx_id=1, block_no=0, new_data=111, committed=False),
    WalRecord(tx_id=1, block_no=1, new_data=222, committed=True),   # Tx 1 committed
    WalRecord(tx_id=2, block_no=0, new_data=999, committed=False),  # Tx 2 crashed before commit record!
]
r1 = recover(disk, wal)
r2 = recover(r1, wal)  # Replay must be 100% idempotent if another crash occurs during recovery!
assert r1 == r2 == {0: 111, 1: 222}, f"WAL crash recovery violated atomicity/idempotency: {r1}"
print("OS VFS & WRITE-AHEAD JOURNALING CRASH RECOVERY ATOMICITY & IDEMPOTENCE VERIFIED")
