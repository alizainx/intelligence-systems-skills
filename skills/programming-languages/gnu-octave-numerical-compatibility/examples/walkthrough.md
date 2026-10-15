# Nontrivial Implementation & Multi-File Engineering Walkthrough: `gnu-octave-numerical-compatibility`

- **Target File**: `examples/portable_rk4_step.m`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
function y_next = portable_rk4_step(f, t, y, dt)
    if (dt <= 0)
        error('ISS:InvalidStep', 'Time step dt must be positive');
    end
    k1 = f(t, y);
    k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1);
    k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2);
    k4 = f(t + dt, y + dt * k3);
    y_next = y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
end

%!test
%! f = @(t, y) -2.0 * y;
%! y1 = portable_rk4_step(f, 0.0, 1.0, 0.01);
%! assert(y1, exp(-0.02), 1e-9);

```
