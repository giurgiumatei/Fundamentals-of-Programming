from init import students
from init import histudents
import init

def citire(): #this function reads input from the user
    init.students.clear()
    
    while(True):
        try:
            n=int(input("Give the number of students: "))
            assert n>1
            break
        except: 
            print("Invalid input")

    print("Give the score of the first student: ")

    for i in range(0,n):
        while(True):
            try:
                ele=[int(input()),int(input()),int(input())]
                assert 0<=ele[0]<=10
                assert 0<=ele[1]<=10
                assert 0<=ele[2]<=10   
                break
            except:
                print("Invalid Input")
            
        init.students.append(ele)
        if i!=(n-1):
            print("Give the scores of the next student: ")
    
    return
