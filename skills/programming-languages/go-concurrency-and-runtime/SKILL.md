---
name: go-concurrency-and-runtime
description: Architect, implement, profile, and verify production Go 1.22+ services using context.Context cancellation propagation, errgroup structured concurrency, channel ownership rules, errors.Is/As wrapping, -race verification, and pprof/escape-analysis optimization.
allowed-tools: execute_bash view_file write_to_file
---

# Go (1.22/1.23+) Goroutines, Channels, Context Cancellation, Race Detector & Pprof

Architect, implement, profile, and verify production Go 1.22+ services using context.Context cancellation propagation, errgroup structured concurrency, channel ownership rules, errors.Is/As wrapping, -race verification, and pprof/escape-analysis optimization.

## A. Identity

- **Skill Name**: `go-concurrency-and-runtime`
- **Domain**: `programming-languages`
- **Language / Representation**: **Go** (`General-Purpose & Cloud Systems Language`)
- **Technical Relationship**: Compiled concurrent systems language with an M:N work-stealing goroutine scheduler, concurrent tri-color mark-sweep GC, and static binary linking.
- **Version**: `2.0.0`
- **Purpose**: Provide deep, language-specific engineering intelligence across all 20 language dimensions and 14 advanced coding capabilities for **Go**.
- **Supported Tasks**: Production code generation, existing code analysis, multi-file implementation, complex debugging, refactoring, dependency troubleshooting, compilation error resolution, performance optimization, security auditing, algorithm implementation, unit/integration testing, build-system troubleshooting, and large-project maintenance.
- **Required Knowledge**: The Go Programming Language Specification, Go Memory Model (Go 1.22 / Go 1.23+)
- **Dependencies**: Host verification harness (`tests/run_verification.py`) and target toolchain (`Go Modules (`go.mod`, `go.sum`, `go mod verify`), `CGO_ENABLED=0` static builds, `govulncheck`.`).
- **Compatibility Requirements**: Model-agnostic Markdown + progressive disclosure (`references/language-engineering-matrix.md`).

## B. Activation Criteria

### When to Use

- Activate when writing, analyzing, refactoring, debugging, optimizing, or verifying **Go** source code or build pipelines.
- Activate when diagnosing compiler/interpreter diagnostics, memory/lifetime bugs, concurrency races, or FFI/ABI defects in **Go**.

### Technical Triggers

- Files, build manifests, or prompts targeting **Go** (`bounded_worker_pool.go`, `Go Modules (`go.mod`, `go.sum`, `go mod verify`), `CGO_ENABLED=0` static builds, `govulncheck`.`).

### Prerequisites

- Target language version (Go 1.22 / Go 1.23+), platform ABI, and execution environment constraints.

### When NOT to Use

- Do not activate for unrelated languages; route sibling languages or parent/target toolchains via `schemas/skill-registry.json`.

## C. Problem Understanding

Execute this 8-step intake protocol before generating or modifying **Go** code:

1. **Identify the Engineering Problem**: Define functional invariants, throughput/latency targets, and failure semantics.
2. **Extract Explicit Requirements**: Lock language version (Go 1.22 / Go 1.23+), public API signatures, and module boundaries.
3. **Identify Hidden Technical Constraints**: Surface memory model rules (Compiler escape analysis (`go build -gcflags="-m"`), `sync.Pool` for reusable buffers, and pre-sized slices (`make([]T, 0, cap)`).), type soundness limits (Type parameters (`[T comparable]`), small consumer-defined interfaces, and watch out for typed-`nil` interface traps (`var p *MyErr = nil; var err error = p` is `err != nil`).), and concurrency hazards (Every goroutine must have a deterministic exit path via `ctx.Done()`; only the sender closes a channel; bound concurrency via `errgroup.SetLimit(n)`.).
4. **Determine Environmental Limitations**: Probe native compiler/runtime availability in the execution environment before claiming runtime verification.
5. **Identify Applicable Standards**: Enforce The Go Programming Language Specification, Go Memory Model.
6. **Separate Known Facts from Assumptions**: Partition verified toolchain/platform facts from explicit engineering assumptions.
7. **Identify Missing Critical Information**: Apply safe, deterministic defaults when non-blocking.
8. **Establish Measurable Acceptance Criteria**: Zero compiler/linter warnings, zero memory/race violations, and 100% pass across nominal, boundary, and negative tests.

## D. Technical Reasoning Protocol

Follow `UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW` across the 20 language-specific engineering dimensions (full matrix in `references/language-engineering-matrix.md`):

