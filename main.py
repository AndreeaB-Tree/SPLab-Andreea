from classes.Book import Book



carte = Book("Padurea spanzuratilor")
chapter1 = carte.getChapter(carte.addChapter("I"))
chapter2 = carte.getChapter(carte.addChapter("II"))
chapter3 = carte.getChapter(carte.addChapter("III"))

chapter1.addSubchapter("1.")
chapter1.addSubchapter("2.")


chapter2.addSubchapter("1.")
chapter2.addSubchapter("2.")

chapter3.addSubchapter("1.")
chapter3.addSubchapter("2.")
chapter3.addSubchapter("3.")

carte.printBook()