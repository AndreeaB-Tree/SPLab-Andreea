from classes.Subchapter import SubChapter


class Chapter():
    def __init__(self, name) -> None:
        self.name = name
        self.subChapters = []

    def printChapter(self):
        print("\n-Chapter: " + self.name)

        for subChapter in self.subChapters:
            subChapter.printSubchapter()

    def addSubchapter(self, subTitle):
        self.subChapters.append(SubChapter(subTitle))

        return len(self.subChapters) - 1

    def getSubchapter(self, index):
        return self.subChapters[index]
