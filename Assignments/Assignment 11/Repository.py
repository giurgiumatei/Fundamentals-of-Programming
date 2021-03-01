from Domain import *
import datetime
from Iterator import *
#import Services

#Repository  module, manages the lists
'''
class Repository:=

    def __init__(self):
        self.students = Student_Inventory
        self.grades = Grade_Inventory()
        self.assignments = Assignment_Inventory()

    def getStudents(self):
        return self.students
    
    def getGrades(self):
        return self.grades
    
    def getAssignments(self):
        return self.assignments
'''
#Student Repository class
class Student_Inventory:

    

    def __init__(self,students): 
        self.students=Iter(students)

    def get_students(self):
        return self.students
       

    def addStudent(self,snew): # adds a new student in the students repository
        
        self.students.append(snew)
        return self.students[-1]

    

    def addStudent_2(self,snew): # adds a new student in the students repository and checks if the name was already in the list
        
        for i in range(len(self.students)):
            
            if snew.get_name() == self.students[i].get_name():
                snew.name_cont+=1
                
                
        self.students.append(snew)

   
    def removeStudent(self,s_id): # removes a student from the students repository by ID
        for i in range(len(self.students)):
            if self.students[i].get_studentID() == s_id:
                del self.students[i]
                break

        return self.students[-1]

        
    
    def updateStudent(self,snew): #updates a students data by ID
        
        for i in range(len(students)):
            if self.students[i].get_studentID() == snew.get_studentID():
                self.students[i]=snew
                return self.students[i]



        

    def listStudents(self): # lists all students present in the repository
        for i in range(len(self.students)):
            print(i)
            if self.students[i].name_cont == 1:
                print(self.students[i].get_name())
            else:
                n=self.students[i].get_name()
                c=self.students[i].name_cont

                print(str(n)+"("+str(c)+")")

    
    def is_in_list(self,s_id): # checks by ID if a student is present in the repository
        for i in range(len(self.students)):
            
            if self.students[i].get_studentID() == s_id:
                return True
        return False

    def pos_in_list(self,s_id): #return the position of a student in the repository or False if he does not exist
        for i in range(len(self.students)):
            
            if students[i].get_studentID() == s_id:
                return i
        return False
    
    
   
        

    def assign_to_one(self,assig_id,s_id): # gives an assignment to one student by assignment ID and student ID
        for i in range(len(self.students)):
            if self.students[i].get_studentID() ==s_id:
                self.students[i].assignments_owned.append(assig_id)
    def pop_from_one(self,s_id):
        for i in range(len(self.students)):
            if self.students[i].get_studentID() ==s_id:
                self.students[i].assignments_owned.pop()
                

    def assign_to_many(self,assig_id,grp):# gives an assignment to a group of students by assignment ID
       for i in range(len(self.students)):
            if self.students[i].get_group() ==grp:
                self.students[i].assignments_owned.append(assig_id)

    def pop_from_many(self,grp):
        for i in range(len(self.students)):
            if self.students[i].get_group() ==grp:
                    self.students[i].assignments_owned.pop()


    def list_students_assignments(self):# lists students and their assignments
        for i in range(len(self.students)):
            if self.students[i].name_cont == 1:
                strn=""
                for x in self.students[i].get_assigments_owned():
                    strn=strn+ " " + x.get_assignmentID()
                print(str(self.students[i].get_name()) + " - " + strn)
            else:
                n=self.students[i].get_name()
                c=self.students[i].name_cont
                print(str(n)+"("+str(c)+")"+" - "+ str(self.students[i].get_assigments_owned()))

    
    
    def list_ungraded_assignments(self,s_id): # list the ungraded assignments of a student given by a student ID
        position=self.pos_in_list(s_id)
        ungraded_assignments=[]
        for i in range(len(self.students[position].assignments_owned)):
            if  self.students[position].get_assigments_owned()[i].get_isgraded()==False:
                ungraded_assignments.append(self.students[position].assignments_owned[i])
        
        return ungraded_assignments

    def grade_assignment(self,s_id,a_id): #Grade an assigment of a student
        position=self.pos_in_list(s_id)
        
        for i in range(len(self.students[position].assignments_owned)):
            if  self.students[position].assignments_owned[i].get_assignmentID()==a_id:
                self.students[position].assignments_owned[i].set_isgraded(True)

    def ungrade_assignment(self,s_id,a_id): #Grade an assigment of a student
        position=self.pos_in_list(s_id)
        
        for i in range(len(self.students[position].assignments_owned)):
            if  self.students[position].assignments_owned[i].get_assignmentID()==a_id:
                self.students[position].assignments_owned[i].set_isgraded(False)



    
                
    def students_late(self,assig): #Returns a list of students who were late with their assignments

        students_lte=[]
        for i in range (len(self.students)):
            for j in range(len(self.students[i].get_assigments_owned())):
                if self.students[i].get_assigments_owned()[j] == assig:
                    students_lte.append(self.students[i].get_name())
        return students_lte

    def student_by_id(self,s_id):# returns an assignment by ID
        
        for i in range(len(self.students)):
            
            if self.students[i].get_studentID() == s_id:
                return self.students[i]
        return False

    


        
       






#Assignment Repository class
class Assignment_Inventory:

    

    def __init__(self,assignments):
        self.assignments=Iter(assignments)
       

    def addAssignment(self,assignew): # adds a new assignment in the assignments repository
        
        self.assignments.append(assignew)
        return self.assignments[-1]

    def removeAssignment(self,assig_id):# removes an assignment by ID from the assignments repository
        for i in range(len(assignments)):
            if assignments[i].get_assignmentID() == assig_id:
                
                del assignments[i]
                break
        return self.assignments[-1]

        
    
    def updateAssignment(self,anew):# update an assignment by ID
        for i in range(len(self.assignments)):
            if self.assignments[i].get_assignmentID() == anew.get_assignmentID():
                self.assignments[i]=anew
                return self.assignments[i]

    def get_assignments(self):
        return self.assignments



        

    def listAssignments(self):# lists the avaible assignments
        for i in range(len(assignments)):
            print(assignments[i].get_description())

    
    def is_in_list(self,assig_id):# checks if an assignment is in the repository and returns False if it isn't
        for i in range(len(assignments)):
            
            if assignments[i].get_assignmentID() == assig_id:
                return True
        return False

    def assignment_by_id(self,assig_id):# returns an assignment by ID
        
        for i in range(len(self.assignments)):
            
            if self.assignments[i].get_assignmentID() == assig_id:
                return self.assignments[i]
        return False

    def passed_assigments(self):# returns a list of assignments with the deadline <today
        assignm_list=[]
        today=datetime.datetime.today()

        for i in range(len(self.assignments)):
            if datetime.datetime.strptime(self.assignments[i].get_deadline(),'%Y-%m-%d') < today:
                assignm_list.append(self.assignments[i])
        return assignm_list






#Grades Repository Class
class Grade_Inventory:

    def __init__(self,grades):
        self.grades=Iter(grades)
   
    def add_grade(self,value):#adds a new grade in the grade repository
        self.grades.append(value)

    def remove_grade(self):
        self.grades.__delitem__(-1)

    def get_grades(self):
        return self.grades

    def name_by_grade(self,value):
        pass





