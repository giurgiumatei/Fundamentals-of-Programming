from init import students
from init import histudents
import init
import copy

def replace(): #this function replaces the score of a participant in the list
    while(True):
        try:
            poz=int(input("Which participant do you want to have his scores replaced? "))
            assert 0<=poz<=len(init.students)-1
            break
        except:
            print("Invalid Input")
    
    while(True):
        try:
            prob=int(input("Which problems score do you want to modify? "))
            assert 1<=prob<=3
            break
        except:
            print("Invalid Input")

    while(True):
        try:
            scr=int(input("Type in the new score: "))
            assert 0<=scr<=10
            break
        except:
            print("Invalid Input")
    
    init.students[poz][prob-1]=scr
    init.histudents.append(copy.deepcopy(init.students))
    



def multiremove(): #this function removes a range of participants from the list
   
   
    while(True):
        try:
            spoz=int(input("Type the position of the first participant: "))
            epoz=int(input("Type the position of the last participant: "))
            assert 0<=spoz<=len(init.students)-1
            assert 0<=epoz<=len(init.students)-1
            break
        except:
             print("Invalid Input")

    for i in range(spoz,epoz+1):
        for j in range (0,3):
            init.students[i][j]=0
    init.histudents.append(copy.deepcopy(init.students))



def remove(): #this function sets a participant scores to 0
    
    while(True):
        try:
            poz=int(input("Which participant do you want to have his scores removed? "))
            assert 0<=poz<=len(init.students)-1
            break
        except:
            print("Invalid Input")
    
    for i in range (0,3):
        init.students[poz][i]=0
    init.histudents.append(copy.deepcopy(init.students))
    
