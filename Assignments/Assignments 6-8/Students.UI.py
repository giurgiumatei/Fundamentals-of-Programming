from Repository import Student_Inventory
from Domain import *
import Services


class Students_UI:
    def __init__(self,repo,service):
        self.repo=repo
        self.service=service

    def menu(self):
        
        
        while True:
                
            while True:
                try:
                    op=input("Give a command: ")
                    assert op=="Add" or op=="Remove" or op=="Update" or op=="List" or op=="0"
                    break
                except:
                    print("Bad command!")

            if op=="0":
                break
            elif op=="Add":
                snew=self.service.constr_student()
                if self.service.validate_student(snew):
                    self.repo.addStudent(snew)
                else: print("Bad input!")


            elif op=="Remove":
                s_id=input("Give the ID of the student you want to be removed: ")
                
                if self.repo.is_in_list(s_id) == False:
                    print("ID not found in the current list! ")
                else: self.repo.removeStudent(s_id)


            elif op=="Update":
                s_id=input("Give the ID of the student you want to be updated: ")
                if self.repo.is_in_list(s_id) == False:
                    print("ID not found in the current list! ")
                else: 
                    self.repo.updateStudent(s_id)

            
            
            
            elif op=="List":
                self.repo.listStudents()