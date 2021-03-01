from Classes import  Expense
import settings
import Req2

def filter():#this function removes the expenses lesser than a given value
    
    val=int(input("Give the value: "))
    n=len(settings.expenses)
    i=0
    while i<n:
        if val > int(settings.expenses[i].get_amount()):
               
            
            n-=1
            del settings.expenses[i]
           
            i-=1
        i+=1
           
           
            
    
   
    settings.hispenses.append(settings.expenses.copy())
        
