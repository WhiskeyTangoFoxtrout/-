#this is a lexer, yup and some how its gonna connect to a window and a file system

class commands:
#remeber this is fixed
    
  
    def __init__(self,input):#this is more dynamic
        
        self.input = pac

class Lexer:

    def __init__(self,fn,text):

        self.fn = fn
        self.text = text
        self.pos = Posistion(-1,0,-1)

    def adv(self):
        self.pos.adv(self.currentPos)
        self.currentPos = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

class Posistion:

    def __init__(self,ln,col,idx,text):

        self.ln = ln
        self.col = col 
        self.idx = idx
        self.Pm = pm
        self.pos = {} #think i got call it commands.cursor.pos()...I think
        
        ln = 1
        col = 0

        self.pos{ln,col}#I think this is valid

    def adv(self,currentPos):
        self.col +=1
        self.idx +=1

        if currentPos == '\n':
            self.ln += 1
            self.col += 0

        return self

    def copy(self):
        return Posistion(self.idx,self.ln,self.col,self.idx)
