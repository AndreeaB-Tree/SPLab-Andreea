from classes.Book import Book
from classes.Author import Author
from classes.Section import Section
from classes.Paragraph import Paragraph
from classes.Image import Image






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