from Repository import *
import datetime
from Domain import Student,Assignment,Grade
import pickle




class Student_Inventory_Pickle(Student_Inventory):


    def __init__(self,students): 

        with open("G:\FP\Assignments\Assignment 9\StudentPickleRepo.pkl","rb") as f:
            try:
                self.students = pickle.load(f)
            except EOFError:
                self.students=students
        with open("G:\FP\Assignments\Assignment 9\StudentPickleRepo.pkl","wb") as f:
            pickle.dump(self.students,f)


    def write_to_file(self,students):
        with open("G:\FP\Assignments\Assignment 9\StudentPickleRepo.pkl","wb") as f:
            pickle.dump(self.students,f)

    def addStudent(self,snew):
        super().addStudent(snew)
        self.write_to_file(self.students)

    def removeStudent(self,s_id):
        super().removeStudent(s_id)
        self.write_to_file(self.students)

    def listStudents(self):
        with open("G:\FP\Assignments\Assignment 9\StudentPickleRepo.pkl","rb") as f:
            self.students=pickle.load(f)

            for i in range(len(self.students)):
                print(i)
                if self.students[i].name_cont == 1:
                    print(self.students[i].get_name())
                else:
                    n=self.students[i].get_name()
                    c=self.students[i].name_cont

                    print(str(n)+"("+str(c)+")")

class Assignment_Inventory_Pickle(Assignment_Inventory):


    def __init__(self,assignments):

        with open("G:\FP\Assignments\Assignment 9\AssignmentPickleRepo.pkl","rb") as f:
            try:
                self.assignments = pickle.load(f)
            except EOFError:
                self.assignments=assignments
        with open("G:\FP\Assignments\Assignment 9\AssignmentPickleRepo.pkl","wb") as f:
            pickle.dump(self.assignments,f)


    def write_to_file(self,assignments):
        with open("G:\FP\Assignments\Assignment 9\AssignmentPickleRepo.pkl","wb") as f:
            pickle.dump(self.assignments,f)

    def addAssignment(self,anew):
        super().addAssignment(anew)
        self.write_to_file(self.assignments)

    def removeAssignment(self,a_id):
        super().removeAssignment(a_id)
        self.write_to_file(self.assignments)
    def updateAssignment(self,anew):
        super().updateAssignment(anew)
        self.write_to_file(self.assignments)


    def listAssignments(self):
        with open("G:\FP\Assignments\Assignment 9\AssignmentPickleRepo.pkl","rb") as f:
            self.assignments=pickle.load(f)

            for i in range(len(self.assignments)):
                
                print(self.assignments[i].get_description())


class Grade_Inventory_Pickle(Grade_Inventory):


    def __init__(self,assignments):

        with open("G:\FP\Assignments\Assignment 9\GradePickleRepo.pkl","rb") as f:
            try:
                self.grades = pickle.load(f)
            except EOFError:
                self.grades=grades
        with open("G:\FP\Assignments\Assignment 9\GradePickleRepo.pkl","wb") as f:
            pickle.dump(self.grades,f)


    def write_to_file(self,grades):
        with open("G:\FP\Assignments\Assignment 9\GradePickleRepo.pkl","wb") as f:
            pickle.dump(self.grades,f)

    def add_Grade(self,gnew):
        super().add_grade(gnew)
        self.write_to_file(self.grades)

    def remove_Grade(self):
        super().remove_grade()
        self.write_to_file(self.grades)

    
               

    
