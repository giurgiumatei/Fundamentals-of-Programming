from Domain import *


class Student_Repo:






    def create_student(self,line):
        id=line[0]
        name=line[1]
        group=line[2]
        graded=int(line[3])

        self.student=Student(id,name,group,graded)

        if len(line)>4:

            for i in range(4,len(line)):
                if i%2==0:
                    self.student.add_laboratories(line[i])
                else:self.student.add_problems(line[i])

        return self.student



    def deconstruct_student(self,student):

        id=student.get_id()
        name=student.get_name()
        group=student.get_group()
        graded=student.get_graded()
        self.string=str(id)+" "+str(name)+" "+str(group)+" "+str(graded)+" "
        laboratories=student.get_laboratories()
        problems=student.get_problems()
        if len(laboratories)>0:
            for j in range(len(laboratories)-1):
                self.string=self.string+str(laboratories[j])
                self.string=self.string+str(problems[j])

        return self.string
    






    def __init__(self):

        self.students=[]

        with open ("G:\FP\Antrenament\students.txt",'r') as f:
            line=f.readline()

            while line!='':
                line=line.strip("\n")
                line=line.strip(" ")
                line=line.split(',')
                self.student=self.create_student(line)
                self.students.append(self.student)
                line=f.readline()


    
    
    def write_to_file(self):

        with open ("G:\FP\Antrenament\students.txt",'w') as f:
            for i in self.students:

                s=self.deconstruct_student(i)
                f.write(s+"\n")


    def get_students(self):
        return self.students




class Grade_Repo:






    def create_grade(self,line):
        student=line[0]
        mark=int(line[1])
        self.grade=Grade(student,mark)

        return self.grade



    def deconstruct_grade(self,grade):

        student=grade.get_student()
        mark=str(grade.get_mark())
        
        self.string=str(student)+" "+str(mark)
        
        return self.string
    






    def __init__(self):

        self.grades=[]

        with open ("G:\FP\Antrenament\grades.txt",'r') as f:
            line=f.readline()

            while line!='':
                line=line.strip("\n")
                line=line.strip(" ")
                line=line.split(',')
                self.grade=self.create_grade(line)
                self.grades.append(self.grade)
                line=f.readline()


    
    
    def write_to_file(self):

        with open ("G:\FP\Antrenament\students.txt",'w') as f:
            for i in self.grades:

                s=self.deconstruct_grade(i)
                f.write(s+"\n")


    def get_students(self):
        return self.grades








                


