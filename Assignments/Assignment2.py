numere = [ ]#this list contains the complex numbers

def citire(): #this function reads the complex numbers and stores them as a list of lists
    n=int(input("Give the number of complex elements: "))

    for i in range(0,n):
        print("Give the values for element number "+str(i+1)+" : ")
        ele=[int(input("Give the real part: ")),int(input("Give the imaginary part: "))]
        numere.append(ele)
    return

def afisare():#this function types the list in the console
    n=len(numere)

    for i in range(0,n):
        print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")



def cer1():#this function solves req. 1
    l=int(0)
    maxl=int(0)
    n=len(numere)
    b=int(-1)
    e=int(-1)

    for i in range(0,n-1):
        l=0
        if numere[i][0]>numere[i-1][0]:
            l+=1
            for j in range(i+1,n):
                if numere[j][0]>numere[j-1][0]:
                    
                    l+=1
                else: break
            if l > maxl:
                maxl=l
                b=i-1
                e=j
    
    if e==n-1:
        for i in range(b,e+1):
            
            print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")
    else:
        for i in range(b,e):
            
            print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")            
 


    



    

def cer5():#this function solves req 5
    l=int(0)
    maxl=int(0)
    n=len(numere)
    b=int(-1)
    e=int(-1)

    for i in range(0,n-1):
        l=0
        if numere[i][1]==0:
            l+=1
            for j in range(i+1,n):
                if numere[j][1] == 0:
                    
                    l+=1
                else: break
            if l > maxl:
                maxl=l
                b=i
                e=j
    if e==n-1:
        for i in range(b,e+1):
                
            print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")
    else:
        for i in range(b,e):
                
            print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")
                
 



def cer10():#this function solves req.10
    l=int(0)
    maxl=int(0)
    n=len(numere)
    b=int(-1)
    e=int(-1)
    s1=int(0)
    s2=int(0)
    inceput=int(0)

    for i in range(0,n):
        s1+=numere[i][0]
        s2+=numere[i][1]

        if s1>10 or s2>10:
            s1=0
            s2=0
            l=0
            inceput+=1
            i=inceput-1
        elif s1==10 and s2==10:
          if l > maxl:
            maxl=l
            b=inceput
            e=i
            
        else: l+=1
        
    if e==n-1:
        for i in range(b,e+1):
                
            print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")
        else:
            for i in range(b,e):
                
                print(str(numere[i][0]) + "+" + str(numere[i][1]) + "i")

    
            
        





         

def optiunea3():#when this function is called it asks the user which req. should be solved
    n=int(input("Which requirement do you want to solve: "))

    if n==5:
        cer5()
    elif n==10:
        cer10()
    elif n==1:
        cer1()
    else: print("Invalid number")
    


def menu():#this function acts like a main function which calls the others
    

    citire()

    

    while(True):
        option=int(input("Give a number corresponding to the option:"))
        if option==4:
            return
        elif option==1:
           citire()
        elif option==2:
            afisare()
        elif option==3:
            optiunea3()
        elif option==0:
            break


menu()#program starts here

