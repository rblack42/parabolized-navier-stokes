#--------------------------------------------------------------------
# File:     EQNexplorer.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from tkinter import *
from PIL import Image,ImageTk
from Explorer import *

class EQNexplorer:

    def __init__(self,parent,solver):
        '''display the equation explorer buttons'''
        self.explorer = Explorer()
        self.solver = solver
        frame=Frame(parent)

        # load the images        
        self.e1xi  = ImageTk.PhotoImage(Image.open('EQNimages/E1xi.jpeg'))
        self.e2xi  = ImageTk.PhotoImage(Image.open('EQNimages/E2xi.jpeg'))
        self.e3xi  = ImageTk.PhotoImage(Image.open('EQNimages/E3xi.jpeg'))
        self.e1eta  = ImageTk.PhotoImage(Image.open('EQNimages/E1eta.jpeg'))
        self.e2eta  = ImageTk.PhotoImage(Image.open('EQNimages/E2eta.jpeg'))
        self.e3eta  = ImageTk.PhotoImage(Image.open('EQNimages/E3eta.jpeg'))
        self.f1eta  = ImageTk.PhotoImage(Image.open('EQNimages/F1eta.jpeg'))
        self.f2eta  = ImageTk.PhotoImage(Image.open('EQNimages/F2eta.jpeg'))
        self.f3eta  = ImageTk.PhotoImage(Image.open('EQNimages/F3eta.jpeg'))
        self.etax   = ImageTk.PhotoImage(Image.open('EQNimages/etax.jpeg'))
        self.etar   = ImageTk.PhotoImage(Image.open('EQNimages/etar.jpeg'))
        self.tauxx  = ImageTk.PhotoImage(Image.open('EQNimages/tauxx.jpeg'))
        self.tauxr  = ImageTk.PhotoImage(Image.open('EQNimages/tauxr.jpeg'))
        self.taurr  = ImageTk.PhotoImage(Image.open('EQNimages/taurr.jpeg'))
        self.taupp  = ImageTk.PhotoImage(Image.open('EQNimages/taupp.jpeg'))
        self.deldv  = ImageTk.PhotoImage(Image.open('EQNimages/deldv.jpeg'))
        self.tmuetar= ImageTk.PhotoImage(Image.open('EQNimages/tmuetar.jpeg'))
        self.tmuetax= ImageTk.PhotoImage(Image.open('EQNimages/tmuetax.jpeg'))
        self.ttmu   = ImageTk.PhotoImage(Image.open('EQNimages/ttmu.jpeg'))
        self.ueta   = ImageTk.PhotoImage(Image.open('EQNimages/ueta.jpeg'))
        self.veta   = ImageTk.PhotoImage(Image.open('EQNimages/veta.jpeg'))
        self.mu     = ImageTk.PhotoImage(Image.open('EQNimages/mu.jpeg'))
        
        # continuity equation
        f1 = Frame(frame)
        Label(f1, text='Continuity',width=20).pack(side='left')
        EQ1    = Frame(f1)
        Button(EQ1,image=self.e1xi,command=self.plotE1xi).pack(side='left')
        Label(EQ1,text='+').pack(side=LEFT)
        Label(EQ1,image=self.etax).pack(side=LEFT)
        Button(EQ1,image=self.e1eta,command=self.plotE1eta).pack(side=LEFT)
        Label(EQ1,text='+').pack(side=LEFT)
        Label(EQ1,image=self.etar).pack(side=LEFT)
        Button(EQ1,image=self.f1eta,command=self.plotF1eta).pack(side=LEFT)
        EQ1.pack(side='right')
        f1.pack(side='top',anchor='w')

        f2 = Frame(frame)
        Label(f2, text='X Momentum',width=20).pack(side='left')
        EQ2    = Frame(f2)
        Button(EQ2,image=self.e2xi,command=self.plotE2xi).pack(side=LEFT)
        Label(EQ2,text='+').pack(side=LEFT)
        Label(EQ2,image=self.etax).pack(side=LEFT)
        Button(EQ2,image=self.e2eta,command=self.plotE2eta).pack(side=LEFT)
        Label(EQ2,text='+').pack(side=LEFT)
        Label(EQ2,image=self.etar).pack(side=LEFT)
        Button(EQ2,image=self.f2eta,command=self.plotF2eta).pack(side=LEFT)
        EQ2.pack(side='top')
        f2.pack(side='top',anchor='w')
        
        f3 = Frame(frame)
        Label(f3, text='R Momentum',width=20).pack(side='left')
        EQ3    = Frame(f3)
        Button(EQ3,image=self.e3xi,command=self.plotE3xi).pack(side=LEFT)
        Label(EQ3,text='+').pack(side=LEFT)
        Button(EQ3,image=self.e3eta,command=self.plotE3eta).pack(side=LEFT)
        Label(EQ3,text='+').pack(side=LEFT)
        Label(EQ3,image=self.etax).pack(side=LEFT)
        Button(EQ3,image=self.e3eta,command=self.plotE3eta).pack(side=LEFT)
        Label(EQ3,text='+').pack(side=LEFT)
        Label(EQ3,image=self.etar).pack(side=LEFT)
        Button(EQ3,image=self.f3eta,command=self.plotE3eta).pack(side=LEFT)
        EQ3.pack(side='top')
        f3.pack(side='top',anchor='w')
        
        # shear stress terms
        f4 = Frame(frame)
        Label(f4, text='Shear Stress',width=20).pack(side='left')
        EQ4 = Frame(f4)
        Button(EQ4,image=self.tauxx,command=self.plotTauxx).pack(side=LEFT)
        Label(EQ4,text='=').pack(side=LEFT)
        Label(EQ4,image=self.tmuetax).pack(side=LEFT)
        Button(EQ4,image=self.ueta,command=self.plotUeta).pack(side=LEFT)
        Label(EQ4,text='-').pack(side=LEFT)
        Label(EQ4,image=self.ttmu).pack(side=LEFT)
        Button(EQ4,image=self.deldv,command=self.plotDeldv).pack(side=LEFT)
        EQ4.pack(side='left')
        f4.pack(side='top',anchor='w')
        
        f5 = Frame(frame)
        Label(f5, text=' ',width=20).pack(side='left')
        EQ5 = Frame(f5)
        Button(EQ5,image=self.tauxr,command=self.plotTauxr).pack(side=LEFT)
        Label(EQ5,text='=').pack(side=LEFT)
        Label(EQ5,image=self.mu).pack(side=LEFT)
        Label(EQ5,text='(').pack(side=LEFT)
        Label(EQ5,image=self.etax).pack(side=LEFT)
        Button(EQ5,image=self.veta,command=self.plotVeta).pack(side=LEFT)
        Label(EQ5,text='+').pack(side=LEFT)
        Label(EQ5,image=self.etar).pack(side=LEFT)
        Button(EQ5,image=self.ueta,command=self.plotUeta).pack(side=LEFT)
        Label(EQ5,text=')').pack(side=LEFT)
        EQ5.pack(side='left')
        f5.pack(side='top',anchor='w')
        
        f6 = Frame(frame)
        Label(f6, text=' ',width=20).pack(side='left')
        EQ6 = Frame(f6)
        Button(EQ6,image=self.taurr,command=self.plotTaurr).pack(side=LEFT)
        Label(EQ6,text='=').pack(side=LEFT)
        Label(EQ6,image=self.tmuetar).pack(side=LEFT)
        Button(EQ6,image=self.veta,command=self.plotVeta).pack(side=LEFT)
        Label(EQ6,text='-').pack(side=LEFT)
        Label(EQ6,image=self.ttmu).pack(side=LEFT)
        Button(EQ6,image=self.deldv,command=self.plotDeldv).pack(side=LEFT)
        EQ6.pack(side='left')
        f6.pack(side='top',anchor='w')
        
        f7 = Frame(frame)
        Label(f7, text=' ',width=20).pack(side='left')
        EQ7 = Frame(f7)
        Button(EQ7,image=self.taupp,command=self.plotTaupp).pack(side=LEFT)
        Label(EQ7,text='=').pack(side=LEFT)
        Label(EQ7,image=self.tmuetax).pack(side=LEFT)
        Button(EQ7,image=self.ueta,command=self.plotUeta).pack(side=LEFT)
        Label(EQ7,text='-').pack(side=LEFT)
        Label(EQ7,image=self.ttmu).pack(side=LEFT)
        Button(EQ7,image=self.deldv,command=self.plotDeldv).pack(side=LEFT)
        EQ7.pack(side='left')
        f7.pack(side='top',anchor='w')
        
        f8 = Frame(frame)
        Label(f8, text=' ',width=20).pack(side='left')
        EQ8 = Frame(f8)
        Button(EQ8,image=self.deldv,command=self.plotDeldv).pack(side=LEFT)
        Label(EQ8,text='=').pack(side=LEFT)
        Label(EQ8,image=self.etax).pack(side=LEFT)
        Button(EQ8,image=self.ueta,command=self.plotUeta).pack(side=LEFT)
        Label(EQ8,text='+').pack(side=LEFT)
        Label(EQ8,image=self.etar).pack(side=LEFT)
        Button(EQ8,image=self.veta,command=self.plotVeta).pack(side=LEFT)
        Label(EQ8,text='+').pack(side=LEFT)
        Label(EQ8,text='vr').pack(side=LEFT)
        EQ8.pack(side='left')
        f8.pack(side='top',anchor='w')
        
        # now pack the frames 
        frame.pack(side='top')

    def plotE1xi(self):
        print("plotting E1xi\n")
        self.solver.setExplorer(1)
        pass

    def plotE2xi(self):
        print("plotting E2xi\n")
        self.solver.setExplorer(2)
        pass

    def plotE3xi(self):
        print("plotting E3xi\n")
        self.solver.setExplorer(3)

    def plotE1eta(self):
        print("plotting E1eta\n")
        self.solver.setExplorer(4)

    def plotE2eta(self):
        print("plotting E2eta\n")
        self.solver.setExplorer(5)

    def plotE3eta(self):
        print("plotting E2eta\n")
        self.solver.setExplorer(6)

    def plotF1eta(self):
        print("plotting F1eta\n")
        self.solver.setExplorer(7)

    def plotF2eta(self):
        print("plotting F2eta\n")
        self.solver.setExplorer(8)

    def plotF3eta(self):
        print("plotting F3eta\n")
        self.solver.setExplorer(9)

    def plotTauxx(self):
        print("plotting Tauxx\n")
        self.solver.setExplorer(10)

    def plotTauxr(self):
        print("plotting Tauxr\n")
        self.solver.setExplorer(11)

    def plotTaurr(self):
        print("plotting Taurr\n")
        self.solver.setExplorer(12)

    def plotTaupp(self):
        print("plotting Taupp\n")
        self.solver.setExplorer(13)

    def plotDeldv(self):
        print("plotting Deldv\n")
        self.solver.setExplorer(14)
   
    def plotUeta(self):
        print("plotting Ueta\n")
        self.solver.setExplorer(15)

    def plotVeta(self):
        print("plotting Veta\n")
        self.solver.setExplorer(16)

if __name__ == "__main__":
    root=Tk();
    init = EQNexplorer(root,None)
    root.mainloop()

