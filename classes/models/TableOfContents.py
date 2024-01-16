from classes.models.Element import Element


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
    