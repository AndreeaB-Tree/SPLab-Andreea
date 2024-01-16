from classes.Element import Element


class Table(Element):
    def __init__(self, title) -> None:
        self.title = title
    
    def print(self):
        print("Table: " + self.title)
