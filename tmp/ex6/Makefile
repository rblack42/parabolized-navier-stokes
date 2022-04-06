# weather-buoys Makefile

TARGET	= tsunami
SRCS	= mod_diff.f90 \
		  mod_io.f90 \
		  mod_parallel.f90 \
		  mod_field.f90 \
		  tsunami.f90
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
