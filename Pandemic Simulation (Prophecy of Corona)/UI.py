from Services import *


class UI:

    def __init__(self,service):
        self.service=service


    def print_menu(self):
        print("1.Simulate; ")
        print("2.Display Persons; ")
        print("3.Vaccinate a person. ")

    def start(self):


        while True:

            self.print_menu()

            opt=int(input())

            if opt==0:
                break
            elif opt==1:
                self.simulate()

            elif opt==2:
                self.display()
            elif opt==3:
                self.vaccinate()

    def simulate(self):
        
        if self.service.infect()==0:
            print("Every1 is healthy ")
        self.service.simulate()

        

        

    def display(self):
        persons=self.service.get_persons()

        for p in persons:
            print(str(p.get_id())+ ' '+str(p.get_immune_status())+' ' + str(p.get_status()))

    def vaccinate(self):

        p_id=input("Give the id of the person you want to vaccinate")

        if self.service.vaccinate(p_id) == 0:
            print("Person is ill!")

    