from classes.Element import Element


class Image(Element):
    def __init__(self, url) -> None:
        self.url = url

    def print(self):
        print("Image: " + self.url)
