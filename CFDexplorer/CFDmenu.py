#--------------------------------------------------------------------
# File:     CFDmenu.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from tkinter import *
import Pmw

class CFDmenu:

    def __init__(self,parent,program):
        self.parent = parent
        self.program = program
        frame = Frame(parent)
        menuBar=Pmw.MenuBar(frame,
                hull_relief='raised',
                hull_borderwidth = 1)
        menuBar.pack(side='left',fill='x',expand=1)
        menuBar.addmenu('File', 'Manage files or exit')
        menuBar.addmenuitem('File', 'command', 'Open file',
            command = PrintOne('Action: open'),
            label = 'Open')
        menuBar.addmenuitem('File', 'command', 'Save file',
            command = PrintOne('Action: open'),
            label = 'Save')
        menuBar.addmenuitem('File', 'separator')
        menuBar.addmenuitem('File', 'command', 'Exit program',
            command = self.program.quit,
            label = 'Save-Exit')
        menuBar.addmenuitem('File', 'command', 'Save and Exit program',
            command = self.program.quit,
            label = 'Exit')
        menuBar.addmenu('Edit', 'Cut, copy or paste')
        menuBar.addmenuitem('Edit', 'command', 'Edit Colors for display',
            command = self.program.showPicker,
            label = 'Colors')


        menuBar.addmenu('Help', 'User manuals', side = 'right')
        menuBar.addmenuitem('Help', 'command', 'About this application',
            command = self.program.showAbout,
            label = 'About...')
                
        frame.pack(side='top',fill='x',expand=1)

class PrintOne:
    def __init__(self, text):
        self.text = text

    def __call__(self):
        print(self.text)

if __name__ == '__main__':
    root = Tk()
    menu = CFDmenu(root)
    root.mainloop()
