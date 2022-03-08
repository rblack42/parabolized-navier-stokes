cmake_minimum_required(VERSION 3.10)
project(rrbaxi Fortran)

enable_language(Fortran)
set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} \
	-O \
	-finit-real=inf \
	-ffpe-trap=invalid,zero \
	-fdefault-real-8")

add_library(rrbaxi SHARED
	src/shared.f90
	src/init.f90
	src/prtplot.f90
	src/body.f90
	src/solve.f90
	src/maccormack.f90
)
