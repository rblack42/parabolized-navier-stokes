#--------------------------------------------------------------------
# File:     XUIbuilder.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from xml.sax import parse, SAXParseException, ContentHandler
from XUIobjects import *

class XUIbuilder( ContentHandler ):
    """XUI Window Builder"""

    
    def __init__( self, tagName ):
        """Initialize ContentHandler and set tag to search for"""
        ContentHandler.__init__( self )
        self.objects = XUIobjects()
        self.tagName = tagName
        self.depth = 0

    def startElement( self, name, attributes ):
        """An element has started"""
        print "\n%s<%s> started" % ( " " * self.depth, name )
        self.depth += 3

        if name == "window":
            width = attributes.getValue( "width" )
            height = attributes.getValue( "height" )
            self.objects.startWindow(width,height)
            
        if name == "menubar":
            self.objects.startMenuBar()

        if name == "cascademenu":
            oname = attributes.getValue( "name" )
            underline = attributes.getValue( "underline" )
            self.objects.startCascadeMenu( oname,underline )
            
        if name == "cascadeitem":
            oname = attributes.getValue( "name" )
            underline = attributes.getValue( "underline" )
            self.objects.startCascadeItem( oname,underline )
            
        if name == "cascadesep":
            self.objects.startCascadeSep()
            
        if name == "frame":
            oname = attributes.getValue( "name" )
            oside = attributes.getValue( "side" )
            ofill = attributes.getValue( "fill" )
            self.objects.startFrame( oname,oside,ofill )
            
        if name == "listbox":
            oname = attributes.getValue( "name" )
            oside = attributes.getValue( "side" )
            ofill = attributes.getValue( "fill" )
            self.objects.startListBox( oname,oside,ofill )
            
        if name == "textbox":
            oname = attributes.getValue( "name" )
            oside = attributes.getValue( "side" )
            ofill = attributes.getValue( "fill" )
            self.objects.startTextBox( oname,oside,ofill )

        for attribute in attributes.getNames():
            print "%s%s = %s" % ( " " * self.depth, attribute,
                attributes.getValue( attribute ) )
            
    def endElement( self,name ):
        self.depth -= 3
        print "%s</%s> ended\n" % ( " " * self.depth, name )
        if name == "window":
            self.objects.endWindow()

def main():
    file = "window.xml"
    tagName = "window"
    try:
        parse( file, XUIbuilder( tagName ) )
    except IOError, message:
        print "Error reading file:", message
    except SAXParseException, message:
        print "Error parsing file:", message

if __name__ == "__main__":
    main()
