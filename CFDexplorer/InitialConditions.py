#--------------------------------------------------------------------
# File:     InitialConditions.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from tkinter import *
import Pmw

class InitialConditions:
    
    def __init__(self,parent):
        frame = Frame(parent)
        self.__initLabels(frame)
        self.__initEntry(frame)
        frame.pack(side='top')



    def RunSolver(self):
        '''Run the Solver'''
        print("Running Solver")
        
    def __initLabels(self,parent):
        frame=Frame(parent)
        Label(frame,text='Minf').pack(side='top',anchor=W)
        Label(frame,text='Tref').pack(side='top',anchor=W)
        Label(frame,text='REref').pack(side='top',anchor=W)
        Label(frame,text='MUref').pack(side='top',anchor=W)
        Label(frame,text='MUinf').pack(side='top',anchor=W)
        Label(frame,text='Thetas').pack(side='top',anchor=W)
        Label(frame,text='dxi').pack(side='top',anchor=W)
        Label(frame,text='Neta').pack(side='top',anchor=W)
        Label(frame,text='Nitmax').pack(side='top',anchor=W)
        Label(frame,text='Nplot').pack(side='top',anchor=W)
        Label(frame,text='Dplot').pack(side='top',anchor=W)
        frame.pack(side='left')        

    def __initEntry(self,parent):
        frame=Frame(parent)
        self.minf=Pmw.EntryField(frame, value='5.95')
        self.minf.pack(side='top')
        self.tref=Pmw.EntryField(frame, value='1464.7157')
        self.tref.pack(side='top')
        self.reref=Pmw.EntryField(frame, value='2179168')
        self.reref.pack(side='top')
        self.muref=Pmw.EntryField(frame, value='7.65034e-7')
        self.muref.pack(side='top')
        self.muinf=Pmw.EntryField(frame, value='0.00002')
        self.muinf.pack(side='top')
        self.thetas=Pmw.EntryField(frame, value='22.0')
        self.thetas.pack(side='top')
        self.dxi=Pmw.EntryField(frame, value='0.0004')
        self.dxi.pack(side='top')
        self.neta=Pmw.EntryField(frame, value='31')
        self.neta.pack(side='top')
        self.nitmax=Pmw.EntryField(frame, value='750')
        self.nitmax.pack(side='top')
        self.nplot=Pmw.EntryField(frame, value='25')
        self.nplot.pack(side='top')
        self.dplot=Pmw.EntryField(frame, value='0.05')
        self.dplot.pack(side='top')
        frame.pack(side='left')        

    def getValues(self):
        v = {}
        v['minf']   = float(self.minf.get())
        v['tref']   = float(self.tref.get())
        v['reref']  = float(self.reref.get())
        v['muref']  = float(self.muref.get())
        v['muinf']  = float(self.muinf.get())
        v['thetas'] = float(self.thetas.get())
        v['dxi']    = float(self.dxi.get())
        v['neta']   = int(self.neta.get())
        v['nitmax'] = int(self.nitmax.get())
        v['nplot']  = int(self.nplot.get())
        v['dplot']  = float(self.dplot.get())
        return v
        
if __name__ == "__main__":
    root=Tk();
    init = InitialConditions(root)
    root.mainloop()
    
