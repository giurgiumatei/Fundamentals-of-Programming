from Domain import *
from Repository import *
from Services import *
from UI import *



s=service(persons_repo())

def main(): 


    s=service(persons_repo())
    ui=UI(s)
    ui.start()










main()