type
  Microseconds* = distinct int64

func `+`*(a, b: Microseconds): Microseconds {.borrow.}
func `<=`*(a, b: Microseconds): bool {.borrow.}

func clampTimeout*(val, maxLimit: Microseconds): Microseconds {.noSideEffect, raises: [].} =
  if int64(val) < 0: return Microseconds(0)
  if val <= maxLimit: return val
  return maxLimit
