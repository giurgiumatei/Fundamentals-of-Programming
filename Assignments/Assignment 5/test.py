import Classes
from Classes import Expense
from Classes import Service

#this is just the test module, where the first functionality according to the requirement is tested

def test_add():
   

    elem=Expense(1,2,3)

    Service().add(elem)

    assert Classes.UI.expenses[-1]==elem


test_add()