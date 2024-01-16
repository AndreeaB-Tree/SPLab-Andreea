from classes.models.Element import Element
from classes.models.Picture import Picture
import time


class Image(Element, Picture):
    def __init__(self, url) -> None:
        time.sleep(1)
        self.url = url
        self.content = ""

    def printElement(self):
        print("Image with url: " + self.url)

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass
    
    def url(self):
        pass

    def dim(self):
        pass

    def content(self):
        pass