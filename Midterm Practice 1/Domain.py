
class bus:

    def __init__(self,id,rcode,model,times):
        self.id=id
        self.rcode=rcode
        self.model=model
        self.times=times

    def get_id(self):
        return self.id
    def get_rcode(self):
        return self.rcode
    def get_model(self):
        return self.model
    def get_times(self):
        return self.times


class bus_route:

    def __init__(self,rcode,lenght):
        self.rcode=rcode
        self.lenght=lenght

    def get_rcode(self):
        return self.rcode

    def get_lenght(self):
        return self.lenght

