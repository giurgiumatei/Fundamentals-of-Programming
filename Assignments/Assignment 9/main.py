from Repository import *
from Domain import *
import UI
import Services
from TextFIleRepo import *
import os
from PickleRepo import *






# fa n operatii din prima functionalitate generate random exemplu random 6--> 6 operatii gen add remove update

def main():#main module
    r=UI.repoUI()
    op=r.option()

    if op==1:
        s=Services.Service(Student_Inventory(students),Assignment_Inventory(assignments),Grade_Inventory(grades))
    elif op==2:
        s=Services.Service(Student_Inventory_Txt(),Assignment_Inventory_Txt(),Grade_Inventory_Txt())
    elif op==3:
        s=Services.Service(Student_Inventory_Pickle(students),Assignment_Inventory_Pickle(assignments),Grade_Inventory_Pickle(grades))


    u=UI.UI(s)
    u.menu()







if __name__ == '__main__':#program starts here
    main()