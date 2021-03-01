from Domain import *
from UI import *



def start_program():
    s=size_UI()
    sze=s.size()
    b=Board(sze[0],sze[1])
    
    ai=AI(b)
    g=Game(b,ai)
    ui=UI(g)
    ui.start()







if __name__ == "__main__":
    start_program()