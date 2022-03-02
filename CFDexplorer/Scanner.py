#--------------------------------------------------------------------
# File:     Scanner.py
#
# Author:   Roie R. Black
# Date:     Dec 9, 2003
# Course:   CS 5335
#--------------------------------------------------------------------

class Scanner:

    def __init__(self,lines):
        'Scanner Constructor - initializes token classes'
        self.tokens = []

        # initialize symbol classes
        symbols = [ 'beginmath', 'endmath', 'lparen', 'rparen',
            'equals',
            'superscript', 'subscript', 'comma', 'backslash',
            'mathbegin', 'mathend', 'begingroup', 'endgroup',
            'ident', 'other', 'endfile' ]
        symclass   = {}
        j = 0
        for i in symbols:
            symclass[i] = j
            j += 1
        self.symclass = symclass

        #initialize token classes
        tokclass = {}
        tokclass['{'] = symclass['begingroup']
        tokclass['}'] = symclass['endgroup']
        tokclass['('] = symclass['lparen']
        tokclass[')'] = symclass['rparen']
        tokclass['^'] = symclass['superscript']
        tokclass['_'] = symclass['subscript']
        tokclass[','] = symclass['comma']
        tokclass['='] = symclass['equals']
        tokclass['\\'] = symclass['backslash']
        tokclass['\0'] = symclass['endfile']
        self.tokclass = tokclass

        # initialize scanning variables
        self.lcount = len(lines)
        self.lines = lines
        self.lpos = 0
        self.cpos = 0
        self.line = lines[0]
        self.linelen = len(self.line)
        self.symbol = ''
        self.code = symclass['other']

    def getChar(self):
        'return the next character from input or eof'
        # end of current line?
        if self.cpos >= self.linelen:
            self.lpos = self.lpos + 1
            if self.lpos >= self.lcount:
                return '\0'
            self.line = self.lines[self.lpos]
            self.linelen = len(self.line)
            self.cpos = 0
        c = self.line[self.cpos]
        self.cpos += 1
        return c

    def pushback(self):
        'push back one character'
        self.cpos = self.cpos -1

    def getSymbol(self):
        'scan input set next symbol and code'
        ch = self.getChar()
        # skip white space up to endfile
        while ch.isspace():
            ch = self.getChar()
        if ch == '\0':
            self.code = self.symclass['endfile']
            return

        # see if we have an identifier
        token = ''
        if ch.isalpha():
            while ch.isalpha() or ch.isdigit():
                token += ch
                ch = self.getChar()
            self.pushback()
            self.code = self.symclass['ident']
            self.symbol = token
            return
        elif ch == '\\':
            tch = self.getChar()
            if tch == '[':
                self.code = self.symclass['mathbegin']
                self.symbol = '\\['
                return
            elif tch == ']':
                self.code = self.symclass['mathend']
                self.symbol = '\\]'
                return
            else:
                self.pushback()
        token += ch
        if self.tokclass.has_key(ch):
            self.code = self.tokclass[ch]
        else:
            self.code = self.symclass['other']
        self.symbol = token

#--------------------------------------------------------------------
# For stand-alone testing

def main():
    lines = [ "{ \ \[ \]  this_is_0 a identifier \class  & }" ]
        
    tex = Scanner(lines)
    tex.getSymbol()
    while tex.code != tex.symclass['endfile']:
        print "Token(%2d) %s" % (tex.code,tex.symbol)
        tex.getSymbol()
        
if __name__ == "__main__":
    main()

