from classes.Section import Section


class Book(Section):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.authors = []


    def printBook(self):
        print("\n-> Book: " + self.title + "\n")
        if len(self.authors) > 0:
            print("\n- Authors: ")
            for author in self.authors:
                author.printAuthor()

            print("\n\n- Content: ")
            super().printElement()


    def addAuthor(self, author):
        self.authors.append(author)

    def addContent(self, element):
        super().add(element)
