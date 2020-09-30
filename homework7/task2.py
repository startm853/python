from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return round(self.materials() + other.materials(), 2)

    @abstractmethod
    def materials(self):
        pass


class Coats(Clothes):
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 10:
            self.__size = 10
        elif size > 100:
            self.__size = 100
        else:
            self.__size = size

    def materials(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 20:
            self.__size = 20
        elif size > 50:
            self.__size = 50
        else:
            self.__size = size

    def materials(self):
        return round(self.size * 2 + 0.3, 2)


item1 = Coats(5)
print(item1.materials())
item2 = Costume(17)
print(item2.materials())

print(Coats(5) + Costume(25))
print(Costume(69) + Coats(70))
