module nogc_ring_slice;

@safe @nogc nothrow pure
bool checkedSliceSum(scope const(long)[] data, out long total) {
    total = 0;
    foreach (v; data) {
        if ((v > 0 && total > long.max - v) || (v < 0 && total < long.min - v))
            return false;
        total += v;
    }
    return true;
}
