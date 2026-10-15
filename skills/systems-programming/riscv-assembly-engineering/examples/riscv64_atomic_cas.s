# RV64GC atomic compare-and-swap using lr.d.aq / sc.d.rl
.text
.globl rv64_atomic_cas_u64
.type rv64_atomic_cas_u64, @function
rv64_atomic_cas_u64:
    # a0 = ptr, a1 = expected, a2 = desired
.Lretry:
    lr.d.aq t0, (a0)
    bne t0, a1, .Lfail
    sc.d.rl t1, a2, (a0)
    bnez t1, .Lretry
    li a0, 1
    ret
.Lfail:
    li a0, 0
    ret
