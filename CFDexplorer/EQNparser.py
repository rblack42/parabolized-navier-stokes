#--------------------------------------------------------------------
# File:     EQNparser.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

from Scanner import *

class Parser:

    def __init__(self,file):
        try:
            texfile = open(file)
        except IOError:
            print "Can't open input file: %s" % file
            sys.exit()
        lines = texfile.readlines()
        self.scanner = Scanner(lines)
        
#--------------------------------------------------------------------

    def Pname(self):
        print "Pname:",
        symbol = ''
        lines = []
        code = self.scanner.code

        # see if we have a simple ident
        if code == self.scanner.symclass['ident']:
            symbol += self.scanner.symbol
            print symbol
            self.scanner.getSymbol()
            return

        # check for a TeX command
        elif code == self.scanner.symclass['backslash']:
            symbol += self.scanner.symbol
            code = self.scanner(lines)
            if code == self.scanner.classes["IDENT"]:
                symbol += self.scanner.token
                print symbol
                self.scanner.getSymbol()
                return
            
        # if we get here with no symbol, error
        if symbol == '':
            print "Parse Error on line %d cpos %d" % \
                ( self.scanner.lpos, self.scanner.lpos )
            sys.exit()
    
    def match(self, nextCode):
        symbol = ''
        code = self.scanner.tokencode
        if code != nextCode:
            print "Parse Error on line %d cpos %d" % \
                ( self.scanner.lpos, self.scanner.cpos )
            sys.exit()
        print "match:",
        print self.scanner.token
        self.scanner.getSymbol()
    
    def Pexpr(self):
        print "Pexpr - start"
        while self.scanner.tokencode != self.scanner.classes["EQEND"]:
            print "EXPR %s %d" % (self.scanner.token,self.scanner.cpos)
            self.scanner.getSymbol()
        print "Pexpr - end"

    def Pequation(self):
        print "Pequation - start"
        
        self.match(self.scanner.classes["EQSTART"])
        
        if self.scanner.tokencode == self.scanner.classes["BEGINGROUP"]:
            print "BeginGroup"
            self.scanner.getSymbol()
            self.Pname()
            self.match(self.scanner.classes["ENDGROUP"])
            print "EndGroup"
        else:
            self.Pname()
        self.match(self.scanner.classes["EQUALS"])
        print "EQN - equals"
        self.Pexpr()
        print "PEquation - end"
            
    def parse(self):
        self.scanner.getSymbol()
        while self.scanner.code != self.scanner.symclass['endfile']:
            self.Pequation()
            
#--------------------------------------------------------------------
# For stand-alone testing

def main():
    file = "coord.eqn"
    parser = Parser(file)
    parser.parse()
        
if __name__ == "__main__":
    main()

#   eqn     ::= lhs '=' rhs;
#   lhs     ::= ident | group
#   group   ::= '{' name '}'
#   name    ::= ident ( superscript | subscript )*
#   ident   ::= IDENT | '\' IDENT
#   rhs     ::= expr
#   expr    ::= expr addop term
#   expr    ::= term
#   term    ::= term mulop factor
#   term    ::= factor
#   factor  ::= lhs
#   factor  ::= '(' expr ')'


