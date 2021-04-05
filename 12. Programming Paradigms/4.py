class Hexagon:
    def __init__(self, s) -> None:
        self.s = s
    def cacculate_perimeter(self) -> float:
        return self.s * 6

h = Hexagon(3, 4)
print(h.cacculate_perimeter())
