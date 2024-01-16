from abc import ABC, abstractmethod 


class Picture(ABC):
    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def dim(self):
        pass

    @abstractmethod
    def content(self):
        pass