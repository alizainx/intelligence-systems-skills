# Nontrivial Implementation & Multi-File Engineering Walkthrough: `dart-isolates-async`

- **Target File**: `examples/sealed_rpc_result.dart`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
sealed class RpcOutcome<T> {
  const RpcOutcome();
}
final class RpcSuccess<T> extends RpcOutcome<T> {
  final T payload;
  const RpcSuccess(this.payload);
}
final class RpcFailure<T> extends RpcOutcome<T> {
  final int code;
  final String message;
  const RpcFailure(this.code, this.message);
}

String formatOutcome(RpcOutcome<int> res) => switch (res) {
  RpcSuccess(payload: final v) => 'OK:$v',
  RpcFailure(code: final c, message: final m) => 'ERR:$c:$m',
};

```
