subroutine f90wrap_driver(minf, rho, n, n0)
    implicit none
    external driver
    
    real, intent(in) :: minf
    real, intent(inout), dimension(n0) :: rho
    integer, intent(in) :: n
    integer :: n0
    !f2py intent(hide), depend(rho) :: n0 = shape(rho,0)
    call driver(minf, rho, n)
end subroutine f90wrap_driver

