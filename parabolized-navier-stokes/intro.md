# Parabolized Navier Stokes Equations

This document is a *Jupyter-Book* that uses Python *SymPy* to generate an
example program that solves the *Parabolized Navier Stokes* equations for
axisymmetric flow over an ogive-cylinder flying at Mach 6. This project was
originally developed by the author in 1976 while working as a research
scientist at the USAF Aerospace Research Laboratory at Wright-Patterson AFB in
Dayton, Ohio. This was my first assignment in the USAF after getting my degrees
in Aerospace Engineering at Virginia Tech. This project was part of research I
was conducting for my PhD, but I never managed to complete the dissertation.

At the time, the program was written in FORTRAN, and ran on a CDC 6600, one of
the most powerful computers available at the time. The code served as the basis
for several Master's thesis projects a few years later, when I was teaching
Computer Science at the Air Force Institute of Technology, also in at WPAFB.

In 2003, I rewrote the original code in Python while working on a second
Master's degree, this time in Computer Science at Texas State University in San
Marcos, Texas. I found my original notes and decided it was time to put them
into use once again, to build an updated version of the code.

The derivation of the equations used in this project found in the appendix, are
transcriptions of my original notes. I kept those and a listing of the original
FORTRAN code as well.

Just for fun, the Fortran code is also included here, rewritten to run under
GNU **gfortran**. The code has been updated to Fortran-2008, but is otherwise
identical to code I have not touched in 40 years!

All code presented in this book was tested on my Macbook Pro. The CDC code took
about 10 minutes of machine time back in 1976. That same code nor runs in less
than 5 seconds on my laptop! Progress!


- Roie Black
- Major, USAF (retired)
- Professor, Computer Science (retired)

- B.S., M.S, Aerospace Engineering
- M.S., Computer Science



