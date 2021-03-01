from init import students
from init import histudents
import init
import copy

def custom_sort(t): # this function is used as a key so that the list is sorted by the average of each student
    return (t[0]+t[1]+t[2])/3


def topbyavg(): #this function list the first m students sorted by average in descending order
    sorted_students=sorted(init.students,key=custom_sort,reverse=True)
    while(True):
        try:
            m=int(input("How many students do you want to see in this ranking? "))
            assert m>0
            assert m<len(sorted_students)
            break
        except: 
            print("Invalid input")
    for i in range(0,m):
        print(sorted_students[i])

def topbygrade(): # this function creates a ranking based on the grades of a given problem
    while(True):
        try:
            m=int(input("Which problem do you  want to be considered? "))
            assert m>0
            assert m<=3
            break
        except: 
            print("Invalid input")
    sorted_students=sorted(init.students,key=lambda x:x[m-1],reverse=True)
    print(sorted_students)
    
def removebyaverage():# this function removes participants by average
    n=len(init.students)
    avg=int(input("Type the average: "))
    while(True):
        try:
            semn=input("Type the sign: ")
            assert (semn in "<=>")==True
            break
        except:
            print("Invalid Input")
    indice=0

    if semn=='<':
        indice=1
    elif semn=='=':
        indice=2
    else: indice=3

    for i in range(0,n):
        if indice==1:
            if sum(init.students[i])/3 < avg:
                init.students[i][0]=0
                init.students[i][1]=0
                init.students[i][2]=0
        elif indice==2:
            if sum(students[i])/3 == avg:
                init.students[i][0]=0
                init.students[i][1]=0
                init.students[i][2]=0
        elif sum(students[i])/3 > avg:
            init.students[i][0]=0
            init.students[i][1]=0
            init.students[i][2]=0
        init.histudents.append(copy.deepcopy(init.students))

    return