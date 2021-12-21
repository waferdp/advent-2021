from __future__ import annotations
import unittest
from Point2d import Point2d

class TestMatrix(unittest.TestCase):

    def testGenerate(self):
        matrix = Matrix.generate(11, 15)
        assert(matrix.width == 11 and matrix.height == 15)

    def testExists(self):
        matrix = Matrix.generate(11, 15)
        point = Point2d(6, 10)
        matrix.set(6, 10)
        assert(matrix.contains(point))

    def testPointify(self):
        matrix = Matrix.generate(5, 5)
        matrix.set(2, 2, 3)
        a = Point2d(2, 2, 3)
        b = matrix.pointify(2, 2)
        assert(a == b)

    def testPad(self):
        matrix = Matrix.generate(2, 2, 1)
        matrix.padMatrix(1, 0)
        assert(str(matrix) == '....\n.##.\n.##.\n....\n')

    def testGetSquare2(self):
        matrix = Matrix([[0,0,0],[0,0,0], [0,1,0]])
        value = matrix.getSquare(1,1)
        assert(value == 2)

    def testGetSquare4(self):
        matrix = Matrix([[0,0,0],[0,0,0], [1,0,0]])
        value = matrix.getSquare(1,1)
        assert(value == 4)

    def testGetSquare16(self):
        matrix = Matrix([[0,0,0],[0,1,0], [0,0,0]])
        value = matrix.getSquare(1,1)
        assert(value == 16)


class Matrix:
    mat = []
    default = 0
    width = None
    height = None

    def generate(width, height, value = 0):
        matrix = Matrix()
       
        for y in range(height):
            emptyRow = []
            for x in range(width):
                emptyRow.append(value)
            matrix.addRow(emptyRow)
        return matrix

    def __init__(self, lines :list = []):
        self.mat = []
        self.height = 0
        self.width = None
        self.parseLines(lines)

    def __str__(self):
        output = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.get(x, y) > 0:
                    output += "#"
                else:
                    output += "."
            output += "\n"
        return output

    def __repr__(self):
        return str(self)

    def padMatrix(self, value) -> Matrix:
        #pad right and left of existing rows
        for y in range(0, len(self.mat)):
            self.mat[y] = [value] + self.mat[y] + [value]

        #pad above and below with empty rows
        emptyRow = []
        for x in range(self.width + 2):
            emptyRow.append(value)
        self.mat = [emptyRow] + self.mat + [emptyRow.copy()]
        self.width += 2
        self.height += 2


    def setDefault(self, value):
        self.default = value

    def contains(self, point: Point2d) -> bool:
        return self.get(point.x, point.y) > 0

    def parseLines(self, lines):
        for line in lines:
            numbers = []
            for raw in line:
                numbers.append(int(raw))
            self.addRow(numbers)

    def addRow(self, row): 
        self.mat.append(row)
        self.height = len(self.mat)
        if self.width is not None:
            assert(self.width == len(row))
        else:
            self.width = len(row)

    def get(self, x, y):
        if y < 0 or x < 0:
            return self.default
        if y >= self.height or x >= self.width:
            return self.default
        return self.mat[y][x]

    def set(self, x, y, value = 1):
        if y < 0 or x < 0 or y >= self.height or x >= self.width:     
            raise RuntimeError("Forbidden navigation to: (" + str(x) + ", " + str(y) + ")")
        self.mat[y][x] = value

    def reset(self, x, y):
        if y < 0 or x < 0:
            return
        if y >= self.height or x >= self.width:
            return
        self.mat[y][x] = 0

    def countDots(self):
        rowDots = map(lambda row: row.count(1), self.mat)
        return sum(rowDots)

    def getSquare(self, x, y):
        value = str(self.upLeft(x,y)) + str(self.above(x,y)) + str(self.upRight(x,y))
        value += str(self.left(x,y)) + str(self.get(x,y)) + str(self.right(x,y))
        value += str(self.downLeft(x,y)) + str(self.below(x,y)) + str(self.downRight(x,y))
        return int(value, 2)

    def above(self, x,y):
        return self.get(x, y-1)
    
    def below(self, x, y):
        return self.get(x, y+1)

    def left(self, x, y):
        return self.get(x-1, y)

    def right(self, x, y):
        return self.get(x+1, y)

    def upLeft(self, x, y):
        return self.get(x-1, y-1)

    def upRight(self, x, y):
        return self.get(x+1, y-1)

    def downLeft(self, x, y):
        return self.get(x-1, y+1)

    def downRight(self, x, y):
        return self.get(x+1, y+1)

    def pointify(self, x,y):
        return Point2d(x, y, self.get(x, y))

if __name__ == '__main__':
    unittest.main()