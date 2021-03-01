

class Song:

    def __init__(self,id,name,author,genre):
        self.id=id
        self.name=name
        self.author=author
        self.genre=genre

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
        