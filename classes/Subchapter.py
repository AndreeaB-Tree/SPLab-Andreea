from classes.Image import Image
from classes.Paragraph import Paragraph
from classes.Table import Table

class SubChapter():
    def __init__(self, name) -> None:
        self.name = name
        self.elements = []

    def printSubchapter(self):
        print("--Subchapter: " + self.name)
        for element in self.elements:
            element.print()


    def addImage(self, url):
        self.elements.append(Image(url))
        print("Image added successfully!")

    def addParagraph(self, text):
        self.elements.append(Paragraph(text))
        print("Paragraph added successfully!")

    def addTable(self, title):
        self.elements.append(Table(title))
        print("Table added successfully!")