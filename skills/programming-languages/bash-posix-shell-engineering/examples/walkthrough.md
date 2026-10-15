# Nontrivial Implementation & Multi-File Engineering Walkthrough: `bash-posix-shell-engineering`

- **Target File**: `examples/atomic_config_writer.sh`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
#!/usr/bin/env bash
set -Eeuo pipefail
shopt -s inherit_errexit

atomic_write_kv() {
  local -r target_file="${1:?target_file required}"
  local -r key="${2:?key required}"
  local -r val="${3:?val required}"

  if [[ ! "$key" =~ ^[A-Z0-9_]+$ ]]; then
    printf 'ERROR: invalid key name: %s\n' "$key" >&2
    return 1
  fi

  local tmp_file
  tmp_file="$(mktemp "${target_file}.tmp.XXXXXX")"
  # Clean up temp file if anything fails before atomic mv
  trap 'rm -f -- "${tmp_file:-}"' RETURN
  printf '%s=%s\n' "$key" "$val" > "$tmp_file"
  mv -f -- "$tmp_file" "$target_file"
  trap - RETURN
}

test_dir="$(mktemp -d)"
trap 'rm -rf -- "$test_dir"' EXIT
out_cfg="${test_dir}/app.env"
atomic_write_kv "$out_cfg" "PORT" "8080"
[[ "$(<"$out_cfg")" == "PORT=8080" ]] || exit 1
if atomic_write_kv "$out_cfg" "bad-key;rm" "1" 2>/dev/null; then
  exit 1
fi
printf 'VERIFIED: Native GNU Bash 5.2 set -Eeuo pipefail, atomic mktemp+mv & key-injection defense passed\n'

```
