#--------------------------------------------------------------------
# File:     GridPlotter.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

import tkinter
import Pmw
from Body import *
from OuterBoundary import *
from LinePlot import *
from ColorList import *

class GridPlotter:
    '''Class to manage display of computational grid'''

    def __init__(self,parent,width,height,angle):
        '''CONSTRUCTOR - initialize the grid display'''
        self.body = OgiveCylinder()
        self.boundary = OuterCone(angle,self.body.bodylength)
        self.length = self.body.bodylength
        self.width = int(width)
        self.height = height
        self.colorList = ColorScale(11)
        self.type = 0
        self.plotter = LinePlot(parent,width,height)

    def setGridType(self,type):
        self.type = type
        
    def plotGrid(self):
        '''Plot the grid in a window width x height pixels'''
        dxi = self.length/float(self.width)
        scale = 1.0
        type = self.type    # (0 = physical plot, !=0 = eta plot
        # draw the body and outer boundary
        points = self.body.getBodyPoints(self.width,dxi,scale)
        bounds = self.boundary.getBoundaryPoints(self.width,dxi,scale)
        self.plotter.setLine(points,'black',2)
        self.plotter.setLine(bounds,'black',2)
        self.plotter.drawLines()

        # now plot the polygons for the grid
        dx = dxi*10.0
        neta = 11
        if type != 0:
            neta = 129
        self.colorList.setColorList(neta)
        for nx in range(int(self.width/10)):
            x1 = float(nx)*dx
            x2 = float(nx+1)*dx
            rb1 = self.body.body.getRadius(x1)
            rb2 = self.body.body.getRadius(x2)
            if type == 0:
                rs1 = self.boundary.body.getRadius(x1)
                rs2 = self.boundary.body.getRadius(x2)
            else:
                rs1 = self.height*dxi
                rs2 = self.height*dxi
            deta1 = (rs1 - rb1)/float(neta-1)
            deta2 = (rs2 - rb2)/float(neta-1)
            xp1 = x1/dxi
            xp2 = x2/dxi
            # now loop over the neta polygons
            yp1 = self.height - rb1/dxi
            yp2 = self.height - rb2/dxi
            for ny in range(neta-1):
                yp3 = self.height - (float(ny+1)*deta1 + rb1)/dxi
                yp4 = self.height - (float(ny+1)*deta2 + rb2)/dxi
                # draw the polygon
                color = self.colorList.getColor(ny)
                self.plotter.drawFilledPolygon(xp1, \
                        yp1,xp1,yp3,xp2,yp4,xp2,yp2,color)
                #print("%10.6f %10.6f %10.6f %10.6f %10.6f\n" % ( \
                #        x1,rb1,rs1,yp1,xp1))
                yp1 = yp3
                yp2 = yp4

    def clearScreen(self):
        self.plotter.clearScreen()

if __name__ == "__main__":
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title("Grid Plot");
    exitButton = Tkinter.Button(root,text='Exit',command=root.destroy)
    exitButton.pack(side='bottom')
    bp = GridPlotter(root,640,350,22.0)
    bp.setGridType(0)
    bp.plotGrid()
    root.mainloop()
