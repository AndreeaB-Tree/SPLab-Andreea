from classes.models.Section import Section
from classes.models.Paragraph import Paragraph
from classes.models.AlignCenter import AlignCenter
from classes.models.AlignLeft import AlignLeft
from classes.models.AlignRight import AlignRight


cap1 = Section("Capitolul 1")
p1 = Paragraph("Paragraf 1")
p2 = Paragraph("Paragraf 2")
p3 = Paragraph("Paragraf 3")
p4 = Paragraph("Paragraf 4")

cap1.add(p1)
cap1.add(p2)
cap1.add(p3)
cap1.add(p4)

cap1.printElement()


p1.setAlignStrategy(AlignCenter())
p2.setAlignStrategy(AlignLeft())
p3.setAlignStrategy(AlignRight())


cap1.printElement()