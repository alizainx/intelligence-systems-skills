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
