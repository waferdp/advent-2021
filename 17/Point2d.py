import unittest
class TestPoint2d(unittest.TestCase):
    def testLte(self):
        a = Point2d(1,1)
        b = Point2d(2,2)
        c = Point2d(2,2)
        d = Point2d(3,2)
        assert(a <= b and b <= c)
        assert(not d <= c)

    def testGte(self):
        a = Point2d(1,1)
        b = Point2d(2,2)
        c = Point2d(2,2)
        d = Point2d(3,2)
        assert(c >= a and c >= b)
        assert(not c >= d)


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

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def copy(self):
        return Point2d(self.x, self.y, self.value)

if __name__ == '__main__':
    unittest.main()