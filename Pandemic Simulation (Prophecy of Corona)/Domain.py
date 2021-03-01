
class Person:
    def __init__(self,id,immune_status,status):
        self.id=id
        self.immune_status=immune_status
        self.status=status
        self.cont=3
        

    def get_id(self):
        return self.id  
    def get_immune_status(self):
        return str(self.immune_status)

    def get_status(self):
        return str(self.status)

    def get_cont(self):
        return self.cont
    def set_cont(self,value):
        self.cont=value
    def set_status(self,value):
        self.cont=3
        self.status=value
    
    def set_immune_status(self,value):
        self.immune_status=value