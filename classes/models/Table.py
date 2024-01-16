from classes.models.Element import Element


class Table(Element):
    def __init__(self, somethingTable) -> None:
        self.somethingTable = somethingTable

    def printElement(self):
        print("Table: " + self.somethingTable)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass