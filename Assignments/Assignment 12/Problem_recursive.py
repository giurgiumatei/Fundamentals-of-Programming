from copy import deepcopy

def mountain(index,l,length):
    
    left=0
    right=0
    mountain_sequence=[]
    i=deepcopy(index)
    
    while i < (length-1) and l[i]<l[i+1]: 
        
        mountain_sequence.append(l[i])
        left+=1
        i+=1

    while i < (length-1) and l[i]>l[i+1]: 
        
        mountain_sequence.append(l[i])
        right+=1
        i+=1
    if l[i]<l[i-1]:
        mountain_sequence.append(l[i])

    if left!=0 and right!=0:
        print(mountain_sequence)


'''
def powerset(set):

    bs=[]

    for i in range (2** len(set)):
        s=[]

        for j in range (len(set)):
            if i & (i<<j):
                s.append(set[j])
            
        bs.append(s)

    return bs
'''


def ismountain(sequence,lenght):
    left=0
    right=0

    i=0

    while i < (lenght-1) and sequence[i]<sequence[i+1]: 
        
        
        left+=1
        i+=1
    
    while i < (lenght-1) and sequence[i]>sequence[i+1]: 
        
        
        right+=1
        i+=1

    if right!=0 and left!=0:
        print(sequence)



def create_sequence(l,n):
    print("Give the elements of the sequence: ")
    while n:
        el=int(input())
        l.append(el)
        n-=1

    return l

def backtrack(start,finish,l):
    if start!=finish:
        sequence=[]
        i=start

        while i<finish:
            
            sequence.append(l[i])
            i+=1
            if len(sequence)>=3:
                ismountain(sequence,len(sequence))
            if sequence[-1] is l[-1]:
                
                backtrack(start+1,finish,l)
        




def main():


    l=[]

    n=int(input("Give the number of elements: "))
    l=create_sequence(l,n)

    #print(powerset(l))

    backtrack(0,n,l)

    



main()
