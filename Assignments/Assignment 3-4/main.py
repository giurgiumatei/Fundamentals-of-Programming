import ui
import cit
import init
import undo
import req1
import req2
import req3
import req4
import req5
def menu(): # main menu function 
    
    
    while True:
        
            try:
                option0=str(input("Use a new list or predefined? "))
                assert option0 == "New" or option0 == "Predefined"
                break
            except: 
                print("Invalid input")
    
    if option0 == "New":
        cit.citire()
        
    
    
    
    
    
    
    while(True):
        while True:
        
            try:
                option=input("Give the number corresponding to the requirement: ")
                assert str(option) == "Undo" or int(option) >= 0 and int(option) < 6 
                break
            except: 
                print("Invalid input")
        
        
        if str(option) == "Undo":
            undo.undo()
        elif int(option)==1:
            ui.requirement1()
        elif int(option)==2:
            ui.requirement2()
        elif int(option)==3:
            ui.requirement3()
        elif int(option)==4:
            ui.requirement4()
        elif int(option)==5:
            ui.requirement5()
        elif int(option)==0:
            break





menu() #program starts here
