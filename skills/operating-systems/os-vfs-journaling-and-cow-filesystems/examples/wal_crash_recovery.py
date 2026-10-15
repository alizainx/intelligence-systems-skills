from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WalRecord:
    tx_id: int
    block_no: int
    new_data: int
    committed: bool

def recover_journal_after_crash(disk_blocks: dict[int, int], wal_log: list[WalRecord]) -> dict[int, int]:
    """Replays ONLY committed write-ahead log (WAL) transactions idempotently; discards uncommitted torn writes."""
    committed_txs = {r.tx_id for r in wal_log if r.committed}
    recovered = dict(disk_blocks)
    for r in wal_log:
        if r.tx_id in committed_txs:
            recovered[r.block_no] = r.new_data
    return recovered
