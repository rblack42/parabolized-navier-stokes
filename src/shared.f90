module shared
  implicit none

  logical :: march, convrg, defdat, betlok
  character :: flag
  real, dimension(51) ::  r, u, v, p, eta
  real :: minf, hinf, xmuinf, beta, pinf
  real :: xl1, xl2, xh, rn, x0, thetas, thetab
  real, dimension(2) :: rb, rs, rbx, rsx, x
  real :: rb0, xf1
  real :: aa, bb, cc, dd, ee, rr, uu, vv, pp
  integer :: mit, nplot, nitmax, neta, nem1
  real :: deta, xmu1, xmu2, dxi, delm
  real :: dplot, xplot
end module shared
