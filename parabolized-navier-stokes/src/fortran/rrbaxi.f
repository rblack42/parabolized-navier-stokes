C*******************************************************************
C
C    RRBAXI - AXISYMMETRIC NAVIER STOKES SOLVER
C         Capt. Roie R. Black
C		  AFIT/ENC . 54185
C
C This program is a test bed for examining methods for solving
C the parabolized Navier Stokes equations. It is currently
C folving a simplified form of the axisymmetric equations
C consisting of the following:
C
C	1) Continuity equation
C	2) X momentum equation
C	3) R momentum equation
C	4) Constant total enthalpy
C	5) State equation
C	6) A simplified eddy viscosity equation
C
C The solution procedure being used is an explicit
C procedure employing MacCormack's explicit method in
C the supersonic floe field (wall is no-slip, first point away
C from the wall must be supersonic. Hypersonic flow works best.
C An arbitrary coordinate transformation is being used
C to obtain a coordinate system that is aligned with the body
C and a ray emanating from the tip of the body at some prescribed
C angle. The body in this test case is an ogive cylinder which is
C being approximated with a polynomial fit from a conical nose tip
C to a cylindrical after body. The polynomial was chosen to eliminate
any curvature discontinuities which can upset the flow.
C
C**********************************************************************

      PROGRAM main
      LOGICAL march,convrg,defdat, betlok
      CHARACTER flag
      COMMON // r(51),u(51),v(51),p(51).eta(51)
     1   ,xminf,hinf,xmuinf,beta,pinf,betlok
     2   ,xl1,xl2,xh,rn,x0,thetas,thetab
     3   ,rb1,rb2,rs1,rs2,rbx1,rbx2,rsx1,rsx2,x1,x2
     4   ,aa,bb,cc,rr,uu,vv,pp
     5   ,mit,nplot,march,nitmax,neta,nem1
     6   ,deta,xmu1,xmu2,dxi,delm
C*****
C  Set logical flags for
C  a) Marching down the body or not (working on starting solution)
C  b) indicating converged starting cone solution
C*****
      march = .FALSE.
      convrg = .FALSE.
C*****
C call C routine to clear screen
C*****
      CALL clear
      STOP
      END

