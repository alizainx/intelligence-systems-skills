# Nontrivial Implementation & Multi-File Engineering Walkthrough: `typescript-type-system-engineering`

- **Target File**: `examples/branded_type_guard.mjs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
// Runtime-executable TypeScript/ES2023 branded type guard & exhaustive discriminated union verifier
import assert from 'node:assert/strict';

export function parsePositiveCents(input) {
  if (typeof input !== 'number' || !Number.isSafeInteger(input) || input <= 0) {
    return { ok: false, error: 'INVALID_CENTS' };
  }
  return { ok: true, value: input };
}

export function handlePaymentResult(res) {
  switch (res.ok) {
    case true:
      return `PAID:${res.value}`;
    case false:
      return `REJECTED:${res.error}`;
    default:
      throw new Error(`Unhandled discriminant: ${JSON.stringify(res)}`);
  }
}

assert.equal(handlePaymentResult(parsePositiveCents(500)), 'PAID:500');
assert.equal(handlePaymentResult(parsePositiveCents(-10)), 'REJECTED:INVALID_CENTS');
assert.equal(handlePaymentResult(parsePositiveCents(Number.NaN)), 'REJECTED:INVALID_CENTS');
console.log('VERIFIED: TypeScript runtime boundary guard, SafeInteger check & exhaustive union verified');

```
