SRCS	= hello.f90
OBJS	= $(SRCS:.f90=.o)
TARGET	= $(SRCS:.f90=)

FCC		= gfortran

all:	$(TARGET)

$(TARGET):	$(OBJS)
	$(FCC) $^ -o $@

%.o:	%.f90
	$(FCC) -c $^ -o $@
