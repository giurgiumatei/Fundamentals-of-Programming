from Domain import *



class UndoController:


    def __init__(self,s_repo,assig_repo,grd_repo):
        #History of the program's undoable operations
        self.history=[]
        #keep the position in the undo/redo list
        self.index=0

        self.duringUndo=False

        self.s_repo=s_repo
        self.assig_repo=assig_repo
        self.grd_repo=grd_repo
        


    

    
    def undo_fct(self,funct_name,params):

        if funct_name=="addStudent" or funct_name=="addStudent_2":
            self.s_repo.removeStudent(params.get_studentID())

        elif funct_name=="removeStudent":
            self.s_repo.addStudent(params)

        elif funct_name=="updateStudent":
            self.s_repo.updateStudent(params[0])

        elif funct_name=="addAssignment":
            self.assig_repo.removeAssignment(params.get_assignmentID())
        elif funct_name=="removeAssignment":
            self.assig_repo.addAssignment(params)

        elif funct_name=="updateAssignment":
            self.assig_repo.updateAssignment(params[0])
        elif funct_name=="assign_to_one":
            self.s_repo.pop_from_one(params[1])
        elif funct_name=="assign_to_many":
            self.s_repo.pop_from_one(params[1])
        elif funct_name=="grade_assignment":
            self.s_repo.ungrade_assignment(params[0],params[1])
        elif funct_name=="add_grade":
            self.grd_repo.remove_grade()
        

    def redo_fct(self,funct_name,params):

        if funct_name=="addStudent" or funct_name=="addStudent_2":
            self.s_repo.addStudent(params)
            

        elif funct_name=="removeStudent":
            self.s_repo.removeStudent(self.s_repo.students[-1].get_studentID())

        elif funct_name=="updateStudent":
            self.s_repo.updateStudent(params[1])

        elif funct_name=="addAssignment":
            self.assig_repo.addAssignment(params)

        elif funct_name=="removeAssignment":
            self.assig_repo.removeAssignment(self.assig_repo[-1].get_assignmentID())
        elif funct_name=="updateAssignment":
            self.assig_repo.updateAssignment(params[1])
        elif funct_name=="assign_to_one":
            self.s_repo.assign_to_one(params[0],params[1])
        elif funct_name=="assign_to_many":
            self.s_repo.assign_to_many(params[0],params[1])
        elif funct_name=="grade_assignment":
            self.s_repo.grade_assignment(params[0],params[1])
        elif funct_name=="add_grade":
            self.grd_repo.add_grade(params[0])






    def undo(self):
        if self.index == 0:
            raise ValueError("No more undos! ")
        self._duringUndo=True
        
        
        self.undo_fct(self.history[self.index-1][0],self.history[self.index-1][1])
        self.index-=1
        self._duringRedo=False



        

    def redo(self):
        if self.index==len(self.history):
            raise ValueError("No more redos! ")
        self.duringRedo=True
        self.redo_fct(self.history[self.index-1][0],self.history[self.index-1][1])
        self.index+=1
        self.duringRedo= False

