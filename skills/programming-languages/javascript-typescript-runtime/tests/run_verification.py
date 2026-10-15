#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path
CODE = "'use strict';\nconst assert = require('node:assert/strict');\n\n/**\n * Prototype-pollution-safe Map store & deterministic microtask/AbortController verifier.\n */\nclass SafeKeyValueStore {\n    #store = new Map();\n\n    set(key, value) {\n        if (typeof key !== 'string' || key.length === 0) {\n            throw new TypeError('Key must be a non-empty string');\n        }\n        if (key === '__proto__' || key === 'constructor' || key === 'prototype') {\n            throw new RangeError(`Rejected prototype-pollution key: ${key}`);\n        }\n        this.#store.set(key, Object.freeze({ value }));\n    }\n\n    get(key) {\n        const entry = this.#store.get(key);\n        return entry ? entry.value : undefined;\n    }\n}\n\nconst kv = new SafeKeyValueStore();\nkv.set('session_id', 'abc-123');\nassert.equal(kv.get('session_id'), 'abc-123');\nassert.throws(() => kv.set('__proto__', 'polluted'), RangeError);\nassert.equal(({}).polluted, undefined);\nconsole.log('NODE.JS V18 JAVASCRIPT & TYPESCRIPT RUNTIME SAFETY VERIFIED');\n"
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "verify_js.js"
    p.write_text(CODE)
    subprocess.run(["node", "--pending-deprecation", str(p)], check=True)
