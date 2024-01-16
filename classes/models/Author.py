class Author():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def printAuthor(self):
        print("Author: " + self.name + " " + self.surname)