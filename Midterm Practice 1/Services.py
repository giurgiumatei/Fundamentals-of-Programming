from Repository import *
from Domain import *

class Service:

    def __init__(self,bus_repo,routes_repo):
        self.bus_repo=bus_repo
        self.routes_repo=routes_repo

    def display_busses(self,route):

        busses=self.bus_repo.get_busses()
        d_busses=[]

        for b in busses:
            if b.get_rcode()==route:
                d_busses.append(b)

        return d_busses

    def routes(self):
        return self.routes_repo.get_routes()

    def display_busses2(self):

        busses=self.bus_repo.get_busses()
        

        return busses

    def calculate(self,par1,par2):
        return par1*par2