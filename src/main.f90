program hello
  use shared
  use init
  use body
  use solver
  use prtplot
  implicit none
  ! This is a comment line; it is ignored by the compiler
  print *, 'Hello, World!'

  ! initialize shared data
  call reset
  !call ogive_cylinder
  call solve(1)
  call plot
end program hello
