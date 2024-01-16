from abc import ABC, abstractmethod 


class AlignStrategy(ABC):
    @abstractmethod
    def render(self, paragraph, context):
        pass
