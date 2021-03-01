from Repository import *
import datetime
from Domain import Student,Assignment,Grade

class Student_Inventory_Txt(Student_Inventory):


    def create_assignment_object(self,line):
        assignmentID=line[0]
        assignmentName=line[1]

        if line[2][-1] == '\n':
            assignmentDate=line[2][:-1]
        else: assignmentDate=line[2]
        assignew=Assignment(assignmentID,assignmentName,assignmentDate)
        return assignew





    def create_student_obj(self,line):
            print(line)
        
            studentID=line[0]
            studentName=line[1]
            studentGrp=line[2]
            snew=Student(studentID,studentName,studentGrp,'')
            if line[3]!='\n':
                assignments_list=line[3].split('/')
            
                for ass  in assignments_list:

                    b=ass.split('.')
                    a=self.create_assignment_object(b)
                    snew.assignments_owned.append(a)
                
            
            
            return snew



    def __init__(self):
        
        self.students=[]
        with open('G:\FP\Assignments\Assignment 9\StudentTextRepo.txt','r') as f:
         reader = f.readline()
         line=reader.split(',')
         snew=self.create_student_obj(line)
         self.students.append(snew)

         while reader:
            reader = f.readline()
            if reader!="":
            
                line=reader.split(',')
                snew=self.create_student_obj(line)
                self.students.append(snew)



    def addStudent(self,snew): # adds a new student in the students repository
        
        super().addStudent(snew)
        self.write_to_file(self.students)


    def removeStudent(self,s_id):
        super().removeStudent(s_id)
        self.write_to_file(self.students)
        

    def updateStudent(self,snew):
        super().updateStudent(snew)
        self.write_to_file(self.students)

    def deconstruct(self,student):
        s_id=student.get_studentID()
        s_name=student.get_name()
        s_group=student.get_group()
        s_assignments=student.get_assigments_owned()

        string=str(str(s_id) + ',' + str(s_name) + ',' + str(s_group) + ',' )

        if len(s_assignments) !=0:

            for a in s_assignments:
                a_id=a.get_assignmentID()
                a_descr=a.get_description()
                a_deadline=a.get_deadline()
                

                string+=str(str(a_id) +'.'+str(a_descr) + '.' + str(a_deadline)+'/')
            return string[:-1]

        return string

    def assign_to_one(self,assig_id,s_id): # gives an assignment to one student by assignment ID and student ID
        super().assign_to_one(assig_id,s_id)
        self.write_to_file(self.students)

    def assign_to_many(self,assig_id,grp):# gives an assignment to a group of students by assignment ID
        super().assign_to_many(assig_id,grp)
        self.write_to_file(self.students)



    def write_to_file(self,students):
        with open ('G:\FP\Assignments\Assignment 9\StudentTextRepo.txt','w') as f:
            for s in students:
                line=self.deconstruct(s)
                f.write(line+'\n')



class Assignment_Inventory_Txt(Assignment_Inventory):

    def create_assignment_obj(self,line):
            print(line)
        
            assignmentID=line[0]
            assignmentName=line[1]
            assignmentDate=line[2]
            
            anew=Assignment(assignmentID,assignmentName,assignmentDate)

            return anew


    def __init__(self):
        
        self.assignments=[]
        with open('G:\FP\Assignments\Assignment 9\AssignmentTextRepo.txt','r') as f:
         reader = f.readline()
         reader=reader.strip('\n')
         reader=reader.strip()
         line=reader.split(',')
         anew=self.create_assignment_obj(line)
         self.assignments.append(anew)

         while reader:
            reader = f.readline()
            if reader!="":

                reader=reader.strip('\n')
                reader=reader.strip()
                line=reader.split(',')
                anew=self.create_assignment_obj(line)
                self.assignments.append(anew)

    def deconstruct(self,assignment):
        a_id=assignment.get_assignmentID()
        a_descr=assignment.get_description()
        a_dline=assignment.get_deadline()
        

        string=str(str(a_id) + ',' + str(a_descr) + ',' + str(a_dline) + ',' )

    
        return string


    def write_to_file(self,assignments):
        with open ('G:\FP\Assignments\Assignment 9\AssignmentTextRepo.txt','w') as f:
            for a in assignments:
                line=self.deconstruct(a)
                f.write(line+'\n')




    def addAssignment(self,anew): # adds a new assignment in the assignments repository
        
        super().addAssignment(anew)
        self.write_to_file(self.assignments)


    def removeAssignment(self,a_id):# removes an assignment from the assignments repository
        super().removeAssignment(a_id)
        self.write_to_file(self.assignments)


    def updateAssignment(self,anew):# update an assignment from the assignments repository
        super().updateAssignment(anew)
        self.write_to_file(self.assignments)



class Grade_Inventory_Txt(Grade_Inventory):

    def create_grade_obj(self,line):
            print(line)
        
            assignmentID=line[0]
            studentID=line[1]
            grade=int(line[2])
            
            gnew=Grade(assignmentID,studentID,grade)

            return gnew


    def __init__(self):
        
        self.grades=[]
        with open('G:\FP\Assignments\Assignment 9\GradeTextRepo.txt','r') as f:
         reader = f.readline()
         reader=reader.strip('\n')
         reader=reader.strip()
         line=reader.split(',')
         gnew=self.create_grade_obj(line)
         self.grades.append(gnew)

         while reader:
            reader = f.readline()
            if reader!="":

                reader=reader.strip('\n')
                reader=reader.strip()
                line=reader.split(',')
                gnew=self.create_grade_obj(line)
                self.grades.append(gnew)

    def deconstruct(self,grade):
        assignment_id=grade.get_assignmentID()
        student_id=grade.get_studentID()
        grd=grade.get_grade()
        

        string=str(str(assignment_id) + ',' + str(student_id) + ',' + str(grd) + ',' )

    
        return string


    def write_to_file(self,assignments):
        with open ('G:\FP\Assignments\Assignment 9\GradeTextRepo.txt','w') as f:
            for a in assignments:
                line=self.deconstruct(a)
                f.write(line+'\n')




    def add_Grade(self,gnew): # adds a new grade in the grades repository
        
        super().add_grade(gnew)
        self.write_to_file(self.grades)


    def remove_Grade(self):# removes an assignment from the assignments repository
        super().remove_grade()
        self.write_to_file(self.grades)







        



        





    

    