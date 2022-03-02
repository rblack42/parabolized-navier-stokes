#--------------------------------------------------------------------
# File:     XUIobjects.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2004
# Course:   CS 5335
#--------------------------------------------------------------------

import sys

class XUIobjects:

    def __init__( self ):
        print "XUIobjects initialized"

    def startWindow( self, width, height ):
        print "Start Window \"%sx%s\"" % (width,height)
        try:
            self.outFile = open("CFDwindow.py", "w")
        except IOError:
            print "Error opening CDF window file"
            sys.exit()
        print >> self.outFile, """# File: CFDexplorer.py
import Tkinter

top = Tkinter.Tk()
top.title( "CFDexplorer v0.6" )
"""        

        print >> self.outFile, \
                "top.geometry(\"%sx%s\")" % \
                ( width, height )
        self.parent = "top"

    def startMenuBar( self, name ):
        print >> self.outFile, "%s.config( -menu addmenu( \"%s\", \"%s\")" % self.parent

    def startCascadeMenu( self,name,underline ):
        print "Start CascadeMenu %s %s" % ( name,underline )

    def startCascadeItem( self,name,underline ):
        print "Start CascadeItem %s %s" % ( name,underline )

    def startCascadeSep( self ):
        print "Start CascadeSep"

    def startFrame( self,name,side,fill ):
        print "Start Frame %s %s %s" % ( name,side,fill )

    def startListBox( self,name,side,fill ):
        print "Start List Box %s %s %s" % ( name,side,fill )

    def startTextBox( self,name,side,fill ):
        print "Start Text Box %s %s %s" % ( name,side,fill )

    def endWindow( self ):
        print >> self.outFile, """
top.mainloop()
"""    
        self.outFile.close()


