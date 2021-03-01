import datetime
#domain module,contains classes and hard-coded lists



class Student: #Student Class
    name_cont=int(1)
    
    def __init__(self,studentID,name,group,assignment_assigned):
        self.studentID=studentID
        self.name=name
        self.group=group
        self.assignments_owned=[]
        if assignment_assigned != "":
            self.assignments_owned.append(assignment_assigned)
        

    
    def get_studentID(self):
        return self.studentID

    
    def get_name(self):
        return self.name

   
    def get_group(self):
        return self.group

    def get_assigments_owned(self):
        return self.assignments_owned

    

    
        
  
    def set_studentID(self,value):
        self.studentID=value
    
   
    def set_name(self,value):
        self.name=value
    
    
    def set_group(self,value):
        self.group=value
    
    




class Assignment: # Student Class
    def __init__(self,assignmentID,description,deadline):
        self.assignmentID=assignmentID
        self.description=description
        self.deadline=str(deadline)
        self.isgraded=False
    
    
    def get_assignmentID(self):
        return self.assignmentID
    
    
    def get_description(self):
        return self.description
    
    
    def get_deadline(self):
        return self.deadline
    
    def get_isgraded(self):
        return self.isgraded

    
    def set_assignmentID(self,value):
        self.assignmentID=value
    
    
    def set_description(self,value):
        self.description=value
    
    
    def set_deadline(self,value):
        self.deadline=value

    def set_isgraded(self,value):
        self.isgraded=value
        




class Grade: # Grade Class
    def __init__(self,assignmentID,studentID,grade):
        self.assignmentID=assignmentID
        self.studentID=studentID
        self.grade=grade

    
    def get_assignmentID(self):
        return self.assignmentID

    
    def get_studentID(self):
        return self.studentID

    
    def get_grade(self):
        return self.grade
    
    
    def set_assignmentID(self,value):
        self.assignmentID=value

    
    def set_studentID(self,value):
        self.studentID=value

    
    def set_grade(self,value):
        self.grade=value





assig1=Assignment("1","Assignment 1",datetime.date(2019,11,16))
assig2=Assignment("2","Assignment 2",datetime.date(2019,11,17))
assig3=Assignment("3","Assignment 3",datetime.date(2019,12,15))
assig4=Assignment("4","Assignment 4",datetime.date(2019,12,26))
assig5=Assignment("5","Assignment 5",datetime.date(2019,12,31))






s1=Student("1","George","1",assig1)
s2=Student("2","Marian","1",assig1)
s3=Student("3","Vlad","1",assig2)
s4=Student("4","Matei","2",assig2)
s5=Student("5","Andrei","2",assig3)
s6=Student("6","Alex","2",assig3)
s7=Student("7","Marcel","3",assig4)
s8=Student("8","Edy","3",assig4)
s9=Student("9","Jean","3",assig5)
s10=Student("10","Cristian","4",assig5)



grade01=Grade("1","1",10)
grade02=Grade("2","1",2)
grade03=Grade("3","2",8)
grade04=Grade("4","2",8)
grade05=Grade("5","3",2)
grade06=Grade("2","3",10)
grade07=Grade("7","2","1")
grade08=Grade("8","3","1")
grade09=Grade("9","4","1")
grade10=Grade("10","5","10")

students=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
assignments=[assig1,assig2,assig3,assig4,assig5]
grades=[grade01,grade02,grade03,grade04,grade05,grade06]



