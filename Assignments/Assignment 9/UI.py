
from Domain import *
import Services


#UI module
class repoUI:


    def option(self):

        print("Which repository do you want to use? ")
        print("1.Normal Repository; ")
        print("2.Text File Repository; ")
        print("3.Pickle Repository")

        op=input()

        if op=='1':
            return 1
        elif op=='2':
            return 2
        elif op=='3':
            return 3
        else:
            print("Invalid Input! ")
            self.option()







class UI: #UI class, contains  every prints in this program
    


    def __init__(self,service):
        
        self.service=service
        self.e=error_asserts()

    

    def print_menu(self):
        print("Which of the following options do you want to use? ")
        print("'1' - Manage the list of students: ")
        print("'2' - Manage the list of assignments: ")
        print("'3' - Give assignments to a student or to a group of students: ")
        print("'4' - Grade students for a given assignment: ")
        print("'5' - Statistics: ")
        print("'6' - Random Operations: ")
    
    def menu(self):
        
        while True:
            while True:
                self.print_menu()
                try:
                    opt=input()
                    assert opt=="1" or opt=="2" or opt=="3" or opt=="0" or opt=="4" or opt=="5" or opt=="Undo" or opt=="Redo" or opt=="6"
                    break
                except:
                    print("Bad command!")
            if opt=="0":
                break
            elif opt=="1":
                
                self.student_menu()
            elif opt=='2':
                self.assignment_menu()
            elif opt=='3':
                self.Assign_Assignments()
            elif opt=='4':
                self.Grade_Assignments()
            elif opt=='5':
                self.Statistics()
            elif opt=="Undo":
                try:
                    self.service.undo_controller.undo()
                except:
                    print("No more Undos! ")
            elif opt=="Redo":
                try:
                    self.service.undo_controller.redo()
                except:
                    print("No more Redos! ")

            elif opt=="6":
                self.random_operations()

            
        
    def random_operations(self):
        nr=input("Give the number of random operations you want to be made: ")
        self.service.so_random(nr)


    
  

    def student_menu(self):
        
        
        while True:
            
            while True:
                try:
                    op=input("'Add' , 'Remove' ,'Update' , 'List' or Add_2 ?")
                    assert op=="Add" or op=="Remove" or op=="Update" or op=="List" or op=="0" or op=="Add_2"
                    break
                except:
                    print("Bad command!")

            if op=="0":
                break
            elif op=="Add":
                
                while True:
                    #try:
                    snew_ID=input("Give an ID for the new student: ")
                    snew_Name=input("Give a name for the new student: ")
                    snew_Group=input("Give the group for the new student: ")
                    assert self.service.add_student(snew_ID,snew_Name,snew_Group) == True
                    break
                    #except:self.e.bad_imput_error()
                        
                



            elif op=="Remove":
                

                while True:
                    try:
                        s_id=input("Give the ID of the student you want to be removed: ")
                        assert self.service.is_in_list_student(s_id) == True
                        break
                    except:self.e.bad_imput_error()
                self.service.remove_student(s_id)
                
                
                   
            elif op=="Update":
                
                
                while True:
                    try:
                        s_id=input("Give the ID of the student you want to be updated: ")
                        assert self.service.is_in_list_student(s_id) == True
                        break
                    except:self.e.bad_imput_error()
                
                
                while True:
                    try:
                
                        snew_Name=input("Give a name for the new student: ")
                        snew_Group=input("Give the group for the new student: ")
                        assert self.service.validate_student(s_id,snew_Name,snew_Group)
                        break
                    except:self.e.bad_imput_error()
                
                self.service.update_student(s_id,snew_Name,snew_Group)

            
            elif op=="Add_2":
                while True:
                    try:
                        snew_ID=input("Give an ID for the new student: ")
                        snew_Name=input("Give a name for the new student: ")
                        snew_Group=input("Give the group for the new student: ")
                        assert self.service.validate_student(snew_ID,snew_Name,snew_Group)== True
                        break
                    except:self.e.bad_imput_error()

                self.service.add_student2(snew_ID,snew_Name,snew_Group)

                
            elif op=="List":
                self.service.listStudents()
    
    
    
    def assignment_menu(self):
        
        while True:
            
            while True:
                try:
                    op=input("'Add' , 'Remove' ,'Update' or 'List' ?")
                    assert op=="Add" or op=="Remove" or op=="Update" or op=="List" or op=="0"
                    break
                except:
                    print("Bad command!")

            if op=="0":
                break
            elif op=="Add":
                while True:
                    try:
                        anew_ID=input("Give an ID for the new assignment: ")
                        anew_description=input("Give a description for this assignment: ")
                        anew_deadline=input("Give a deadline for this assignment: ")
                        assert self.service.add_assignment(anew_ID,anew_description,anew_deadline)
                        break
                    except:self.e.bad_imput_error()
                




            elif op=="Remove":
                
                
                while True:
                    try:
                        a_id=input("Give the ID of the assignment you want to be removed: ")
                        assert self.service.is_in_list_assignment(a_id) == True
                        break
                    except: self.e.bad_imput_error()
                self.service.remove_assignment(a_id)


            elif op=="Update":
                
                
                while True:
                    try:
                        a_id=input("Give the ID of the assignment you want to be updated: ")
                        assert self.service.is_in_list_assignment(a_id) == True
                        break
                    except:self.e.bad_imput_error()

                while True:
                    try:
                        anew_description=input("Give a description for this ID: ")
                        anew_deadline=input("Give a deadline for this assignment: ")
                        assert self.service.validate_assignment(a_id,anew_description,anew_deadline)
                        break
                    except:self.e.bad_imput_error()
                self.service.update_assignment(a_id,anew_description,anew_deadline)
                        

            
            elif op=="List":
                self.service.listAssignments()

   
   
   
    def Assign_Assignments(self):
        while True:
            try:
                a_id=input("Which assignment do you want to distribute ")
                assert self.service.is_in_list_assignment(a_id)
                break
            except:self.e.non_existent_assignment_error()
        
        assig=self.service.assignment_by_id(a_id)
                
        
        while True:
            try:
                op=input("Give assignment to one or to a group of students? ")
                assert op == "One" or op == "Group"
                break
            except:
                print("Bad input! ")
        if op == "One":
            while True:
                try:
                    s_id=input("Which student do you want to receive the assignment (give the ID): ")
                    assert self.service.is_in_list_student(s_id) == True
                    break
                except:self.e.non_existent_student_error()
            self.service.give_to_one(assig,s_id)
        elif op == "Group":
            while True:
                try:
                    grp=input("Which group do you want to receive the assignment (give only the number of the group): ")
                    
                    break
                except:self.e.non_existent_group_error()
            self.service.give_to_group(assig,grp)
        self.service.list_students_assignments()



    def Grade_Assignments(self):
        
        while True:
            try:
                grade=int(input("Give the grade for the assignment: "))
                assert grade<=10 and grade>=1
                break
            except:self.e.bad_imput_error()

        while True:
            try:
                s_id=input("Give the ID of the student you want to be graded: ")
                assert self.service.is_in_list_student(s_id) == True
                break
            except:self.e.non_existent_student_error()
        
        ug_assignments=self.service.list_ungraded_assignments(s_id)
        

        while True:
            try:

                strn=" "
                for x in ug_assignments:
                    strn=strn+ " " + x.get_assignmentID()
                
                print("This student have the following assignments: ")
                print(strn)
                a_id=input("Give the ID of the assigment you want to be graded: ")
                assert self.service.is_in_list_assignment(a_id)
                break
            except:self.e.non_existent_assignment_error()
        
        self.service.grade_assignment(s_id,a_id)
        grd=self.service.constr_grade(grade,s_id,a_id)
        print("Student with the ID "+str(grd.get_studentID()) + " and assignment " +str(grd.get_assignmentID()) + "- grade " + str(grd.get_grade()))
        self.service.add_grade(grd)


    def Statistics(self):

        while True:
            
            while True:
                try:
                    op=input("Which statistics do you want (give option 1,2,3 or 4): ")
                    assert op=="1" or op=="2" or op=="3" or op=="0" or op=="4"
                    break
                except:self.e.bad_command_error()

            if op=="0":
                break
            elif op=="2":
                print(self.service.late_students())
            elif op=="0":
                break
            elif op=="3":
                print(self.service.best_students())
            elif op=="4":
                print(self.service.ordered_groups())
            elif op=="1":
                while True:
                    try:

                        a_id=input("Give the ID of the assigment you want to be used as a sorting crieria: ")
                        assert self.service.is_in_list_assignment(a_id)
                        break
                    except:self.e.non_existent_assignment_error()



                print(self.service.students_assignments_grades(a_id))
        




                    


        







                    
                    
            
            
            
        


    


class error_asserts:
    def bad_imput_error(self):
        print("Bad imput! ")
    def bad_command_error(self):
        print("Bad command! ")
    def non_existent_student_error(self):
        print("This student does not currently exist! ")
    def non_existent_assignment_error(self):
        print("This assignment does not currently exist! ")
    def non_existent_group_error(self):
        print("This group does not currently exist! ")









