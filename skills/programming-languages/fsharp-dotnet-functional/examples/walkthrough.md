# Nontrivial Implementation & Multi-File Engineering Walkthrough: `fsharp-dotnet-functional`

- **Target File**: `examples/UnitsOfMeasureKinematics.fs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
module Iss.FSharp.Kinematics

[<Measure>] type m
[<Measure>] type s
[<Measure>] type kg
[<Measure>] type N = kg * m / s^2

[<Struct>]
type ThrustCommand = { Force: float<N>; Duration: float<s> }

let computeImpulse (cmd: ThrustCommand) : Result<float<kg * m / s>, string> =
    if cmd.Duration <= 0.0<s> then Error "Duration must be positive"
    else Ok (cmd.Force * cmd.Duration)

```
