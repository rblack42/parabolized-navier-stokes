program tsunami

  use iso_fortran_env, only: int32, real32
  use mod_diff, only: diff => diff_centered
  use mod_initial, only: set_gaussian

  implicit none

  integer(int32) :: i, n
  integer(int32), parameter :: grid_size = 100
  integer(int32), parameter :: num_time_steps = 5000
  real(real32), parameter :: dt = 0.02, dx = 1, g = 9.8
  real(real32), parameter :: hmean = 10

  real(real32)  :: h(grid_size), u(grid_size)

  integer(int32), parameter :: icenter = 25
  real(real32), parameter :: decay = 0.02

  call set_gaussian(h, icenter, decay)
  u = 0

  print *, 0, h
  time_loop: do n = 1, num_time_steps
    u = u - (u * diff(u) + g * diff(h)) / dx * dt
    h = h - diff(u * (hmean + h)) / dx * dt
    print *, n, h
  end do time_loop

end program tsunami
