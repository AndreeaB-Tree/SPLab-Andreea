from abc import ABC, abstractmethod 

class Element(ABC):
    @abstractmethod
    def printElement(self):
        pass

    @abstractmethod
    def addElement(self):
        pass

    @abstractmethod
    def removeElement(self):
        pass

    @abstractmethod
    def getElement(self):
        pass

class Author:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def printAuthor(self):
        print("Author = " + self.name + " " + self.surname)

class Section(Element):
    def __init__(self, title) -> None:
        self.title = title
        self.elements = []
    
    def printElement(self):
        print("Section = " + self.title)

    def addElement(self, element):
        self.elements.append(element)

    def removeElement(self, element):
        self.elements.remove(element)

    def getElement(self):
        pass
        

class Book(Section):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.authors = []

    def printBook(self):
        print("Title = " + self.title)
        if len(self.authors) > 0:
            for author in self.authors:
                author.printAuthor()

    def addAuthor(self, author):
        self.authors.append(author)

from abc import ABC, abstractmethod 


class Element(ABC):
    @abstractmethod
    def printElement(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get(self):
        pass
    


class Author:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def printAuthor(self):
        print("Author: " + self.name + " " + self.surname)



class Section(Element):
    def __init__(self, title) -> None:
        self.title = title
        self.elements = []
    
    def printElement(self):
        print("\nSection: " + self.title)
        for element in self.elements:
            element.printElement()

    def add(self, element):
        self.elements.append(element)

    def remove(self, element):
        self.elements.remove(element)

    def get(self):
        pass
        


class Book(Section):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.authors = []
        self.contents = []

    def printBook(self):
        print("\n-> Book: " + self.title + "\n")
        if len(self.authors) > 0:
            print("\n- Authors: ")
            for author in self.authors:
                author.printAuthor()

            print("\n\n- Content: ")
            for content in self.contents:
                content.printElement()
            print("\n")

    def addAuthor(self, author):
        self.authors.append(author)

    def addContent(self, content):
        self.contents.append(content)




class TableOfContents(Element):
    def __init__(self, somethingTableOfContents) -> None:
        self.somethingTableOfContents = somethingTableOfContents

    def printElement(self):
        print("TableOfContents: " + self.somethingTableOfContents)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    



class Paragraph(Element):
    def __init__(self, text) -> None:
        self.text = text
    
    def printElement(self):
        print("Paragraph: " + self.text)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    

class Image(Element):
    def __init__(self, url) -> None:
        self.url = url

    def printElement(self):
        print("Image with name: " + self.url)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    

class Table(Element):
    def __init__(self, somethingTable) -> None:
        self.somethingTable = somethingTable

    def printElement(self):
        print("Table: " + self.somethingTable)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    



carte = Book("Noapte buna!")
autor = Author("Ana", "Blandiana")
autor2 = Author("Cristian Tudor", "Popescu")

carte.addAuthor(autor)
carte.addAuthor(autor2)


capitolul1 = Section("Capitolul 1")
capitolul11 = Section("Capitolul 1.1")
capitolul111 = Section("Capitolul 1.1.1")
capitolul1111 = Section("Capitolul 1.1.1.1")


carte.addContent(Paragraph("Multumesc celor care..."))
carte.addContent(capitolul1)

capitolul1.add(Paragraph("Moto capitol"))
capitolul1.add(capitolul11)

capitolul11.add(Paragraph("Text from subchapter 1.1"))
capitolul11.add(capitolul111)

capitolul111.add(Paragraph("Text from subchapter 1.1.1"))
capitolul111.add(capitolul1111)

capitolul1111.add(Image("Image from subchapter 1.1.1.1"))


carte.printBook()