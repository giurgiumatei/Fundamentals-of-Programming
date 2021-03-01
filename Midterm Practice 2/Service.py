from Repository import *

class service:

    def __init__(self,songs_repo):
        self.songs_repo=songs_repo


    def cautare(self,nume):
        list=[]
        songs=self.songs_repo.get_songs()

        for s in songs:
            if s.get_name()==nume:
                list.append(s)
        
        return list

    def get_songs(self):

        return self.songs_repo.get_songs()



    