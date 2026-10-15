package com.iss.jvm;
import java.util.Objects;

public sealed interface SealedOrderState
    permits SealedOrderState.Pending, SealedOrderState.Filled, SealedOrderState.Cancelled {

    record Pending(long orderId, long qty) implements SealedOrderState {
        public Pending {
            if (qty <= 0) throw new IllegalArgumentException("qty must be > 0");
        }
    }
    record Filled(long orderId, long filledQty, long priceMicros) implements SealedOrderState {}
    record Cancelled(long orderId, String reason) implements SealedOrderState {
        public Cancelled { Objects.requireNonNull(reason, "reason"); }
    }
}
