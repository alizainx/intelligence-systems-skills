# Nontrivial Implementation & Multi-File Engineering Walkthrough: `javascript-v8-runtime`

- **Target File**: `examples/safe_json_merge.mjs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
import assert from 'node:assert/strict';

const FORBIDDEN_KEYS = new Set(['__proto__', 'constructor', 'prototype']);

export function safeFreezeMerge(target, patch) {
  const out = Object.assign(Object.create(null), target);
  for (const [k, v] of Object.entries(patch ?? {})) {
    if (FORBIDDEN_KEYS.has(k)) {
      throw new TypeError(`Rejected prototype-pollution key: ${k}`);
    }
    out[k] = (v !== null && typeof v === 'object') ? safeFreezeMerge(Object.create(null), v) : v;
  }
  return Object.freeze(out);
}

const merged = safeFreezeMerge({ host: 'localhost' }, { port: 8080 });
assert.equal(merged.host, 'localhost');
assert.equal(merged.port, 8080);
assert.equal(Object.getPrototypeOf(merged), null);
assert.throws(() => safeFreezeMerge({}, JSON.parse('{"__proto__":{"admin":true}}')), TypeError);
console.log('VERIFIED: Native Node.js V8 ES2023 null-prototype merge & prototype-pollution defense passed');

```
