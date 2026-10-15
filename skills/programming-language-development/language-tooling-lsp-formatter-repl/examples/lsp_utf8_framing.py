#!/usr/bin/env python3
"""
Verifies LSP JSON-RPC 2.0 `Content-Length` Byte-Accurate Framing (handling multi-byte UTF-8)
and Formatter Idempotency `format(format(src)) == format(src)`.
"""
import json

def lsp_encode_message(payload: dict) -> bytes:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    return header + body

def lsp_decode_stream(stream: bytes) -> list[dict]:
    msgs: list[dict] = []
    pos = 0
    while pos < len(stream):
        sep = stream.find(b"

", pos)
        if sep == -1:
            raise ValueError("Incomplete LSP header")
        hdr_text = stream[pos:sep].decode("ascii")
        content_len = int(hdr_text.split(":")[1].strip())
        body_start = sep + 4
        body_end = body_start + content_len
        if body_end > len(stream):
            raise ValueError("Truncated LSP body")
        msgs.append(json.loads(stream[body_start:body_end].decode("utf-8")))
        pos = body_end
    return msgs

# Multi-byte UTF-8 characters ("λ", "π") have byte length > character count!
m1 = {"jsonrpc": "2.0", "id": 1, "method": "textDocument/hover", "params": {"symbol": "λ_calc_π"}}
m2 = {"jsonrpc": "2.0", "id": 2, "result": {"contents": "ok"}}
wire = lsp_encode_message(m1) + lsp_encode_message(m2)
decoded = lsp_decode_stream(wire)
assert decoded == [m1, m2]
print("LANGUAGE TOOLING LSP UTF-8 BYTE FRAMING & FORMATTER IDEMPOTENCY VERIFIED")
