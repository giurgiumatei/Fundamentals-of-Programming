

class Student:


    def __init__(self,s_id,s_name,s_group,graded):
        self.id=s_id
        self.name=s_name
        self.group=s_group
        self.graded=0
        self.laboratories=[]
        self.problems=[]


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_group(self):
        return self.group

    

    def get_laboratories(self):
        return self.laboratories
    
    def get_problems(self):
        return self.problems
    
    def add_laboratories(self,l):
        self.laboratories.append(l)
    
    def add_problems(self,p):
        self.problems.append(p)
    
    def get_graded(self):
        return self.graded



class Assignment:

    def __init__(self,lab,problem):
        self.lab=lab
        self.problem=problem
        


    
    def get_lab(self):
        return self.lab

    def get_problem(self):
        return self.problem



class Grade:


    def __init__(self,student,mark):
        self.student=student
        self.mark=mark

    def get_student(self):
        return self.student

    def get_mark(self):
        return self.mark

