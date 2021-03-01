from Domain import *

class persons_repo:


    def person_construct(self,line):
        id=line[0]
        immune_status=line[1]
        status=line[2]
        person=Person(id,immune_status,status)
        
        return person

    def __init__(self):

        self.persons=[]

        with open ("D:\FP\Test\Persons.txt","r") as f:

            reader=f.readline()
            reader=reader.strip('\n')
            reader=reader.strip()
            line=reader.split(',')

            pnew=self.person_construct(line)
            self.persons.append(pnew)

            while reader:
                reader=f.readline()
                if reader!="":

                    
                    reader=reader.strip('\n')
                    reader=reader.strip()
                    line=reader.split(',')

                    pnew=self.person_construct(line)
                    self.persons.append(pnew)

    def get_persons(self):
        return self.persons
    def set_persons(self,value):
        self.persons=value
        
