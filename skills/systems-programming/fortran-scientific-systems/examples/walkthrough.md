# Nontrivial Implementation & Multi-File Engineering Walkthrough: `fortran-scientific-systems`

- **Target File**: `examples/col_major_spmv.f90`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
module col_major_spmv
  use, intrinsic :: iso_fortran_env, only: real64, int32
  use, intrinsic :: iso_c_binding, only: c_double, c_int32_t
  implicit none (type, external)
  private
  public :: matvec_col_major
contains
  pure subroutine matvec_col_major(n, m, a, x, y) bind(C, name="matvec_col_major")
    integer(c_int32_t), value, intent(in) :: n, m
    real(c_double), intent(in)  :: a(n, m), x(m)
    real(c_double), intent(out) :: y(n)
    integer(int32) :: i, j
    y = 0.0_real64
    do j = 1, m
      do i = 1, n
        y(i) = y(i) + a(i, j) * x(j)
      end do
    end do
  end subroutine matvec_col_major
end module col_major_spmv

```
