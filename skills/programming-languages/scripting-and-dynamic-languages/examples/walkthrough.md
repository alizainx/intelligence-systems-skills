# Verified Example: `scripting-and-dynamic-languages` (`defensive_shell_and_perl.sh`)

```
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Safe array handling & Perl strict/warnings invocation on filenames with spaces
tmp_dir="$(mktemp -d)"
trap 'rm -rf -- "$tmp_dir"' EXIT

touch "$tmp_dir/file with spaces 1.txt" "$tmp_dir/file with spaces 2.txt"
count=0
for f in "$tmp_dir"/*.txt; do
    [[ -e "$f" ]] || continue
    count=$((count + 1))
done
[[ "$count" -eq 2 ]] || exit 1

perl -Mstrict -Mwarnings -e '
    my @nums = (10, 20, 30, 40);
    my $sum = 0;
    for my $n (@nums) { $sum += $n; }
    die "Sum mismatch" unless $sum == 100;
'
echo "NATIVE BASH 5.2 (set -euo pipefail) & PERL 5 (strict/warnings) VERIFIED"

```
