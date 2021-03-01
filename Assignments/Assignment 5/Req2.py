from Classes import  Expense
import settings

def list():#this function displays the expenses
    
    for i in range (len(settings.expenses)):
        print("Day: " + str(settings.expenses[i].get_day()) + " Amount: " + str(settings.expenses[i].get_amount()) + " Type: " + str(settings.expenses[i].get_type()))