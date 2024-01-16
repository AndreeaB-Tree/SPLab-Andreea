class SingletonComponent():
    def __init__(self) -> None:
        print("SingletonComponent::SingletonComponent = " + str(id(self)))
        print("")

    def __str__(self) -> str:
        return "SingletonComponent@" + str(id(self))

    def operation(self) -> None:
        print("Invoked SingletonComponent::operation() on " + str(id(self)))
        print("")


class TransientComponent():
    def __init__(self) -> None:
        print("TransientComponent::TransientComponent = " + str(id(self)))
        print("")

    def __str__(self) -> str:
        return "TransientComponent@" + str(id(self))
    
    def operation(self) -> None:
        print("Invoked TransientComponent::operation() on " + str(id(self)))
        print("")




class ClientComponent():
    def __init__(self, tc, sc) -> None:
        self.tc = tc
        self.sc = sc

        print("ClientComponent::ClientComponent = " + str(id(self)))
        print(" o SingletonComponent = " + sc.__str__())
        print(" o TransientComponent = " + tc.__str__())
        print("")


    def __str__(self) -> str:
        return "ClientComponent@" + str(id(self))
    

    def operation(self) -> None:
        print("Invoked ClientComponent::operation() on " + str(id(self)))
        print(" o SingletonComponent = " + self.sc.__str__())
        print(" o TransientComponent = " + self.tc.__str__())
        print("")


