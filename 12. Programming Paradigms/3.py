import math

class Triangle:
    def __init__(self, h, b) -> None:
        self.h = h
        self.b = b
    def area(self) -> float:
        return self.h * self.b / 2

t = Triangle(3, 4)
print(t.area())
