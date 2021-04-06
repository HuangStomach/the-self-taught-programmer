class Rectangle:
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.h * 2 + self.w * 2

class Square:
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.h * 2 + self.w * 2

r = Rectangle(3, 4)
s = Square(3, 4)
print(r.cacculate_perimeter())
print(s.cacculate_perimeter())
