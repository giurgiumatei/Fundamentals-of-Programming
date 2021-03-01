import init

def afisare(): # this function displays the participants and their grades
    n=len(init.students)

    for i in range(0,n):
        print("Participant "+ str(i) + ":   " + str(init.students[i][0]) + " , " + str(init.students[i][1]) + " , " + str(init.students[i][2]))
    return