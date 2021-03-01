from Domain import *

class songs_repo:

    
    def construct_song(self,line):
        id=line[0]
        name=line[1]
        author=line[2]
        genre=line[3]

        sng=Song(id,name,author,genre)

        return sng
    
    
    def __init__(self):

        self.songs=[]

        with open ("G:\FP\Exercitiu pentru test 2\Piese.txt","r") as f:
            reader=f.readline()
            reader=reader.strip("\n")
            reader=reader.strip()
            line=reader.split(";")
            snew=self.construct_song(line)
            self.songs.append(snew)

            while reader:

                reader=f.readline()

                if reader!="":
                    reader=f.readline()
                    reader=reader.strip("\n")
                    reader=reader.strip()
                    line=reader.split(";")
                    snew=self.construct_song(line)
                    self.songs.append(snew)


    def get_songs(self):
        return self.songs



