class Rectangle:
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.h * 2 + self.w * 2

class Square:
    def __init__(self, w) -> None:
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.w * 4
    def change_size(self, w) -> None:
        self.w = w

s = Square(3)
s.change_size(4)
print(s.cacculate_perimeter())
