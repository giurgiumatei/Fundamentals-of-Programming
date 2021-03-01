from init import students
from init import histudents
import init

def add():#this function adds a new participant to the list
    print("Type in the scores of the new participant: ")
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
    init.histudents.append(init.students.copy())

def insert(): #this function inserts a participant in the list on a given position
    print("Type in the scores of the new participant ")
    while(True):
            try:
                ele=[int(input()),int(input()),int(input())]
                assert 0<=ele[0]<=10 
                assert 0<=ele[1]<=10 
                assert 0<=ele[2]<=10 
                break
            except:
                print("Invalid Input")
    ind=int(input("Give the position on which you want to insert: "))
    init.students.insert(ind,ele)
    init.histudents.append(init.students.copy())
