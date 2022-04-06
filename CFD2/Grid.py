import math
import FreeStream as fs


class Grid(object):
 
	def __init__(self):
		pi = math.acos(-1.0)
		drcon = pi/180.0

		# body properties
		self.x0 = 5.0
		self.xl1 = 22.5
		self.xl2 = self.xl1 + 27.5
		self.xh = 4.25
		
		self.x0
		self.rho = []
		self.u = []
		self.v = []
		self.t = []
		self.pt = []
		self.mach = []
		self.h = []
		self.x = [self.x0, self.x0 + self.dxi]
		tants = math.tan(fs.thetas)
		self.rs = [self.x[0] * tants, self.x[1] * tants]
		self.rsx = tan(fs.thetas)
		self.rbx = tan(fs.thetab)

	def reset(self):
		# set initial conditions for calculations
		for i in range(fs.neta+1):
			rho.append(1.0)
			u.append(1.0)
			v.append(0.0)
			p.append(fs.pinf)
		u[0] = 0.0 # no slip condition
			
			

