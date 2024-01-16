from classes.Element import Element


class Image(Element):
    def __init__(self, url) -> None:
        self.url = url

    def printElement(self):
        print("Image with name: " + self.url)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    