1. **Syntax & Semantics**: Explicit error returns, `defer` LIFO cleanup, Go 1.22 per-iteration loop variable scoping, and interface satisfaction by method set.
2. **Type System & Inference**: Type parameters (`[T comparable]`), small consumer-defined interfaces, and watch out for typed-`nil` interface traps (`var p *MyErr = nil; var err error = p` is `err != nil`).
3. **Memory Management**: Compiler escape analysis (`go build -gcflags="-m"`), `sync.Pool` for reusable buffers, and pre-sized slices (`make([]T, 0, cap)`).
4. **Concurrency & Async Programming**: Every goroutine must have a deterministic exit path via `ctx.Done()`; only the sender closes a channel; bound concurrency via `errgroup.SetLimit(n)`.
5. **Standard Library & Ecosystem**: Standard library (`net/http`, `log/slog`, `sync/atomic`, `context`), `golang.org/x/sync/errgroup`, `golangci-lint`.
6. **Build Systems & Package Management**: Go Modules (`go.mod`, `go.sum`, `go mod verify`), `CGO_ENABLED=0` static builds, `govulncheck`.
7. **Compiler / Interpreter Behavior**: Stack growth via contiguous stack copying (`2KB` initial goroutine stack) and non-preemptive safepoints in tight CGo calls.
8. **Debugging & Observability**: `go test -race`, Delve (`dlv`), `net/http/pprof` (CPU, heap, goroutine, mutex profiles), and `go tool trace`.
9. **Security Hardening**: `crypto/subtle.ConstantTimeCompare`, `html/template` auto-escaping, and explicit `ReadHeaderTimeout`/`IdleTimeout` on `http.Server`.
10. **Performance Optimization**: Keep hot structs on the stack (avoid escaping interface conversions), use `strings.Builder`/`bytes.Buffer`, and align 64-bit atomic fields.
11. **Error Handling Discipline**: Wrap errors with `fmt.Errorf("op: %w", err)` and inspect via `errors.Is` / `errors.As`.
12. **Testing Methodologies**: Table-driven subtests (`t.Run`), `t.Parallel()`, `testing.F` native fuzzing (`go test -fuzz=.`), and `-race`.
13. **Interoperability & Cross-Platform ABI**: Prefer pure Go over `cgo` where possible (due to CGo stack-switch & thread pinning overhead); isolate CGo behind build tags.
14. **Architecture, Multi-File Maintenance & Refactoring**: Enforce acyclic module dependencies, characterization tests before refactoring, and strict interface boundaries.

## E. Verification Protocol

### Verification Methods and Test Requirements

Execute the language verification suite:

```bash
python3 skills/programming-languages/go-concurrency-and-runtime/tests/run_verification.py
```

### Failure Conditions, Boundary Cases, and Tolerances

- **Failure Conditions**: Any syntax/type error, compiler warning under strict flags, sanitizer fault, or failed invariant assertion.
- **Boundary Cases**: Empty/zero inputs, numeric/index bounds, resource exhaustion, and concurrent contention.
- **Numerical & Semantic Tolerances**: Exact state/integer equivalence (`0` drift) and bounded IEEE 754 tolerances where applicable.
- **Safety and Performance Criteria**: Deterministic cleanup and bounded algorithmic complexity.
- **Reproducibility Requirements**: Record exact toolchain status (`VERIFIED` when native compiler/runtime executes; `PARTIALLY VERIFIED` when verified via host AST/semantic verifier).

## Multi-Stage Quality Assurance Workflow

1. **Stage 1 (Requirement Verification)**: Confirm version (Go 1.22 / Go 1.23+), interfaces, and module layout.
2. **Stage 2 (Technical Verification)**: Audit type soundness, memory lifetime/ownership, and concurrency ordering.
3. **Stage 3 (Implementation Verification)**: Compile or execute nominal workloads via `run_verification.py`.
4. **Stage 4 (Edge-Case Verification)**: Test boundary, overflow, malformed, and error-unwinding paths.
5. **Stage 5 (Independent Review)**: Run static analysis, AST/model auditing, or dynamic sanitizers.
6. **Stage 6 (Final Validation)**: Record honest verification status (`VERIFIED` vs. `PARTIALLY VERIFIED`) in `validation.md`.

## Gotchas and Error Detection

Report all defects using the 6-field schema (Description, Severity, Root Cause, Potential Consequences, Proposed Correction, Verification Procedure):

- **Primary Pitfalls in Go**: Unbuffered channel sends without `select { case <-ctx.Done(): }` leaking goroutines, copying `sync.Mutex` by value (`go vet` `-copylocks`), and mutating shared maps concurrently.
- **Unverified Toolchain Claims**: Never mark a compilation or runtime check `VERIFIED` unless the binary or interpreter actually executed in the test environment.
