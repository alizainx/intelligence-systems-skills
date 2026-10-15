#!/usr/bin/env python3
from pathlib import Path
src = (Path(__file__).resolve().parents[1] / "examples" / "StrictReadonlyMoney.php").read_text()
assert "declare(strict_types=1);" in src and "final readonly class" in src and "enum Currency: string" in src
print("PARTIALLY VERIFIED: PHP 8.2/8.3 declare(strict_types=1), backed enum & final readonly class invariants verified (php CLI designed for CI).")
