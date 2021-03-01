from Domain import *



class bus_repo:

    
    def construct_bus(self,line):

        b_id=line[0]
        b_rcode=line[1]
        b_model=line[2]
        b_times=line[3]

        b=bus(b_id,b_rcode,b_model,b_times)
        return b

    
    
    
    def __init__(self):

        self.bus_list=[]

        with open ("D:\FP\Exercitiu pentru test\Busses.txt","r") as f:

            reader=f.readline()
            reader=reader.strip("\n")
            reader=reader.strip()
            line=reader.split(",")
            bnew=self.construct_bus(line)
            self.bus_list.append(bnew)

            while reader:
                reader=f.readline()
                if reader!="":
                    reader=reader.strip("\n")
                    reader=reader.strip()
                    line=reader.split(",")
                    bnew=self.construct_bus(line)
                    self.bus_list.append(bnew)


    def get_busses(self):

        return self.bus_list



class buss_routes_repo:



    def construct_bus_route(self,line):

        rcode=line[0]
        lenght=line[1]
        r=bus_route(rcode,lenght)
        return r



    def __init__(self):

        self.bus_routes_list=[]

        with open ("D:\FP\Exercitiu pentru test\Bus Routes.txt","r") as f:

            reader=f.readline()
            reader=reader.strip("\n")
            reader=reader.strip()
            line=reader.split(",")
            bnew=self.construct_bus_route(line)
            self.bus_routes_list.append(bnew)

            while reader:
                reader=f.readline()
                if reader!="":
                    reader=reader.strip("\n")
                    reader=reader.strip()
                    line=reader.split(",")
                    bnew=self.construct_bus_route(line)
                    self.bus_routes_list.append(bnew)


    def get_routes(self):
        return self.bus_routes_list



    




