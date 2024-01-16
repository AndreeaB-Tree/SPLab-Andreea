from abc import ABC, abstractmethod 


class Element(ABC):
    @abstractmethod
    def printElement(self):
        pass

    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def remove(self, element):
        pass

    @abstractmethod
    def get(self, index):
        pass