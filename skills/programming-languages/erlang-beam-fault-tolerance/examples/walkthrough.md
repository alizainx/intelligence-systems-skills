# Nontrivial Implementation & Multi-File Engineering Walkthrough: `erlang-beam-fault-tolerance`

- **Target File**: `examples/circuit_breaker_statem.erl`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
-module(circuit_breaker_statem).
-behaviour(gen_statem).
-export([callback_mode/0, init/1, closed/3, open/3]).

-record(data, {failures = 0 :: non_neg_integer(), threshold = 3 :: pos_integer()}).

callback_mode() -> state_functions.

init(Threshold) when is_integer(Threshold), Threshold > 0 ->
    {ok, closed, #data{failures = 0, threshold = Threshold}}.

closed({call, From}, record_failure, D = #data{failures = F, threshold = T}) ->
    NextF = F + 1,
    case NextF >= T of
        true  -> {next_state, open, D#data{failures = NextF}, [{reply, From, tripped}]};
        false -> {keep_state, D#data{failures = NextF}, [{reply, From, ok}]}
    end.

open({call, From}, reset, D) ->
    {next_state, closed, D#data{failures = 0}, [{reply, From, reset_ok}]}.

```
