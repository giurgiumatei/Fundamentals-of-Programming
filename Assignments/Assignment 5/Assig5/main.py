import Classes



def main():#this function builds the UI and asks the user if he wants a new list or a predefined 1
    while True:
        
            try:
                start=str(input("Use a new list or predefined? "))
                assert start == "New" or start == "Predefined"
                break
            except: 
                print("Invalid input")

    u=Classes.UI()
    
    if start == "New":
        
        u.build()
    u.menu()
    
    
    
    




main()#program starts here