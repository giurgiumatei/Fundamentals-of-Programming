# this module contains the classes used
import copy

class Expense: #class for the expenses
    def __init__(self, day, amount, ttype):
        self.amount=int(amount)
        self.day=int(day)
        self.ttype=ttype
    
    def set_amount(self,am):

        self.amount=am

    def set_day(self,d):
        self.day=d
    
    def set_type(self,t):
        self.ttype=t
    
    def get_amount(self):
        return self.amount
    
    def get_day(self):
        return self.day
    
    def get_type(self):
        return self.ttype

class UI: #UI class

    

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

    

    hispenses=[] #this is whe the list history is stored for the UNDO funcionality

    hispenses.append(hispenses1.copy())

    def build(self): # this function reads the list of expenses from the user
        UI.expenses.clear()

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
            UI.expenses.append(EL)
            UI.hispenses.append(UI.expenses.copy())




    def menu(self):# this function manages the list until the user types 0

        p=Service()
        
        while(True):
            while True:
            
                try:
                    option=input("Give the number corresponding to the requirement: ")
                    assert str(option) == "Undo" or int(option) >= 0 and int(option) < 4 
                    break
                except: 
                    print("Invalid input")
            
            
            if str(option) == "Undo":
                p.undo()
            elif int(option)==1:
                p.imput_add()
            elif int(option)==2:
                
                p.list()
            elif int(option)==3:
                p.filter()
            elif int(option)==0:
                break

class Service: # service class

   
   
   
    def add(self,elem):#this function adds a new expense to the list
        
        UI.expenses.append(elem)
        UI.hispenses.append(UI.expenses.copy())
   
   
   
   
   
    def imput_add(self): #this function reads a new expense to be added
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
        self.add(EL)






    def list(self):#this function displays the expenses
    
        for i in range (len(UI.expenses)):
            print("Day: " + str(UI.expenses[i].get_day()) + " Amount: " + str(UI.expenses[i].get_amount()) + " Type: " + str(UI.expenses[i].get_type()))


    def filter(self):#this function removes the expenses lesser than a given value
    
        val=int(input("Give the value: "))
        n=len(UI.expenses)
        i=0
        while i<n:
            if val > int(UI.expenses[i].get_amount()):
                
                
                n-=1
                del UI.expenses[i]
            
                i-=1
            i+=1
            
            
                
        
    
        UI.hispenses.append(UI.expenses.copy())

    def undo(self): # This function undos changes to the list until there are no more undos
        
        
        
        if len(UI.hispenses) == 1:
            print("No more undos")
        
        else:
            UI.expenses.clear()
            
            UI.hispenses.pop()
            

        
            UI.expenses=UI.hispenses[-1].copy()


    




    






