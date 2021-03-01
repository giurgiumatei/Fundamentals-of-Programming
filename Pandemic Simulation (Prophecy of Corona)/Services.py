
class service:

    def __init__(self,p_repo):
        self.p_repo=p_repo


    def get_persons(self):
        return self.p_repo.get_persons()

    def infect(self):#look specifications

        persons=self.p_repo.get_persons()
        counter=0 #check if there are ill persons

        for p in persons: #search for them
            if p.get_status()=='ill':
                counter=1
                

        if counter==0:
            return 0

        for p in persons: # if healthy become ill
            if p.get_immune_status()!='vaccinated':
                if p.get_status()=='healthy':
                    p.set_status('ill')
                    print("Infected")
                    self.p_repo.set_persons(persons)
                    
                    return 1 #exit after spreading plague
        

    def simulate(self):# simulate the day

        persons=self.p_repo.get_persons() # get persons list

        for p in persons:#look in the persons list
            p.set_cont(int(p.get_cont()-1))# decrease the day counter

            if p.get_cont()==0:
                p.set_status('healthy') # set status to healthy

        self.p_repo.set_persons(persons)

        return 1

    def vaccinate(self,value):

        persons=self.p_repo.get_persons()

        for p in persons:
            if p.get_id()==value:

                if p.get_status()=='healthy':
                    p.set_immune_status('vaccinated')
                    self.p_repo.set_persons(persons)

                    return 1

        return 0

            



