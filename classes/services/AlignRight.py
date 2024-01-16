from classes.AlignStrategy import AlignStrategy

class AlignRight(AlignStrategy):
    def __init__(self) -> None:
        return
    

    def render(self, paragraph, context):
        print("---------------", paragraph)