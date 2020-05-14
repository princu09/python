# from abc import ABCMeta , abstractmethod
from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

class Squre(Shape):
    def __init__(self):
        self.length = 5
        self.breadth = 8

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
sq = Squre()
print(rect1.printarea())
print(sq.printarea())

print("\nFor learn how to run and access abstract base class method , open this file in your editor and learn about this file")
print("\nThank You\n")