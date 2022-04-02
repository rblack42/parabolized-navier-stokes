program tsunami
  implicit none

  integer :: i, n
  integer, parameter :: grid_size = 100
  integer, parameter :: num_time_steps = 100

  real, parameter :: dt = 1, dx = 1, c = 1
  real  :: h(grid_size), dh(grid_size)

  integer, parameter :: icenter = 25
  real, parameter :: decay = 0.02

  character(*), parameter :: fmt = '(i0,*(1x,es15.8e2))'

  do concurrent (i = 1:grid_size)
    h(i) = exp(-decay * (i-icenter)**2)
  end do

  print fmt, 0, h

  time_loop: do n = 1, num_time_steps
    dh(1) = h(1) - h(grid_size)
    do concurrent (i = 2:grid_size)
      dh(i) = h(i) - h(i-1)
    end do
    do concurrent (i = 1:grid_size)
      h(i) = h(i) - c * dh(i) / dx * dt
    end do
    print fmt, n, h
  end do time_loop


end program tsunami
