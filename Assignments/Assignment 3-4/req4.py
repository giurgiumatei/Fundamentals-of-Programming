from init import students
from init import histudents
import init
def avgavg():# This function writes the average of the average scores for participants between given position
    while(True):
        try:
            spoz=int(input("Which range of participants do you want to have their score considered "))
            epoz=int(input())
            assert 0<=spoz<=len(init.students)-1
            assert 0<=epoz<=len(init.students)-1
            break
        except:
             print("Invalid Input")
    cont=0
    suma=0
    for i in range(spoz,epoz+1):
        suma=suma+(init.students[i][0]+init.students[i][1]+init.students[i][2])/3
        cont+=1
    print(suma/cont)

def minavg(): # This function the lowest score of the participants between given positions
    while(True):
        try:
            spoz=int(input("Which range of participants do you want to have their score considered "))
            epoz=int(input())
            assert 0<=spoz<=len(init.students)-1
            assert 0<=epoz<=len(init.students)-1
            break
        except:
             print("Invalid Input")
    lavg=(init.students[spoz][0]+init.students[spoz][1]+init.students[spoz][2])/3
    for i in range(spoz,epoz+1):
        if lavg>(init.students[i][0]+init.students[i][1]+init.students[i][2])/3:
            lavg=(init.students[i][0]+init.students[i][1]+init.students[i][2])/3
        
    print(lavg)





def problem4(): # This function solves problem 4
    print("Which criteria do you want to use: average or minimum?")
    while(True):
        try:
            m=str(input())
            assert m=="average" or m=="minimum" 
            
            break
        except: 
            print("Invalid input")
        
    if m=="average":
        avgavg()
    else: minavg()