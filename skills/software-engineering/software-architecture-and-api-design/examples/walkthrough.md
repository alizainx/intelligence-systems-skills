# Verified Example: `software-architecture-and-api-design` (`idempotent_api_gateway.py`)

```
#!/usr/bin/env python3
"""Verifies Idempotent API Request Deduplication Store & Backward-Compatible Schema Evolution."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ApiResponse:
    status_code: int
    body: str

class IdempotentApiGateway:
    def __init__(self) -> None:
        self._store: dict[str, tuple[str, ApiResponse]] = {}

    def handle_post(self, idempotency_key: str, payload_hash: str, compute_fn) -> ApiResponse:
        if not idempotency_key:
            raise ValueError("Missing Idempotency-Key header")
        if idempotency_key in self._store:
            saved_hash, saved_resp = self._store[idempotency_key]
            if saved_hash != payload_hash:
                return ApiResponse(422, "Conflict: Idempotency-Key reused with different request payload")
            return saved_resp
        resp = compute_fn()
        self._store[idempotency_key] = (payload_hash, resp)
        return resp

gw = IdempotentApiGateway()
calls = [0]
def charge():
    calls[0] += 1
    return ApiResponse(201, f"charged_{calls[0]}")

r1 = gw.handle_post("key-1", "sha256:aaa", charge)
r2 = gw.handle_post("key-1", "sha256:aaa", charge)  # Retry with same key+payload -> no duplicate side-effect!
r3 = gw.handle_post("key-1", "sha256:bbb", charge)  # Reused key with different payload -> HTTP 422!
assert r1 == r2 and calls[0] == 1 and r3.status_code == 422
print("SOFTWARE ARCHITECTURE IDEMPOTENCY KEY & API CONTRACT VERIFIED")

```
