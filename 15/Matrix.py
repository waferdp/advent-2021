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

    def testMultiplyRight(self):
        matrix = Matrix.generate(5, 5, 1)
        matrix.multiplyRight(2)
        assert(matrix.width == 10)
    
    def testMultiplyDown(self):
        matrix = Matrix.generate(5, 5, 1)
        matrix.multiplyDown(2)
        assert(matrix.height == 10)

    def testIncreaseOverflow(self):
        matrix = Matrix.generate(5, 5, 8)
        matrix.multiplyRight(3)
        assert(10 not in matrix.mat[0])

class Matrix:
    mat = []
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
                    output += " "
            output += "\n"
        return output

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

    def multiplyRight(self, times):
        for row in self.mat:
            extra = []
            for i in range(1, times):
                for original in row:
                    value = original + i 
                    if value > 9:
                        value -= 9
                    extra.append(value)
            row += extra
        self.width = len(self.mat[0])

    def multiplyDown(self, times):
        extras = []
        for i in range(1, times):
            for row in self.mat:
                incCopy = []
                for original in row:
                    value = original + i 
                    if value > 9:
                        value -= 9
                    incCopy.append(value)
                extras.append(incCopy)
        self.mat += extras
        self.height = len(self.mat)

    def inf():
        return 999999999

    def get(self, x, y):
        if y < 0 or x < 0:
            return Matrix.inf()
        if y >= self.height or x >= self.width:
            return Matrix.inf()
        return self.mat[y][x]

    def set(self, x, y, value = 1):
        if(self.get(x,y) != 0):
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

    # def increaseDonut(self, x, y):
    #     self.above(x,y)
    #     self.below(x,y)
    #     self.left(x,y)
    #     self.right(x,y)
    #     self.upLeft(x,y)
    #     self.upRight(x,y)
    #     self.downLeft(x,y)
    #     self.downRight(x,y)

    def above(self, x,y):
        return self.pointify(x, y-1)
    
    def below(self, x, y):
        return self.pointify(x, y+1)

    def left(self, x, y):
        return self.pointify(x-1, y)

    def right(self, x, y):
        return self.pointify(x+1, y)

    # def upLeft(self, x, y):
    #     return self.set(x-1, y-1)

    # def upRight(self, x, y):
    #     return self.set(x+1, y-1)

    # def downLeft(self, x, y):
    #     return self.set(x-1, y+1)

    # def downRight(self, x, y):
    #     return self.set(x+1, y+1)

    def pointify(self, x,y):
        return Point2d(x, y, self.get(x, y))

if __name__ == '__main__':
    unittest.main()