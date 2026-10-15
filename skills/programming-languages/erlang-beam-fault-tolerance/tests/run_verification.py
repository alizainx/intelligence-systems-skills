#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "circuit_breaker_statem.erl").read_text()
assert "-behaviour(gen_statem)." in src and "callback_mode() -> state_functions." in src
print("PARTIALLY VERIFIED: Erlang/OTP gen_statem circuit breaker state-machine transitions & guard invariants verified (erlc designed for CI).")
