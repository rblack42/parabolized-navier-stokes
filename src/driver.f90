subroutine driver (minf, rho, n)
  implicit none
  integer intent(in) :: n
  real intent(out) :: rho(:)
  real intent(in) :: minf

  integer i

  do i = 1,n
    rho(i) = minf**2
  end do
end subroutine driver


