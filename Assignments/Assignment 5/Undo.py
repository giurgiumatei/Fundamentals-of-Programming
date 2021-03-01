from Classes import  Expense
import settings
from settings import expenses
from settings import hispenses


def undo(): # This function undos changes to the list until there are no more undos
    
    
    
    if len(settings.hispenses) == 1:
        print("No more undos")
    
    else:
        settings.expenses.clear()
        
        settings.hispenses.pop()
        

    
        settings.expenses=settings.hispenses[-1].copy()
        
    