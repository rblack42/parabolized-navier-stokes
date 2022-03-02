module init
  use shared
  implicit none

contains
  
  subroutine reset()
    real tref, xmuref, reref
    real an, drcon, pi, rm, xplot, et
    real dx0
    integer i
    tref = 1464.7157
    xmuref = 7.65034e-7
    reref = 2179168

    minf = 5.95
    thetas = 22
    x0 = 0.5
    dxi = 0.0004
    xmuinf = 0.00002
    beta = -20.0
    neta = 31
    nitmax = 750
    nplot = 25
    dplot = 0.1
    xplot = 0.1

    hinf = (1.0 + 2.0 / (0.4 * minf**2))/2.0
    pinf = 1.0 / (1.4 * minf**2)
    an = neta - 1
    nem1 = neta - 1
    deta = 1.0 / an
    pi = acos(-1.0)
    drcon = pi / 180.0

    xl1 = 22.5
    xl2 = xl1 + 27.5
    xh = 4.25
    rn = xh/2.0 + xl1*xl1/(2.0 *xh)
    
    thetab = asin((xl1 - x0)/rn)
    thetas = thetas * drcon
    
    rb0 = xh -  rm + sqrt(rn * rn -(xl1-x0)**2)
    dx0 = rb0 / tan(thetab) - x0

    x0 = x0 + dx0
    xl1 = xl1 + dx0
    xl2 = xl2 + dx0

    ! initial conditions - freestream
    et = 0.0
    do i = 1,neta
      eta(i) = et
      r(i) = 1.0
      u(i) = 1.0
      v(i) = 1.0
      p(i) = pinf
      et = et + deta
    end do

    ! boundary condition on surface
    u(1) = 0.0
    v(1) = 0.0

    mit = 0
  end subroutine reset

end module init

