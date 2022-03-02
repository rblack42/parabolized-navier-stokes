#--------------------------------------------------------------------
# File:     BodyPlotter.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

import Tkinter
import Pmw

from Body import *
from LinePlot import *

class BodyPlotter:
    '''Class to manage plotting body data'''

    def __init__(self,parent,width,height):
        '''CONSTRUCTOR - initialize the body data'''
        self.body = OgiveCylinder()
        self.length = self.body.bodylength
        self.width = width
        self.height = height
        self.plotter = LinePlot(parent,width,height)

    def plotBody(self):
        '''Plot the body in a window widthxheight pixels big'''
        dxi = self.length/float(self.width)
        scale=1.0
        points = self.body.getBodyPoints(self.width,dxi,scale)
        scale = 35.0
        slopes = self.body.getBodySlopes(self.width,dxi,scale)
        scale = -100.0
        curves = self.body.getBodyCurvatures(self.width,dxi,scale)
        self.plotter.setLine(points,'black',3)
        self.plotter.setLine(slopes,'blue',1)
        self.plotter.setLine(curves,'red',1)
        self.plotter.drawLines()

if __name__ == "__main__":
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title("Body Plot");
    exitButton = Tkinter.Button(root,text='Exit',command=root.destroy)
    exitButton.pack(side='bottom')
    bp = BodyPlotter(root,640,200)
    bp.plotBody()
    root.mainloop()

        
