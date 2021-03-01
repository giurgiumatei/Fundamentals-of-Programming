from Domain import *



class Service:


    def __init__(self,student_repo,grade_repo):
        self.student_repo=student_repo
        self.grade_repo=grade_repo

    
    
    
    def validate_student(self,id,name,group):
        students=self.student_repo.get_students()

        for s in students:
            if s.get_id()==id:
                return False

        if len(name)==0:
            return False
        if len(group)==0:
            return False
        return True

    
    
    
    
    
    def add_student(self,id,name,group):

        if self.validate_student(id,name,group)==False:
            return False