CADIR	=	/usr/local/cellar/opencoarrays/2.9.2_1
SRCS	=	$(wildcard *.f90)
OBJS	=	$(SRCS:.f90=.o)
TARGET	=	diffusion
FCC		=	mpifort

$(TARGET):	$(OBJS)
	echo $(OBJS)
	${FCC} -L${CADIR}/lib -lcaf_mpi -o $(TARGET)

%.o:	%.f90
	$(FCC} -fcoarray=lib -c $<

clean:
	-rm -f $(TARGET)
	-rm -f */*.o
