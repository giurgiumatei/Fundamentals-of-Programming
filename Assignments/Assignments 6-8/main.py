from Repository import *
from Domain import *
import UI
import Services

s=Services.Service(Student_Inventory(students),Assignment_Inventory(assignments),Grade_Inventory(grades))
u=UI.UI(s)



# fa n operatii din prima functionalitate generate random exemplu random 6--> 6 operatii gen add remove update

def main():#main module
    
    u.menu()







if __name__ == '__main__':#program starts here
    main()