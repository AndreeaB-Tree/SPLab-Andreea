from classes.Element import Element
from classes.Picture import Picture
from classes.Image import Image


class ImageProxy(Element, Picture):
    def __init__(self, url) -> None:
        self.url = url
        self.dim = ""
        self.loadImage()


    def printElement(self):
        print("Image Proxy with name: " + self.url)


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


    def loadImage(self):
        Image(self.url)
    

