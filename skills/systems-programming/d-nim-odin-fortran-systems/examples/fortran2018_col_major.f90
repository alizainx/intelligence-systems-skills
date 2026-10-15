! Fortran 2018 pure column-major matrix-vector kernel with explicit intent and contiguous bounds
pure subroutine matvec_col_major(m, n, A, x, y)
   use iso_fortran_env, only: real64
   implicit none
   integer, intent(in) :: m, n
   real(real64), contiguous, intent(in)  :: A(m, n), x(n)
   real(real64), contiguous, intent(out) :: y(m)
   integer :: i, j
   y = 0.0_real64
   do j = 1, n
      do i = 1, m
         y(i) = y(i) + A(i, j) * x(j) ! Unit-stride column-major inner loop i!
      end do
   end do
end subroutine matvec_col_major
