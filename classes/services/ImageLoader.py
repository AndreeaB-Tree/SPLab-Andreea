from abc import ABC, abstractmethod 


class ImageLoader(ABC):
    @abstractmethod
    def load(self, string):
        pass