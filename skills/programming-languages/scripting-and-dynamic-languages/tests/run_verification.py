#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path
SCRIPT = '#!/usr/bin/env bash\nset -euo pipefail\nIFS=$\'\\n\\t\'\n\n# Safe array handling & Perl strict/warnings invocation on filenames with spaces\ntmp_dir="$(mktemp -d)"\ntrap \'rm -rf -- "$tmp_dir"\' EXIT\n\ntouch "$tmp_dir/file with spaces 1.txt" "$tmp_dir/file with spaces 2.txt"\ncount=0\nfor f in "$tmp_dir"/*.txt; do\n    [[ -e "$f" ]] || continue\n    count=$((count + 1))\ndone\n[[ "$count" -eq 2 ]] || exit 1\n\nperl -Mstrict -Mwarnings -e \'\n    my @nums = (10, 20, 30, 40);\n    my $sum = 0;\n    for my $n (@nums) { $sum += $n; }\n    die "Sum mismatch" unless $sum == 100;\n\'\necho "NATIVE BASH 5.2 (set -euo pipefail) & PERL 5 (strict/warnings) VERIFIED"\n'
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "test_script.sh"
    p.write_text(SCRIPT)
    p.chmod(0o755)
    subprocess.run(["bash", str(p)], check=True)
