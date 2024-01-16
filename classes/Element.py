from abc import ABC, abstractmethod 


class Element(ABC):
    @abstractmethod
    def print(self):
        pass
