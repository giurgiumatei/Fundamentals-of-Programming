from Domain import *
from Services import *
from Repository import *
from UI import *


s=Service(bus_repo(),buss_routes_repo())


def main():
    
    ui=UI(s)
    ui.start()




main()