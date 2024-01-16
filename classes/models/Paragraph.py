from classes.models.Element import Element
from classes.models.AlignLeft import AlignLeft


class Paragraph(Element):
    def __init__(self, text) -> None:
        self.text = text
        self.textAlignment = AlignLeft()
    
    def printElement(self):
        self.textAlignment.render(self.text, "")

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass

    def setAlignStrategy(self, align):
        self.textAlignment = align