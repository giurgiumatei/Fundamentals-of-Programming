from Domain import *
from Service import *


class UI:

    def __init__(self,service):
        self.service=service

    def print_menu(self):
        print("1.Cautare; ")
        print("2.Afisare dupa gen. ")
    
    def start(self):
        
        while True:
            self.print_menu()
            opt=int(input())

            if opt==0:
                break
            elif opt==1:
                self.cautare()

            elif opt==2:
                self.afisare()


    def cautare(self):

        nume=input("Give the name of the song: ")
        songs=self.service.cautare(nume)

        for s in songs:
            print("Titlu: "+ str(s.get_name()) + '. Autor:' + str(s.get_author()) + ". Gen: " + str(s.get_genre()))

    def afisare(self):

        while True:
            try:
                song=int(input("Give the id of the song: "))
                break
            except:"The ID is invalid! "

        songs=self.service.get_songs()
        
        genre=""

        for s in songs:
            if s.get_id() == str(song):
                genre=s.get_genre()

        if genre=="":
            print("Song not in the list! ")
            return 0
        print("Genul cautat: "+str(genre))

        for s in songs:
            if s.get_genre()==genre:
                print("Titlu: "+ str(s.get_name()) + '. Autor:' + str(s.get_author()) + " (id " + str(s.get_id()) +")")


