# Functional, Lisp & BEAM Engineering Matrix

In Erlang/Elixir, unbound `receive` or unmonitored `spawn` leaks processes; always use OTP `Supervisor` trees with bounded `max_restarts`/`max_seconds`.
