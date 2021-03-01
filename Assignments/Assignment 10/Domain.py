from random import *
from texttable import Texttable
from copy import deepcopy

class Point:

    def __init__(self,i,j): #row-->i ;collumn-->j

        self.i=i
        self.j=j


    def get_i(self):
        return self.i
    
    def get_j(self):
        return self.j









class Board:
    def __init__(self,height,width):
        
        
        self.height=height
        self.width=width
        self.data=[]

        for i in range (self.height):
            self.data.append([0]*width)  #initialised the board 

        self.remaining_options=[]  #this list contains the remaining options of board space which can be occupied
        
        for i in range(self.height):
            for j in range(self.width):
                op=[i,j]
                self.remaining_options.append(op)
        print(self.remaining_options)


    def get_remaining_options(self):
        return self.remaining_options

    def set_remaining_options(self,newopt):
        self.remaining_options=newopt



  
    
    #information expert

    def isWon(self): #checks if there are remaining options, if not then game over
        
        if len(self.remaining_options) == 0:
            return True
        return False
        

   

    def move(self,x,y,symbol):
        # ensure x,y on board
        
        if x >self.height or x<0  or y >self.width or y<0:
            raise ValueError("Move outside board! ")
        #check if we do not override moves
        if self.data[x][y] !=0:
            raise ValueError("Invalid Square for Move !")
        if symbol not in ['X','O']:
            raise ValueError("Incorrect Symbol! ")
        
        d={'X':1,'O':'O'}
        self.data[x][y] = d[symbol]
        opt=[x,y]
        self.remaining_options.remove(opt)
        try:

            if x-1>=0 and y-1>=0:
                self.data[x-1][y-1]=-1
                opt=[x-1,y-1]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if x-1>=0:
                self.data[x-1][y]=-1
                opt=[x-1,y]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if x-1>=0 and y+1<=self.width:
                self.data[x-1][y+1]=-1
                opt=[x-1,y+1]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if y-1>=0:
                self.data[x][y-1]=-1
                opt=[x,y-1]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if y+1<=self.width:
                self.data[x][y+1]=-1
                opt=[x,y+1]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if x+1<=self.height and y-1>=0:
                self.data[x+1][y-1]=-1
                opt=[x+1,y-1]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if x+1<=self.height:
                self.data[x+1][y]=-1
                opt=[x+1,y]
                self.remaining_options.remove(opt)
        except:pass
        try:
            if x+1<=self.height and y+1<=self.width:
                self.data[x+1][y+1]=-1
                opt=[x+1,y+1]
                self.remaining_options.remove(opt)
        except:pass

        

    def __str__(self):
        t=Texttable()
        d={0:' ',1:'X',-1:'*','O':'O'}
        for i in range(self.height):
            row=self.data[i][:]
            for j in range(self.width):
                row[j]=d[row[j]]
            t.add_row(row)
        return t.draw()



class AI: #This AI uses "Omnia Temere" strategy
    
    def __init__(self,board):
        self.board=board
        


    def move(self):
        options=self.board.get_remaining_options()
        choice=randint(0,len(options)-1)
        m=deepcopy(options[choice])
        
        if m == -1:
            raise ValueError
        return m



class Game:

    def __init__(self,board,ai):
        self.board=board
        self.ai = ai
        

    def playerMove(self,x,y):
        self.board.move(x,y,'X')

    def computerMove(self):
        move=self.ai.move()
        self.board.move(move[0],move[1],'O')

    def getBoard(self):
        return self.board