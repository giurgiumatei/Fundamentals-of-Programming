from Domain import *
import datetime
#import Services



class Iter:
    def __init__(self,lst):

        self.list=lst

        self.index = -1

    def __iter__(self):
        "iterator for the class"
        return iter(self.list)

    def __len__(self):
        "for the length"
        return len(self.list)

   
   
    def __next__(self):
        "getter for the next item from the list"
        if self.index > len(self.list) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.list[self.index]

   
    def __setitem__(self, index, val):
        "the setter for an item"
        self.list[index] = val

    def __getitem__(self, index):
        "we get here the item"
        return self.list[index]

    def append(self, x):
        self.list.append(x)

    def __delitem__(self, index):
        "here is the delete function"
        del self.list[index]

    def pop(self, id):
        self.list.pop(id - 1)

    def clear(self):
        self.list.clear()


class Methods():
    def gnomeSort(self,givenList,comparisonFunction):
        '''comparison funct is considered such as:
           cmp(a,b) == True <=> a>=b
        '''
        index = 0
        while index < len(givenList):
            if index == 0 or comparisonFunction(givenList[index][-1], givenList[index-1][-1]) == True:
                index+=1
            else:
                auxilliaryVariable = givenList[index]
                givenList[index] = givenList[index-1]
                givenList[index-1] = auxilliaryVariable
                index-=1
        return givenList


    def filter(self,givenList, filterCriteria):
        temporaryList = []
        for i in givenList:
            if filterCriteria(i) == True:
                temporaryList.append(i)
        return temporaryList