class FreeStream:

    self.minf  	= 5.95
    self.tref   = 1464.7157
    self.reref  = 2179168.0
    self.muref  = 7.65034e-7
    self.muinf  = 0.00002
    self.thetas = 22.0
    self.dxi    = 0.0004
    self.neta   = 31
    self.nitmax = 750
    self.nplot  = 25
    self.dplot  = 0.05

    # computed values ------------------------------------
    self.hinf    = (1.0+2.0/(0.4*self.xminf**2))/2.0
    self.pinf    = 1.0/(1.4*self.xminf**2)

    self.thetas  = self.thetas* drcon
    self.rn  = self.xh/2.0+self.xl1*self.xl1/(2.0*self.xh)
    self.thetab  = math.asin((self.xl1-self.x0)/self.rn)
    self.rb0 = self.xh - self.rn + math.sqrt(self.rn**2-(self.xl1-self.x0)**2)
    self.dx0 = self.rb0/math.tan(self.thetab) - self.x0
    self.deta   = 1.0/float(self.neta-1)
fs.thetas
