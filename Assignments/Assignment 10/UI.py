from Domain import *

class UI:
    def __init__(self,game):
        self.game=game
       


    def readPlayerMove(self):
        cmd=input("Your move: ").split(" ")
        if len(cmd)!=2:
            return -1
        return (int(cmd[0]),int (cmd[1]))
    def start(self):
        #program UI starts here
        b=self.game.getBoard()
        while True:
            try:
                opt=int(input("Press 1 if you want to start or 2 if you want the AI to start: "))
                if opt!=1 and opt!=2:
                    raise ValueError
                break
            except:print("Invalid Input! ")

        if opt==1:

            playerMove=True
        else:playerMove=False
        
        while b.isWon() == False:
           
            print(b)
            print(" ")
            
            if playerMove == True:

                while True:
                    try:
                        choice = self.readPlayerMove()
                        if choice==-1:
                            raise ValueError
                        self.game.playerMove(choice[0],choice[1])
                        playerMove=False
                        break
                    except:print("Invalid Coordinates! ")
            else:
                try:
                    self.game.computerMove()
                except:break
                playerMove=True

        
        print(b)    
        if playerMove != True:
            print("You Win!")
        else:
            print("Take the L!")


class size_UI:

    def size(self):

        while True:
            try:

                print("Give the size of the board")

                h=int(input("Give the number of rows: "))
                if h<1:
                    raise ValueError
                
                w=int(input("Give the number of columns: "))
                if w<1:
                    raise ValueError

                break
            except:print("Invalid Coordinates! ")

        sze=[h,w]

        return sze
           