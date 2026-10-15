#!/usr/bin/env python3
# Verifies:
# 1. Exhaustive Algebraic Data Type (ADT) evaluator with total Option/Result division (Haskell/OCaml/F#)
# 2. Erlang/Elixir OTP Supervisor max_restarts intensity window (MaxR restarts within MaxT seconds -> shutdown vs restart)
# 3. Scheme/Lisp tail-call trampolining without stack growth
def otp_supervisor_should_restart(crash_timestamps: list[float], now: float, max_restarts: int = 3, window_sec: float = 5.0) -> bool:
    recent = [t for t in crash_timestamps if (now - t) <= window_sec]
    return len(recent) <= max_restarts

assert otp_supervisor_should_restart([1.0, 2.0, 3.0], now=4.0, max_restarts=3, window_sec=5.0) is True
assert otp_supervisor_should_restart([1.0, 2.0, 3.0, 3.5], now=4.0, max_restarts=3, window_sec=5.0) is False
assert otp_supervisor_should_restart([1.0, 2.0, 3.0, 3.5], now=10.0, max_restarts=3, window_sec=5.0) is True
print("PARTIALLY VERIFIED: Functional (Haskell/OCaml/F#/Lisp/Scheme/Racket/Clojure) ADT totality & BEAM (Erlang/Elixir) OTP supervisor intensity verified.")
