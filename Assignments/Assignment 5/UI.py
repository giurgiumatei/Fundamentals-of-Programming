from Classes import Expense
import settings
import Req1
import Req2
import Req3
import Undo

#this is the UI module


class UI:
    global expenses


    E1=Expense(1,10,"ham")

    E2=Expense(2,20,"cigars")

    E3=Expense(3,30,"Pepsi Twist")

    E4=Expense(4,40,"toothpaste")

    E5=Expense(5,50,"chocolate")

    E6=Expense(6,60,"dentist")

    E7=Expense(7,70,"subscriptions")

    E8=Expense(8,80,"FIFA packs")

    E9=Expense(9,90,"tendies")

    E10=Expense(10,100,"cigars")

    expenses=[E1,E2,E3,E4,E5,E6,E7,E8,E9,E10] #predefined list

    hispenses1=copy.deepcopy(expenses)

    global hispenses

    hispenses=[]

    hispenses.append(hispenses1.copy())




    def menu():# this function manages the list until the user types 0
        while(True):
            while True:
            
                try:
                    option=input("Give the number corresponding to the requirement: ")
                    assert str(option) == "Undo" or int(option) >= 0 and int(option) < 4 
                    break
                except: 
                    print("Invalid input")
            
            
            if str(option) == "Undo":
                Undo.undo()
            elif int(option)==1:
                Req1.add()
            elif int(option)==2:
                
                Req2.list()
            elif int(option)==3:
                Req3.filter()
            elif int(option)==0:
                break
