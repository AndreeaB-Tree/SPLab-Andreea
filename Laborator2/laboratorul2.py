class Book():
    def __init__(self, title, authors, chapters) -> None:
        self.title = title
        self.authors = authors
        self.chapters = chapters

    def printBook(self):
        print("title = " + self.title)

class Author():
    def __init__(self, name) -> None:
        self.name = name
    
    def printAuthor(self):
        print("Author = " + self.name)


class TableOfContens():
    def __init__(self) -> None:
        pass

    def printTableContents(self):
        pass

class Chapter():
    def __init__(self, name, subChapters) -> None:
        self.name = name
        self.subChapters = subChapter

    def printChapter(self):
        print("Chapter = " + self.name)


class SubChapter():
    def __init__(self, name, images, paragraphs, tables) -> None:
        self.name = name
        self.images = images
        self.paragraphs = paragraphs
        self.tables = tables

    def printSubChapter(self):
        print("SubChapter = " + self.name)

class Image():
    def __init__(self, imageName) -> None:
        self.imageName = imageName

    def printImage(self):
        print("Image = " + self.imageName)

class Paragraph():
    def __init__(self, text) -> None:
        self.text = text

    def printParagraph(self):
        print("Paragraph = " + self.text)

class Table():
    def __init__(self, title) -> None:
        self.title = title
    
    def printTable(self):
        print("Table = " + self.title)

#component este Book composite este chapter
autor = Author("Liviu Rebreanu")
tabel = Table("Scrisoare")
imagine = Image("Portret")
paragraf = Paragraph("Numai când e singur omul cu sufletul său, numai atunci există un echilibru între lumea lui cea mică dinăuntru şi restul universului; îndată ce intervine realitatea de-afară, omul devine o jucărie neputincioasă, fără voinţă adevărată, mergând încotro îl mână puteri şi hotărâri străine de fiinţa lui...")
subcapitol = SubChapter("II", [imagine], [paragraf], [tabel])
capitol1 = Chapter("I", [subcapitol])
capitol2 = Chapter("II", [subcapitol])
carte = Book("Padurea spanzuratilor", autor, [capitol1, capitol2])

autor.printAuthor()