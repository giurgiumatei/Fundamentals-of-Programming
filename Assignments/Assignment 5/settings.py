#this module exists so that the list can be globally used
from Classes import Expense
import copy

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

def build():
    expenses.clear()

    n=int(input("Give the number of expenses: "))

    for i in range (n):
        print("Type in the day for the expense: ")
        while(True):
                try:
                    day=int(input())
                    assert 0<=day<=30 
                    break
                except:
                    print("Invalid Input")
    
        print("Type in the amount of money for the expense: ")
        while(True):
                try:
                    amount=int(input())
                    assert 0<=amount
                    break
                except:
                    print("Invalid Input")
   
        ttype=input("Type in the type of the expense: ")
        EL=Expense(day,amount,ttype)
        expenses.append(EL)
        hispenses.append(expenses.copy())






