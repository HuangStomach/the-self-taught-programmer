class Rider:
    def __init__(self, name) -> None:
        self.name = name

class Horse:
    def __init__(self, name, rider) -> None:
        self.name = name
        self.rider = rider

r = Rider("john")
h = Horse("jack", r)

print(h.rider.name)
