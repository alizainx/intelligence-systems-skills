# Go Concurrency & Memory Model Reference

Unbuffered channel send blocks forever if the receiver exits early unless guarded by `select { case ch <- v: case <-ctx.Done(): }`.
