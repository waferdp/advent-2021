import unittest
from unittest.case import expectedFailure

class testVec3(unittest.TestCase):
    def testRotateX(self):
        point = vec3(1, 2, 3)
        expected = vec3(1, -3 ,2)
        rotated = point.rotate('x')
        assert(rotated == expected)

    def testRotateY(self):
        point = vec3(1, 2, 3)
        expected = vec3(3, 2 ,-1)
        rotated = point.rotate('y')
        assert(rotated == expected)

    def testRotateZ(self):
        point = vec3(1, 2, 3)
        expected = vec3(-2, 1, 3)
        rotated = point.rotate('z')
        assert(rotated == expected)

    def testTriple(self):
        point = vec3(1, 2, 3)
        expected = vec3(2, -1, 3)
        rotated = point.rotateMany(['z','z','z'])
        assert(rotated == expected)
class vec3:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z 
    
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other:object):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other:object):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __hash__(self) -> int:
        return hash(str(self))

    def rotate(self, axis):
        new = vec3(self.x, self.y, self.z)
        new.__rotateInplace(axis)
        return new

    def rotateMany(self, rotations):
        new = vec3(self.x, self.y, self.z)
        for rotation in rotations:
            new.__rotateInplace(rotation)
        return new
    
    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __rotateInplace(self, axis):
        if axis == 'x':
            temp = self.y
            self.y = self.z * -1
            self.z = temp
        elif axis == 'y':
            temp = self.x
            self.x = self.z
            self.z = temp * -1
        elif axis == 'z':
            temp = self.x
            self.x = self.y * -1
            self.y = temp

if __name__ == '__main__':
    unittest.main()