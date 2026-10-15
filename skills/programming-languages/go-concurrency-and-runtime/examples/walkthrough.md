# Verified Example: `go-concurrency-and-runtime` (`worker_pool.go`)

```
package concurrency

import "context"

func WorkerPool(ctx context.Context, jobs <-chan int, results chan<- int) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        case j, ok := <-jobs:
            if !ok {
                return nil
            }
            select {
            case <-ctx.Done():
                return ctx.Err()
            case results <- j * 2:
            }
        }
    }
}

```
