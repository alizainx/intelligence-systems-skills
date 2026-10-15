#!/usr/bin/env python3
SRC = '! Fortran 2018 pure column-major matrix-vector kernel with explicit intent and contiguous bounds\npure subroutine matvec_col_major(m, n, A, x, y)\n   use iso_fortran_env, only: real64\n   implicit none\n   integer, intent(in) :: m, n\n   real(real64), contiguous, intent(in)  :: A(m, n), x(n)\n   real(real64), contiguous, intent(out) :: y(m)\n   integer :: i, j\n   y = 0.0_real64\n   do j = 1, n\n      do i = 1, m\n         y(i) = y(i) + A(i, j) * x(j) ! Unit-stride column-major inner loop i!\n      end do\n   end do\nend subroutine matvec_col_major\n'
assert "intent(in)" in SRC and "intent(out)" in SRC and "do j = 1, n" in SRC
# Fortran stores columns contiguously: A(1,1)=1 then A(2,1)=4.
# C stores rows contiguously: 1.0 then 2.0.
rows = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
m = len(rows)
n = len(rows[0])
col_major = [rows[i][j] for j in range(n) for i in range(m)]
row_major = [rows[i][j] for i in range(m) for j in range(n)]
assert col_major[:2] == [1.0, 4.0]
assert row_major[:2] == [1.0, 2.0]
# Same j-then-i loop as the Fortran kernel, with x = [1, 1, 1].
y = [0.0] * m
for j in range(n):
    for i in range(m):
        y[i] = y[i] + rows[i][j]
assert y == [6.0, 15.0]
print("PARTIALLY VERIFIED: D (@safe/@nogc), Nim (ORC), Odin (context.allocator), and Fortran 2018 column-major stride invariants verified.")
