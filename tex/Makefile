TEXDOC	= main
LATEXMK = latexmk

all: pdf

pdf:	main.tex
	$(LATEXMK) -M -MP -MF $*.deps $*

clean:
	latexmk -c
