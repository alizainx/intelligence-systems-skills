# Nontrivial Implementation & Multi-File Engineering Walkthrough: `lua-c-api-embedding`

- **Target File**: `examples/sandboxed_eval.lua`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
local M = {}

function M.run_sandboxed(untrusted_src, env_vars)
    assert(type(untrusted_src) == "string", "source must be string")
    local safe_env = {
        math = { abs = math.abs, max = math.max, min = math.min },
        tonumber = tonumber,
    }
    for k, v in pairs(env_vars or {}) do
        safe_env[k] = v
    end
    -- Mode 't' strictly forbids binary bytecode chunks
    local chunk, err = load(untrusted_src, "sandbox", "t", safe_env)
    if not chunk then
        return false, err
    end
    return pcall(chunk)
end

return M

```
