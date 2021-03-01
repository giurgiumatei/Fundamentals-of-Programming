from Domain import *
from Service import *
from Repository import *
from UI import *




def main():

    s=service(songs_repo())
    ui=UI(s)

    ui.start()






main()