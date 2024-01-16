from classes.ImageProxy import ImageProxy
from classes.Section import Section
from classes.Book import Book
import time


start_time = time.time()

img1 = ImageProxy("Pamela Anderson")
img2 = ImageProxy("Kim Kardashian")
img3 = ImageProxy("Kirby Griffin")

playboyS1 = Section("Front Cover")
playboyS1.add(img1)

playboyS2 = Section("Summer Girls")
playboyS2.add(img2)
playboyS2.add(img3)


playboy = Book("Playboy")
playboy.addContent(playboyS1)
playboy.addContent(playboyS2)

end_time = time.time()
print("Time: ", end_time - start_time)


start_time = time.time()
playboy.printBook()
end_time = time.time()
print("Time: ", end_time - start_time)
