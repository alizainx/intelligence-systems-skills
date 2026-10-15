package worker

import (
    "context"
    "errors"
)

var ErrInvalidLimit = errors.New("worker limit must be positive")

func ProcessBounded[T any, R any](ctx context.Context, items []T, limit int, fn func(context.Context, T) (R, error)) ([]R, error) {
    if limit <= 0 {
        return nil, ErrInvalidLimit
    }
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()
    out := make([]R, len(items))
    for i, item := range items {
        select {
        case <-ctx.Done():
            return nil, ctx.Err()
        default:
        }
        res, err := fn(ctx, item)
        if err != nil {
            cancel()
            return nil, err
        }
        out[i] = res
    }
    return out, nil
}
