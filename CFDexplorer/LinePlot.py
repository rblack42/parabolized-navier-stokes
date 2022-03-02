#--------------------------------------------------------------------
# File:     LinePlot.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from tkinter import *

class LinePlot:
    ''' Basic Line Plot class'''

    def __init__(self,parent,width,height):
        '''CONSTRUCTOR - initialize line plot object'''
        self.parent = parent
        self.width = width
        self.height = height
        canvas = Canvas(parent,width=width, height=height, bg='white')
        canvas.pack()
        self.canvas = canvas
        self.lines = []
        self.colors = []
        self.widths = []

    def setLine(self,lines,color,thick):
        '''Set a line into the plotting object for display'''
        self.lines.append(lines)
        self.colors.append(color)
        self.widths.append(thick)

    def clearLines(self):
        '''Clear the line set from the plotting object'''
        self.lines=[]
        self.colors=[]
        self.widths=[]
        
    def drawLines(self):
        '''Draw the current line set in LinePlot window'''
        for l in range(len(self.lines)):
            color = self.colors[l]
            thick = self.widths[l]
            for i in range(len(self.lines[l]) - 1):
                x1,y1 = self.lines[l][i]
                y1 = self.height-y1
                x2,y2 = self.lines[l][i+1]
                y2 = self.height-y2
                self.canvas.create_line(x1,y1,x2,y2,width=thick,fill=color)
            
    def drawOutlinePolygon(self,x0,y0,x1,y1,x2,y2,x3,y3,color):
        '''Draw an outlined, filled polygon in the LinePlot Window'''
        self.canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,
            width=1,outline='black',fill='yellow')
        
    def drawFilledPolygon(self,x0,y0,x1,y1,x2,y2,x3,y3,color):
        '''Draw a filled, no outline polygon in the LinePlot Window'''
        self.canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,
            width=1,fill=color)  
        
    def clearScreen(self):
        self.canvas.delete(ALL)

if __name__ == "__main__":
    root = Tk()
    root.title = "Test Plot"
    Button(root,text='Exit',command=root.quit).pack(side=BOTTOM)
    plot = LinePlot(root,640,100)
    line = [(50,50), (100,75), (200,50)]
    plot.setLine(line,'black',1)
    line = [(50,40), (100,65), (200,40), (250,50)]
    plot.setLine(line,'blue',1)
    line = [(50,30), (100,55), (200,30), (250,40), (300,30)]
    plot.setLine(line,'red',1)
    plot.drawLines()
    root.mainloop()

