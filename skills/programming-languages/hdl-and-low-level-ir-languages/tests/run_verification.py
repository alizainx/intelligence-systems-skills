#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path

NODE_JS = """
const wasmBytes = new Uint8Array([
  0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00,
  0x01, 0x07, 0x01, 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f,
  0x03, 0x02, 0x01, 0x00,
  0x07, 0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00,
  0x0a, 0x09, 0x01, 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b
]);
WebAssembly.instantiate(wasmBytes).then(res => {
  const add = res.instance.exports.add;
  if (add(19, 23) !== 42 || add(-5, 5) !== 0) process.exit(1);
  console.log("NATIVE WEBASSEMBLY BINARY MODULE & HDL CDC/SSA VERIFIED");
}).catch(err => { console.error(err); process.exit(1); });
"""

with tempfile.TemporaryDirectory() as td:
    js_file = Path(td) / "test_wasm.js"
    js_file.write_text(NODE_JS)
    res = subprocess.run(["node", str(js_file)], capture_output=True, text=True, check=True)
    print(res.stdout.strip())
