from init import students
from init import histudents
import init

def custom_sort(t): # this function is used as a key so that the list is sorted by the average of each student
    return (t[0]+t[1]+t[2])/3

def sortbyaverage(): #this function sorts the students by their averages
    sorted_students=sorted(init.students,key=custom_sort,reverse=True)
    print(sorted_students)
    




def listbyaverage():# this function displays students whose average is < = or > than a given amount
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
                print("Participant "+ str(i) + ":   " + str(init.students[i][0]) + " , " + str(init.students[i][1]) + " , " + str(init.students[i][2]))
        elif indice==2:
            if sum(init.students[i])/3 == avg:
                print("Participant "+ str(i) + ":   " + str(init.students[i][0]) + " , " + str(init.students[i][1]) + " , " + str(init.students[i][2]))
        elif sum(init.students[i])/3 > avg:
            print("Participant "+ str(i) + ":   " + str(init.students[i][0]) + " , " + str(init.students[i][1]) + " , " + str(init.students[i][2]))

    return




