from Domain import *
from Repository import *
from collections import defaultdict
import copy
from UndoFunction import *
import random

#Service module, contains every functionality which doesn't modify the lists of students and assignments


class Service:

    def __init__(self,s_repo,assig_repo,grd_repo):
        self.s_repo=s_repo
        self.assig_repo=assig_repo
        self.grd_repo=grd_repo
        self.undo_controller=UndoController(self.s_repo,self.assig_repo,self.grd_repo)
        
        



    def constr_student(self,snew_ID,snew_Name,snew_Group): # builds a student object
        if self.validate_student(snew_ID,snew_Name,snew_Group) == False:
            return False
       
        snew=Student(snew_ID,snew_Name,snew_Group,"")
        return snew
    
    
    def validate_student(self,s_ID,s_Name,s_Group): # checks if a student is valid
        if s_ID.isnumeric():
            if s_Name.isalpha():
                return True
        return False

    def add_student2(self,snew_ID,snew_Name,snew_Group): # calls add_student2 from the student repo class
        snew=self.constr_student(snew_ID,snew_Name,snew_Group)
        self.s_repo.addStudent_2(snew)
        
        self.undo_controller.history.append(["addStudent_2",snew])
        self.undo_controller.index+=1
    
    
    
    def add_student(self,snew_ID,snew_Name,snew_Group): # constructs a student object and adds it in the student repo class
        
        if self.constr_student(snew_ID,snew_Name,snew_Group) == False:
            
            return False
        snew=self.constr_student(snew_ID,snew_Name,snew_Group)
        self.s_repo.addStudent(snew)
       
        self.undo_controller.history.append(["addStudent",snew])
        self.undo_controller.index+=1
        return True

    
    def is_in_list_student(self,s_id): # checks if a student is in the students repo    
        if self.s_repo.is_in_list(s_id) == False:
            return False
        return True

    def is_in_list_assignment(self,a_id):# checks if an assignment is in assignment repo
        if self.assig_repo.is_in_list(a_id) == False:
            return False
        return True
        
    
    
    def remove_student(self,s_id):# calls the remove student function from student repo class
        snew=self.s_repo.student_by_id(s_id)
        self.s_repo.removeStudent(s_id)
        
        self.undo_controller.history.append(["removeStudent",snew])
        self.undo_controller.index+=1


    def remove_assignment(self,a_id):# calls the remove assignment
        anew=self.assig_repo.assignment_by_id(a_id)
        self.assig_repo.removeAssignment(a_id)
        
        self.undo_controller.history.append(["removeAssignment",anew])
        self.undo_controller.index+=1



    
    def update_student(self,snew_ID,snew_Name,snew_Group):# calls the update student function from the student repo
       
       snew=Student(snew_ID,snew_Name,snew_Group,"")
       svechi=self.s_repo.student_by_id(snew_ID)
      
       self.undo_controller.history.append(["updateStudent",[svechi,snew]])
       self.undo_controller.index+=1

       self.s_repo.updateStudent(snew)
       return True

    def update_assignment(self,anew_ID,anew_Description,anew_Deadline):# calls the update assignment function from the assignment repo
        anew=Assignment(anew_ID,anew_Description,anew_Deadline)
        avechi=self.assig_repo.assignment_by_id(anew_ID)
        
        self.undo_controller.history.append(["updateAssignment",[avechi,anew]])
        self.undo_controller.index+=1

        self.assig_repo.updateAssignment(anew)
        return True
    
    
    
    def listStudents(self): # calls the list students function
        self.s_repo.listStudents()
    def listAssignments(self):# calls the list assignments function
        self.assig_repo.listAssignments()
    def list_students_assignments(self):# calls the list students  assignments function 
        self.s_repo.list_students_assignments()
    def list_ungraded_assignments(self,s_id):# calls the list ungraded assignments function
        return self.s_repo.list_ungraded_assignments(s_id)
    
    
    
    def constr_assignment(self,anew_ID,anew_description,anew_deadline):# builds an assignment object
        if self.validate_assignment(anew_ID,anew_description,anew_deadline) == False:
            return False
       
        anew=Assignment(anew_ID,anew_description,anew_deadline)
        return anew


    def validate_assignment(self,a_ID,a_description,a_deadline):# checks if an assignment is valid
        if a_ID.isnumeric():
            while True:
                try:
                    datetime.datetime.strptime(a_deadline,'%Y-%m-%d')
                   
                    return True
                except:return False
        

    
   
    def add_assignment(self,anew_ID,anew_description,anew_deadline):# adds an assignment to the assignment repo
        
        if self.constr_assignment(anew_ID,anew_description,anew_deadline) == False:
            
            return False
        anew=self.constr_assignment(anew_ID,anew_description,anew_deadline)
        self.assig_repo.addAssignment(anew)
        
        self.undo_controller.history.append(["addAssignment",anew])
        self.undo_controller.index+=1
        return True

    def give_to_one(self,a_id,s_id):# calls the give to one function from students repo
        self.s_repo.assign_to_one(a_id,s_id)

        self.undo_controller.history.append(["assign_to_one",[a_id,s_id]])
        self.undo_controller.index+=1

    def give_to_group(self,a_id,group):# calls the give to group function from students repo
        self.s_repo.assign_to_many(a_id,group)

        self.undo_controller.history.append(["assign_to_many",[a_id,group]])
        self.undo_controller.index+=1

    def assignment_by_id(self,assig_id):# calls the assignments by ID function from assignments repo
        return self.assig_repo.assignment_by_id(assig_id)

    def constr_grade(self,grade,s_id,assig_id):# builds a grade object
        return Grade(assig_id,s_id,grade)

    def grade_assignment(self,s_id,a_id):# calls the grade assignment function from the student repo
        self.s_repo.grade_assignment(s_id,a_id)

        self.undo_controller.history.append(["grade_assignment",[s_id,a_id]])
        self.undo_controller.index+=1



    def add_grade(self,grd):# adds a grade object in the grade repo
        self.grd_repo.add_grade(grd)

        self.undo_controller.history.append(["add_grade",[grd]])
        self.undo_controller.index+=1

    def late_students(self): # returns a list of students who were late with their assignments
        assignments_passed=self.assig_repo.passed_assigments()
        students_lte=[]
        
        for i in assignments_passed:
            students_lte=students_lte + self.s_repo.students_late(i)
        
        return set(students_lte)
        

    
    def custom_sort(self,t): # this is used as a sorting key,sorts the list of lists by the last element in the nested list 
        return t[-1]
    
    
    
    
    def best_students(self):# returns a list of students sorted by their best average grade received for all assignments
        grades=self.grd_repo.get_grades()
        groups=defaultdict(list)

        for grade in grades:
            groups[grade.get_studentID()].append(grade)

        grouped_list=list(groups.values())
        

        for i in range(len(grouped_list)):
            s=0
            l=0
            
            for j in range (len(grouped_list[i])):
                s=s+grouped_list[i][j].get_grade()
                l+=1
            
            s=s/l
            grouped_list[i].append(copy.deepcopy(s))
        
        
        sorted_grouped_list=sorted(grouped_list,key=self.custom_sort,reverse=True)
        ranking=[]

        for i in range(len(sorted_grouped_list)):
            ranking.append(sorted_grouped_list[i][0].get_studentID())


        stndts=self.s_repo.get_students()

        ranking_names=[]

        for r in ranking:
            for i in stndts:
                if i.get_studentID()==r:
                    ranking_names.append(i.get_name())




       
        return ranking_names




    def ordered_groups(self):
        # list of groups ordered by the number of lab problems received with average <7
        # do the average for every assignment
        # count  only the  assignments from that group that <7 in a group and put it into a count
        # sort the groups by that count


        grades=self.grd_repo.get_grades()
        groups=defaultdict(list)

        for grade in grades:
            groups[grade.get_assignmentID()].append(grade)

        grouped_list=list(groups.values()) 

        for i in range(len(grouped_list)):
            a=0
            l=0
            
            for j in range (len(grouped_list[i])):
                a=a+grouped_list[i][j].get_grade()
                l+=1
            
            a=a/l
            grouped_list[i].append(copy.deepcopy(a))

        assignments_with_average=[]  #here are stored assignments with their afferent average, as a list with 2 parameters, one being the assignment one being the average
        el=[]

        for i in range(len(grouped_list)):
            el.clear()
            el.append(grouped_list[i][0].get_assignmentID())
            el.append(grouped_list[i][-1])
            assignments_with_average.append(copy.deepcopy(el))

        stndts=self.s_repo.get_students()

        groups2=defaultdict(list)

        for s in stndts:
            groups2[s.get_group()].append(s)

        grouped_list2=list(groups2.values()) #students grouped by group

        for i in range(len(grouped_list2)):
            cont=0
            for j in range (len(grouped_list2[i])):
                stud=grouped_list2[i][j]
                for d in stud.assignments_owned:
                    assi= d.get_assignmentID() # it's get_assignments_owned()
                    for x in range(len(assignments_with_average)):
                        if assi == assignments_with_average[x][0]:
                            if int(assignments_with_average[x][1])<7:
                                cont+=1
                                

            grouped_list2[i].append(copy.deepcopy(cont))
        
        sorted_grouped_list=sorted(grouped_list2,key=self.custom_sort,reverse=True)

        ranking=[]

        for i in range(len(sorted_grouped_list)):
            ranking.append("Group "+str(sorted_grouped_list[i][0].get_group()))

        return ranking



    def students_assignments_grades(self,a_id):  #returns a list of students sorted by a grade for a specific assignment
        grades=self.grd_repo.get_grades()
        students_and_grades=[]

        for g in grades:
            if g.get_assignmentID() == a_id:
                students_and_grades.append(g)
        
        
        
        students_by_rank=[]
        el=[]

        for grade in students_and_grades:
            el.clear()
            el.append(grade.get_studentID())
            el.append(grade.get_grade())
            students_by_rank.append(copy.deepcopy(el))

        students_by_rank_sorted=sorted(students_by_rank,key=self.custom_sort,reverse=True)
        ranking=[]

        for s in students_by_rank_sorted:
            ranking.append("Student with the ID "+str(s[0]))
       
        return ranking

    def so_random(self,number):
        conts=int(10)
        conta=int(10)
        number=int(number)

        while number !=0:
            number-=1
            
            
            
            
            
            supdate=Student(4,"Randi",5,1)
            aupdate=Assignment(3,"Assignment Random",datetime.date(2019,11,16))

            
            op= random.randint(1,7)

            if op==1:
                conts+=1
                snew=Student(conts,"Randy",4,1)
                self.s_repo.addStudent(snew)
                print("Student "+ str(snew.get_name()) + " was added to the list! ")
            elif op==2:
                conts-=1
                rmvs=random.randint(1,conts+1)
                self.s_repo.removeStudent(rmvs)
                print("Student with the ID "+ str(rmvs) +" was removed from the list! ")
            elif op==3:
                self.s_repo.updateStudent(supdate)
                print("Student with the ID 4 was updated! ")
            elif op==4:
                conta+=1
                anew=Assignment(conta,"Assignment Randomly Generated",datetime.date(2021,11,16))
                self.assig_repo.addAssignment(anew)
                print("Assignment "+ str(conta) + "was added to the list! ")

            elif op==5:
                conta-=1
                rmva=random.randint(1,conta+1)
                self.assig_repo.removeAssignment(rmva)
                print("Assignment with the ID "+ str(rmva) +" was removed from the list! ")
            elif op==6:
                self.assig_repo.updateAssignment(aupdate)
                print("Assignment with the ID 3 was updated! ")








        
                
            





        

       










        

     


        


    

    




    

