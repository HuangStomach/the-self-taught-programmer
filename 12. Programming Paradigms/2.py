import math

class Circle:
    def __init__(self, d) -> None:
        self.d = d
    def area(self) -> float:
        return math.pi * self.d * self.d

c = Circle(2)
print(c.area())
