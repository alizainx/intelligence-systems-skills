# Nontrivial Implementation & Multi-File Engineering Walkthrough: `webassembly-linear-memory-wasi`

- **Target File**: `examples/wasm_euclid_gcd.mjs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
import assert from 'node:assert/strict';

// Hand-assembled valid WebAssembly binary module exporting gcd(a: i32, b: i32) -> i32
// (module (func (export "gcd") (param $a i32) (param $b i32) (result i32) ...))
const wasmBytes = new Uint8Array([
  0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00, // magic + version 1
  0x01, 0x07, 0x01, 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f, // type 0: (i32, i32) -> i32
  0x03, 0x02, 0x01, 0x00, // func 0 uses type 0
  0x07, 0x07, 0x01, 0x03, 0x67, 0x63, 0x64, 0x00, 0x00, // export "gcd" -> func 0
  0x0a, 0x24, 0x01, 0x22, 0x01, 0x01, 0x7f, // code section: 1 local $t of type i32
  0x02, 0x40, // block
    0x03, 0x40, // loop
      0x20, 0x01, 0x45, 0x0d, 0x01, // local.get $b; i32.eqz; br_if 1 (exit block)
      0x20, 0x01, 0x21, 0x02, // local.get $b; local.set $t
      0x20, 0x00, 0x20, 0x01, 0x6f, 0x21, 0x01, // local.get $a; local.get $b; i32.rem_u; local.set $b
      0x20, 0x02, 0x21, 0x00, // local.get $t; local.set $a
      0x0c, 0x00, // br 0 (continue loop)
    0x0b, // end loop
  0x0b, // end block
  0x20, 0x00, 0x0b // local.get $a; end func
]);

assert.equal(WebAssembly.validate(wasmBytes), true);
const { instance } = await WebAssembly.instantiate(wasmBytes);
assert.equal(instance.exports.gcd(1071, 462), 21);
assert.equal(instance.exports.gcd(48, 18), 6);
assert.equal(instance.exports.gcd(17, 0), 17);
console.log('VERIFIED: Native W3C WebAssembly binary validation & V8 Euclid GCD loop execution passed');

```
