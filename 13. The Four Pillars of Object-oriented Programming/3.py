class Shape:
    def __init__(self) -> None:
        pass
    def what_am_i(self) -> None:
        print("I am s shape")

class Rectangle(Shape):
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.h * 2 + self.w * 2

class Square(Shape):
    def __init__(self, w) -> None:
        self.w = w
    def cacculate_perimeter(self) -> float:
        return self.w * 4
    def change_size(self, w) -> None:
        self.w = w

r = Rectangle(3, 4)
s = Square(3)
print(r.what_am_i())
print(Shape.what_am_i())
