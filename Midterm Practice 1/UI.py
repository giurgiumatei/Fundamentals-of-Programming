from Services import *

from Domain import *
class UI:

    def __init__(self,service):

        self.service=service

    
    def print_menu(self):

        print("1.Display all busses by a certain route; ")
        print("2.Display all bus routes; ")
        print("3.Compute how many km's the bus has travelled.")

    def start(self):
        
        
        

        while True:
            self.print_menu()

            opt=int(input())

            if opt==0:
                break
            elif opt==1:
                self.display_busses()
            elif opt==2:
                self.display_routes()

            elif opt==3:
                self.compute()



    def display_busses(self):
        route=input("Give the route")

        busses=self.service.display_busses(route)

        for b in busses:
            print(str(b.get_id())+' ' +str(b.get_rcode())+ ' '+str(b.get_model())+' '+str(b.get_times()))

    def display_routes(self):
        rts=self.service.routes()

        for r in rts:
            print("Route "+str(r.get_rcode()))

    def compute(self):
        b_id=input("Give the buss ID")
        busses=self.service.display_busses2()

        for b in busses:
            if b_id==b.get_id():
                t=b.get_times()
                r=b.get_rcode()
                break

        routes=self.service.routes()

        for route in routes:
            if r==route.get_rcode():
                l=route.get_lenght()
                break

        
        print (self.service.calculate(int(l),int(t)))




        