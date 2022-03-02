#--------------------------------------------------------------------
# File:     CFDexplorer.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from tkinter import *
import Pmw
from InitialConditions import *
from GridPlotter import *
from CFDmenu import *
from EQNexplorer import *
from AXIsolver import *
from Body import *
from OuterBoundary import *
import colorsys

class CFDexplorer(Pmw.MegaWidget):
    pgm_version='1.0'
    pgm_name = 'Computational Fluid Dynamics Explorer - v1.0'
    pgm_copyright = 'Copyright (c) 2003 SK Consulting Services.' + \
        ' All rights reserved'
    pgm_contact = 'Roie R. Black'
    pgm_contactemail = 'rblack@skcon.com'

    pgm_width   = 800
    pgm_height  = 600
    
    def __init__(self):
        self.root = Tk()
        Pmw.initialise(self.root)
        self.initializePgm(self.root)
        self.root.title(self.pgm_name)
        self.root.geometry('%dx%d' % 
            (self.pgm_width, self.pgm_height))
        Pmw.MegaWidget.__init__(self,parent=self.root)        
        self.focus_set()
        frame= Frame(self.root,width=self.pgm_width,height=self.pgm_height);
        self.__BuildScreen(frame)
        frame.pack(side='top',expand=YES,fill=BOTH,padx=5,pady=5)

    def initializePgm(self,root):
        root.option_readfile('options.db')
        root.option_add('*foreground','black')

    def run(self):
        self.pack()
        self.mainloop()
        
    def __createAbout(self):
        Pmw.aboutversion(self.pgm_version)
        Pmw.aboutcopyright(self.pgm_copyright)
        Pmw.aboutcontact(
                'For more information, contact: %s\n Email: %s\n' %\
                (self.pgm_contact, self.pgm_contactemail))
        self.about = Pmw.AboutDialog(self._hull,
                applicationname=self.pgm_name)
        self.about.withdraw()
        return None

    def showAbout(self):
        self.about.show()
        self.about.focus_set()

    def __createColorPicker(self):
        '''Display a color picker window to fetch color lmits'''
        self.colorpicker = Pmw.Dialog(self._hull,buttons=('Pick',))
        self.colorpicker.withdraw()
        canvas=Canvas(self.colorpicker.interior(),
                width=100,height=100)
        canvas.pack()
        hue = Label(canvas,text='Hue')
        hue.grid(row=0,column=0)
        light = Label(canvas,text='Lightness')
        light.grid(row=0,column=1)
        sat = Label(canvas,text='Saturation')
        sat.grid(row=0,column=2)
        self.rgb = Label(canvas,text='RGB:(0,0,0)')
        self.rgb.grid(row=0,column=3)

        self.cph = Scale(canvas,from_=255,to=0,command=self.update)
        self.cph.grid(row=1,column=0)
        self.cpl = Scale(canvas,from_=255,to=0,command=self.update)
        self.cpl.grid(row=1,column=1)
        self.cps = Scale(canvas,from_=255,to=0,command=self.update)
        self.cps.grid(row=1,column=2)

        self.cpc = Canvas(canvas,width=100,height=100,bg='Black')
        self.cpc.grid(row=1,column=3)
        

    def update(self,*args):
        'Get the scale values and change the canvas color'
        r,g,b = colorsys.hls_to_rgb(self.cph.get()/255.0,
                                    self.cpl.get()/255.0,self.cps.get()/255.0)
        r,g,b = r*255,g*255,b*255
        self.rgb.configure(text='RGB:(%d,%d,%d)' % (r,g,b))
        self.cpc.configure(bg='#%02X%02X%02X' % (r,g,b))
        
    def showPicker(self):
        self.colorpicker.activate()
        self.colorpicker.focus_set()
        
    def __createSolver(self,parent):
        frame=Frame(parent,borderwidth=1,relief=GROOVE)
        f1 = Frame(frame,borderwidth=1,relief=GROOVE)
        self.__createInitialConditions(f1)
        f1.pack(side='left',padx=5,pady=5)
        f2 = Frame(frame,borderwidth=1,relief=GROOVE)
        self.__createPlotArea(f2)
        f2.pack(side='left',padx=5,pady=5)
        frame.pack(side='top',padx=5,pady=5)
        
    def __createInitialConditions(self,parent):
        frame = Frame(parent)
        self.init = InitialConditions(frame)
        v = self.init.getValues()
        self.AXIsolver = AXIsolver(v)
        self.body = OgiveCylinder()
        self.shock = OuterCone(v['thetas'],self.body.bodylength)
        self.AXIsolver.setBody(self.body)
        self.AXIsolver.setShock(self.shock)
        self.AXIsolver.setPrinter(0)
        self.AXIsolver.setExplorer(0)
        self.__createButtons(frame)
        frame.pack(side='left',padx=5,pady=5)
        
    def __createPlotArea(self,parent):
        frame = Frame(parent)
        self.grid = GridPlotter(frame,800,400,22.0)
        self.AXIsolver.setPlotter(self.grid)
        self.grid.plotGrid()
        frame.pack(side='left')

    def __createEquations(self,parent):
        frame=Frame(parent,borderwidth=1,relief=GROOVE)
        self.equations = EQNexplorer(frame,self.AXIsolver)
        frame.pack(side='top',padx=5,pady=5)

    def __createMenu(self,parent,program):
        frame=Frame(parent)
        menu = CFDmenu(frame,program)
        frame.pack(side='top',expand=1,fill='x')

    def __createButtons(self,parent):
        '''Set up Control Buttons for solver control'''
        frame=Frame(parent)
        self.bbox1 = Pmw.ButtonBox(frame)
        self.bbox1.add('clear',command=self.clearScreen)
        self.bbox1.alignbuttons()
        
        self.bbox2 = Pmw.ButtonBox(frame)
        self.bbox2.add('X-R Grid',command=self.showXR)
        self.bbox2.add('Xi-Eta Grid',command=self.showXE)
        
        self.bbox3 = Pmw.ButtonBox(frame)
        self.bbox3.add('X-R Data',command=self.showXRdata)
        self.bbox3.add('Xi-Eta Data',command=self.showXEdata)
        self.bbox1.alignbuttons()
        self.bbox2.alignbuttons()
        self.bbox3.alignbuttons()
        self.bbox1.pack(side='top')
        self.bbox2.pack(side='top')
        self.bbox3.pack(side='top')
        frame.pack(side='top',padx=10,pady=20)

    def clearScreen(self):
        '''Clear the Plotting area'''
        self.grid.clearScreen()

    def showXR(self):
        '''Display the grid in XY coordinates'''
        self.grid.clearScreen()
        self.grid.setGridType(0)
        self.grid.plotGrid()

    def showXE(self):
        '''Display the grid in XY coordinates'''
        self.grid.clearScreen()
        self.grid.setGridType(1)
        self.grid.plotGrid()

    def showXRdata(self):
        '''Display the data in XY coordinates'''
        self.grid.clearScreen()
        self.AXIsolver.setDataType(0)
        self.runSolver()

    def showXEdata(self):
        '''Display the data in XY coordinates'''
        self.grid.clearScreen()
        self.AXIsolver.setDataType(1)
        self.runSolver()
        
    def runSolver(self):
        print("Running Solver for Initial conditions:")
        self.AXIsolver.setValues(self.init.getValues())
        self.AXIsolver.initSolver()
        self.AXIsolver.setPrinter(0)
        self.AXIsolver.runSolver()

    def __BuildScreen(self,parent):        
        frame = Frame(parent)
        self.__createAbout()
        self.__createColorPicker()
        self.__createMenu(frame,self)
        self.__createSolver(frame)
        self.__createEquations(frame)
        frame.pack(side='top')
        
if __name__ == '__main__':
    pgm = CFDexplorer()
    pgm.run()
        
