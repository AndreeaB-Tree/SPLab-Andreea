from classes.Chapter import Chapter


class Book():
    def __init__(self, title) -> None:
        self.title = title
        self.authors = []
        self.chapters = []


    def printBook(self):
        print("-Book-")
        print("\nTitle: " + self.title)

        print("\nAuthors: ")
        for author in self.authors:
            author.printAuthor()

        print("\nChapters: ")
        for chapter in self.chapters:
            chapter.printChapter()


    def addAuthor(self, author):
        self.authors.append(author)
        

    def addChapter(self, title):
        self.chapters.append(Chapter(title))
        return len(self.chapters) - 1


    def getChapter(self, index):
        return self.chapters[index]