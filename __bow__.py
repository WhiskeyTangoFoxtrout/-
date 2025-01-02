#dis da kern gone try and make a fuction that can open a userfriendlyKernal(O.S)
#kern kicks in where its more bit and m.c then python so when u need to look at the threadcount
#this is made for a 24inch comp moniter. Idk how to autosize it yet
import curses

class Bow:

    
    def __init__(self,name,Nput):

        self.nput = getstr(1915,9)
        self.name = title
        
    def bootuProcess(self,window):

        wdow = curses.initscr(1920,1000)#Wdow.newwin()
        curses.nobreak()
        curses.echo()
        curses.nocbreak()#not in the kernal
        curses.beep('5s')
        curses.flash()
        curses.def_shell()
        curses.napms(500)
    
    def frame(self):
        
        self.Frame = wdow.border(0,0,40,0,0,0,0,0)#think this put a line at da 40 pixels
        self.mousePos = wdow.move(1915,3)
        self.runna = wdow.doupdate()
        wdow.addstr(950,500,"Welcome to The O.S")
        

