#--------------------------------------------------------------------
# File:     ColorList.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

import tkinter
import Pmw

class ColorScale:
    '''Manage a color scale for data plotting'''
    def __init__(self,numColors):
        self.correction  = 1.0
        self.saturation  = 1.0
        self.intensity   = 1.0
        self.extraOrange = 1
        self.colorList = Pmw.Color.spectrum(
                numColors,self.correction,self.saturation,
                self.intensity,self.extraOrange)

    def getColor(self,index):
        '''Return a color from the current list'''
        return self.colorList[index]

    def setColorList(self,numColors):
        self.colorList = Pmw.Color.spectrum(
                numColors,self.correction,self.saturation,
                self.intensity,self.extraOrange)

