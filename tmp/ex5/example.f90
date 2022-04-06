! example.f90
module mpi_master
! The OpenMPI master process module.
    implicit none
    private
    public :: master
contains
    subroutine master(nworkers)
        character(len=*), parameter :: fmt = '("--- Master [", i4, 5(a, i2.2), "]")'
        integer, intent(in)         :: nworkers
        integer                     :: dt(8)

        call date_and_time(values=dt)
        print fmt, dt(1), '/', dt(2), '/', dt(3), ' ', dt(5), ':', dt(6), ':', dt(7)
    end subroutine master
end module mpi_master

module mpi_worker
! The OpenMPI worker process module.
    implicit none
    private
    public :: worker
contains
    subroutine worker(nworkers, rank)
        integer, intent(in) :: nworkers
        integer, intent(in) :: rank

        print '(a, i0)', '>>> Hello from worker ', rank
        call sleep(1)
    end subroutine worker
end module mpi_worker

program main
! Example program that calls OpenMPI.
    use, intrinsic :: iso_fortran_env, only: real64
    use :: mpi
    use :: mpi_master
    use :: mpi_worker
    implicit none
    real(kind=real64) :: t1, t2
    integer           :: master_rank
    integer           :: nproc
    integer           :: nworkers
    integer           :: rank
    integer           :: rc

    ! Initialise OpenMPI communication infrastructure.
    call mpi_init(rc)

    ! Get number of active processes.
    call mpi_comm_size(mpi_comm_world, nproc, rc)

    master_rank = 0
    nworkers    = nproc - 1

    ! Identify process.
    call mpi_comm_rank(mpi_comm_world, rank, rc)

    if (rank == master_rank) then
        ! Master process.
        t1 = mpi_wtime()
        call master(nworkers)
        t2 = mpi_wtime()

        print '("--- Timing: ", f6.4, " sec on ", i0, " workers")', t2 - t1, nworkers
    else
        ! Worker process.
        call worker(nworkers, rank)
    endif

    ! Terminate OpenMPI communication infrastructure.
    call mpi_finalize(rc)
end program main
