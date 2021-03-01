from Classes import  Expense
import settings

def add():#this function adds a new expense to the list
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
    settings.expenses.append(EL)
    settings.hispenses.append(settings.expenses.copy())
    