#--------------------------------------------------------------------
# File:     Explorer.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from AXIsolver import *

class Explorer:

    def __init__(self):
        '''Set default explorer array'''
        self.x = []
        self.y = []
        self.data = []

    def setRadial(self,neta):
        '''Tell the explorer how many points radially'''
        self.neta = neta
        for i in range (neta):
            self.x += [ 0.0 ]
            self.y += [ eta ]
    def setOption(self,option):
        '''Tell the explorer that item to display'''
        self.option = option
        
    def setValue(self,j,value):
        '''set explorer data value for eta[j]'''
        self.data[j][option] = value

        # option set:
        #   'etax'
        #   'etar'
        #   'ueta
        #   'veta'
        #   'deldv'
        #   'txx'
        #   'sigxr'
        #   'trr'
        #   'sigpp'
        #   'e1'
        #   'e2'
        #   'e3'
        #   'f1'
        #   'f2'
        #   'f3'
