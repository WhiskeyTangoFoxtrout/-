#this is a lexer, yup and some how its gonna connect to a window and a file system
#this is the skeleton of a parser had to borrow from the old acccount
#ima have to add this to an program where the user gives input to the comman console
class commands:
#remeber this is fixed
    
  
    def __init__(self,input):#this is more dynamic
        
        self.input = pac

class Posistion:

    def __init__(self,idx,ln,col,fn,ftxt):

        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt  = ftxt

    def adv(self, currentPos):

        self.idx += 1
        self.col += 1

        if currentPos == '\n':

            self.ln += 1 
            self.col = 0

        return self

    def copy(self):

        return Posistion(self.idx, self.ln, self.col,self.fn, self.ftxt)

#------------------------------------------- Tokens---------------------------------------------------

class Tokens:

    def __init__(self,type_,value=None):
        
        self.t

    def __init__(self,fn,text):
        
        self.fn = fn
        self.text = text
        self.pos = Posistion(-1,0,-1,fn,text)
        self.currentPos = None
        self.adv()

    def make_tokens(self):

        tokens =[]
        #wenever I figure the commands

#----------------------------------------Parser-----------------------------------------------------------------

class Parser:

    def __init__(self,tokens):

        self.tokens = tokens
        self.tok.idx = 1
        self.adv()

    def adv(self):

        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

#    def parse(self):
#        res - self.expr()
#        return res 


