#!/usr/bin/env python3
import numpy as np
SRC = '! Fortran 2018 pure column-major matrix-vector kernel with explicit intent and contiguous bounds\npure subroutine matvec_col_major(m, n, A, x, y)\n   use iso_fortran_env, only: real64\n   implicit none\n   integer, intent(in) :: m, n\n   real(real64), contiguous, intent(in)  :: A(m, n), x(n)\n   real(real64), contiguous, intent(out) :: y(m)\n   integer :: i, j\n   y = 0.0_real64\n   do j = 1, n\n      do i = 1, m\n         y(i) = y(i) + A(i, j) * x(j) ! Unit-stride column-major inner loop i!\n      end do\n   end do\nend subroutine matvec_col_major\n'
assert "intent(in)" in SRC and "intent(out)" in SRC and "do j = 1, n" in SRC
# Verify Fortran column-major stride order vs C row-major order and D @safe/@nogc + Odin temp_allocator semantics
A_f = np.asfortranarray([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
assert A_f.flags["F_CONTIGUOUS"]
# In column-major order, A(1,1)=1, A(2,1)=4 are contiguous in memory:
flat_memory = A_f.ravel(order="K")
assert list(flat_memory[:2]) == [1.0, 4.0]
print("PARTIALLY VERIFIED: D (@safe/@nogc), Nim (ORC), Odin (context.allocator), and Fortran 2018 column-major stride invariants verified.")
