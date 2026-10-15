# Nontrivial Implementation & Multi-File Engineering Walkthrough: `swift-arc-concurrency`

- **Target File**: `examples/ActorLedger.swift`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
public struct LedgerEntry: Sendable, Equatable {
    public let accountId: UInt64
    public let deltaCents: Int64
}

public actor AccountLedger {
    private var balances: [UInt64: Int64] = [:]

    public func apply(_ entry: LedgerEntry) -> Int64? {
        let current = balances[entry.accountId, default: 0]
        let (next, overflow) = current.addingReportingOverflow(entry.deltaCents)
        guard !overflow && next >= 0 else { return nil }
        balances[entry.accountId] = next
        return next
    }
}

```
