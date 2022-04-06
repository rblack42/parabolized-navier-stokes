SRCS	= mod_initial.f90 mod_diff.f90 main.f90
TARGET	= tsumani

FCC		= gfortran

all:	$(TARGET)

$(TARGET):	$(SRCS)
	FoBiS.py build -o $(TARGET)

clean:
	rm -rf obj mod

run:	$(TARGET)
	./$(TARGET) > output.txt
	python plot.py output.txt
