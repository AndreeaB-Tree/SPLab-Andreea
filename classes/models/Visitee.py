from abc import ABC, abstractmethod 


class Visitee(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
