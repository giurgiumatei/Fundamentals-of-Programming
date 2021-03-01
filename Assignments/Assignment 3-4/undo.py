from init import histudents
from init import students
import init

def undo(): # This function undos changes to the list until there are no more undos
    
    
    
    if len(init.histudents) == 1:
        print("No more undos")
    
    else:
        init.students.clear()
        
        init.histudents.pop()
        

    
        init.students=init.histudents[-1].copy()
        
    
    
    
    
    
    



