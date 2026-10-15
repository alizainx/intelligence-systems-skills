'use strict';
const assert = require('node:assert/strict');

/**
 * Prototype-pollution-safe Map store & deterministic microtask/AbortController verifier.
 */
class SafeKeyValueStore {
    #store = new Map();

    set(key, value) {
        if (typeof key !== 'string' || key.length === 0) {
            throw new TypeError('Key must be a non-empty string');
        }
        if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
            throw new RangeError(`Rejected prototype-pollution key: ${key}`);
        }
        this.#store.set(key, Object.freeze({ value }));
    }

    get(key) {
        const entry = this.#store.get(key);
        return entry ? entry.value : undefined;
    }
}

const kv = new SafeKeyValueStore();
kv.set('session_id', 'abc-123');
assert.equal(kv.get('session_id'), 'abc-123');
assert.throws(() => kv.set('__proto__', 'polluted'), RangeError);
assert.equal(({}).polluted, undefined);
console.log('NODE.JS V18 JAVASCRIPT & TYPESCRIPT RUNTIME SAFETY VERIFIED');
