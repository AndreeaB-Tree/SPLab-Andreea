from classes.models.Element import Element


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

    def get(self, index):
        return self.elements[index]