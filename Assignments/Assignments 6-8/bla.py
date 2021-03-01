class Assignment_Inventory:

    service2=Services.Service()

    def __init__(self,assignments):
        self.assignments=assignments
       

    def addStudent(self,snew):
        
        self.assignments.append(snew)

    def removeStudent(self,s_id):
        for i in range(len(assignments)):
            if assignments[i].get_studentID() == s_id:
                del assignments[i]
                break

        
    
    def updateStudent(self,s_id):
        for i in range(len(assignments)):
            if assignments[i].get_studentID() == s_id:
                new_name=input("Give the new name: ")
                new_group=input("Give the new group: ")
                snew=Student(s_id,new_name,new_group)
                if self.service1.validate_student(snew) == True:
                    for i in range(len(assignments)):
                        if assignments[i].get_studentID() == s_id:
                            assignments[i]=snew
                else:print("Bad input! ")



        

    def listStudents(self):
        for i in range(len(assignments)):
            print(assignments[i].get_name())

    def is_in_list(self,s_id):
        for i in range(len(assignments)):
            print(i)
            if assignments[i].get_studentID() == s_id:
                return True
        return False