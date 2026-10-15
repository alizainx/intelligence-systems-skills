# Nontrivial Implementation & Multi-File Engineering Walkthrough: `php-zend-strict-typing`

- **Target File**: `examples/StrictReadonlyMoney.php`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
<?php
declare(strict_types=1);

namespace Iss\Php;

enum Currency: string {
    case USD = 'USD';
    case EUR = 'EUR';
}

final readonly class StrictReadonlyMoney {
    public function __construct(
        public int $minorUnits,
        public Currency $currency,
    ) {
        if ($this->minorUnits < 0) {
            throw new \InvalidArgumentException('minorUnits must be non-negative');
        }
    }
}

```
