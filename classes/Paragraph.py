from classes.Element import Element

class Paragraph(Element):
    def __init__(self, text) -> None:
        self.text = text

    def print(self):
        print("Paragraph: " + self.text)