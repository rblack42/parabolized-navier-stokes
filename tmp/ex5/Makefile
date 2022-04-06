# weather-buoys Makefile

TARGET	= weather_stats_parallel
SRCS	= mod_arrays.o mod_io.o mod_parallel.o weather_stats_parallel.o
OBJS	= $(SRCS:.f90=.o)
MPILIB	= /usr/local/Cellar/opencoarrays/2.9.2_1/lib
FCC		= mpifort
HOSTFILE = hostfile

RM		= rm -f

all: $(TARGET)

$(TARGET):	$(OBJS)
	mpifort -L$(MPILIB) *.o -lcaf_mpi -o $(TARGET)

%.o:	%.f90
	$(FCC) -fcoarray=lib -c $<

.PHONY: clean
clean:
	$(RM) weather_stats* *.o
