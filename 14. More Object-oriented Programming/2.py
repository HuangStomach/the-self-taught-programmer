class Shape:
    def __init__(self) -> None:
        pass
    def what_am_i(self) -> None:
        print("I am s shape")

class Square(Shape):
    square_list = []
    def __init__(self, w) -> None:
        self.w = w
        self.square_list.append(self)
    def __repr__(self) -> str:
        return "{} by {} by {} by {}".format(self.w, self.w, self.w, self.w)
    def cacculate_perimeter(self) -> float:
        return self.w * 4
    def change_size(self, w) -> None:
        self.w = w

s = Square(3)
print(s)
