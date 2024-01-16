from classes.Element import Element

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