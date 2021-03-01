from init import students
from init import histudents
import afis
import req1
import req2
import req3
import req4
import req5
import init

def requirement1(): #This function does requirement 1
     
    while True:
            
        try:
            option=str(input("Add or Insert? "))
            assert option == "Add" or option == "Insert"
            break
        except: 
            print("Invalid input")

    if option == "Add":
        req1.add()
        
    elif option == "Insert":
        req1.insert()

def requirement2(): #This function does requirement 2
    
    while True:
            
        try:
            option=str(input("Remove or Replace? "))
            assert option == "Remove" or option == "Replace"
            break
        except: 
            print("Invalid input")

    if option == "Remove":
        while True:
            
            try:
                option1=str(input("Remove one or multiple? "))
                assert option1 == "One" or option1 == "Multiple"
                break
            except: 
                print("Invalid input")
        if option1 == "One":
            req2.remove()
        elif option1 == "Multiple":
            req2.multiremove()
        
    elif option == "Replace":
        req2.replace()

def requirement3(): #This function does requirement 3
    
    while True:
            
        try:
            option=str(input("List, list by average or list sorted? "))
            assert option == "List" or option == "List by average" or option == "List sorted"
            break
        except: 
            print("Invalid input")
    
    if option=="List":
        afis.afisare()
    elif option=="List Sorted":
        req3.sortbyaverage
    elif option=="List by average":
        req3.listbyaverage

def requirement4(): #This function does requirement 4
    req4.problem4()

def requirement5(): #This function does requirement 5
    while True:
            
        try:
            option=str(input("Top by average, top by grade or remove by average? "))
            assert option == "Top by average" or option == "Top by grade" or option == "Remove"
            break
        except: 
            print("Invalid input")
    
    if option == "Top by average":
        req5.topbyavg()
    elif option == "Top by grade":
        req5.topbygrade()
    elif option == "Remove":
        req5.removebyaverage()
        



        
