# Legacy Migration Semantic Traps Reference

C integer division `-3 / 2` truncates toward zero (`-1`), whereas Python `-3 // 2` floors toward $-\infty$ (`-2`); migrating math/hash code without `int(a / b)` breaks negative inputs!
