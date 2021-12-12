class Point2d:
    x = 0
    y = 0
    value = 0

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __init__(self, x , y, value = 1) -> None:
        self.x = x
        self.y = y
        self.value = value

    def __str__(self) -> str:
        return str(self.x) + ", " + str(self.y)

    def __repr__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"