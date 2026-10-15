# Defensive Scripting & Dynamic Language Security Matrix

Never parse `ls` output or unquoted `$@`; always iterate over globs `"$dir"/*.ext` with `nullglob` or `[[ -e "$f" ]]`.
