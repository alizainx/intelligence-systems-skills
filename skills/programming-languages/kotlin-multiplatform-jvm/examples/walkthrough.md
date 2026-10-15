# Nontrivial Implementation & Multi-File Engineering Walkthrough: `kotlin-multiplatform-jvm`

- **Target File**: `examples/StructuredFlowWorker.kt`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
package com.iss.kotlin
import kotlin.coroutines.cancellation.CancellationException

@JvmInline
value class RequestId(val raw: Long) {
    init { require(raw > 0L) { "RequestId must be positive" } }
}

suspend inline fun <T, R> safeSuspendRun(block: () -> R): Result<R> =
    try {
        Result.success(block())
    } catch (c: CancellationException) {
        throw c // Mandatory: never swallow CancellationException in coroutines
    } catch (t: Throwable) {
        Result.failure(t)
    }

```
