SRCS	= main.f90
OBJS	= $(SRCS:.f90=.o)
TARGET	= tsumani

FCC		= gfortran

all:	$(TARGET)

$(TARGET):	$(OBJS)
	$(FCC) $^ -o $@

%.o:	%.f90
	$(FCC) -c $^ -o $@

run:	$(TARGET)
	./$(TARGET) > output.txt
	python plot.py output.txt
