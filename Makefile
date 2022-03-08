PROJPATH = $(PWD)
PROJNAME = $(notdir $(PROJPATH))

FSRCS	:= src/shared.f90 \
		   src/init.f90 \
		   src/prtplot.f90 \
		   src/body.f90 \
		   src/solve.f90 \
		   src/maccormack.f90 \
		   src/main.f90
FOBJS	:= $(FSRCS:.f90=.o)
FFLAGS	:= -O -std=f2018 -Jmod -fcheck=bounds

.PHONY: build
build:	$(FOBJS)
	gfortran -o $(PROJNAME) $^

%.o:	%.f90
	gfortran -c -o $@ $< $(FFLAGS)

.PHONY: clean
clean:
	rm -f $(FOBJS)
	rm -f mod/*

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: pyinit
pyinit:
	pip install -U pip pip-tools

.PHONY: reqs
reqs:
	pip-compile
	pip install -r requirements.txt
	cp ~/_sys/tikzmagic.py .direnv/python-3.10.2/lib/python3.10/site-packages/

.PHONY: nb
nb:
	cd book && \
		jupyter notebook

.PHONY: bool
book:
	jb build book
	cp -R book/* docs

.PHONY: tex
tex:
	cd tex && \
	pdflatex main &&  \
	bibtex main && \
	pdflatex main && \
	pdflatex main
