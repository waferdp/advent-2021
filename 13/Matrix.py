import unittest
import readFile as file

class TestMatrix(unittest.TestCase):

    def testGenerate(self):
        matrix = Matrix.generate(11, 15)
        assert(matrix.width == 11 and matrix.height == 15)

    def testExists(self):
        matrix = Matrix.generate(11, 15)
        matrix.set(6, 10)
        assert(matrix.contains(6,10))

    def testFoldSelfX(self):
        matrix = Matrix.generate(11, 11)
        matrix.set(0, 10)
        matrix.set(10, 10)
        matrix.fold(5, None)
        assert(matrix.countDots() == 1)

    def testFoldSelfY(self):
        matrix = Matrix.generate(11, 11)
        matrix.set(3, 0)
        matrix.set(3, 10)
        matrix.fold(None, 5)
        assert(matrix.countDots() == 1)

    def testFoldOther(self):
        matrix = Matrix.generate(11, 11)
        matrix.set(0, 9)
        matrix.set(6, 10)
        matrix.fold(5, None)
        assert(matrix.countDots() == 2)


class Matrix:
    mat = []
    width = None
    height = None

    def generate(width, height):
        matrix = Matrix()
       
        for y in range(height):
            emptyRow = []
            for x in range(width):
                emptyRow.append(0)
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

    def contains(self, x, y):
        return self.get(x, y) > 0

    def parseLines(self, lines):
        for line in lines:
            numbers = []
            for raw in line:
                numbers.append(int(raw))
            self.addRow(numbers)

    def fold(self, x, y):
        if y is not None:
            half = self.mat[:y]
            rest = self.mat[y+1:]
            Matrix.copyY(rest, half)
            self.mat = half
            self.height = len(self.mat)

        elif x is not None:
            half = list(map(lambda row: row[:x], self.mat))
            rest = list(map(lambda row: row[x+1:], self.mat))
            Matrix.copyX(rest, half)
            self.mat = half
            self.width = len(self.mat[0])

    def copyY(src, dest):
        for y in range(0, len(src)):
            for x in range(0, len(src[y])):
                dest[-y-1][x] = max(src[y][x], dest[-y-1][x])

    def copyX(src, dest):
        for y in range(0, len(src)):
            for x in range(0, len(src[y])):
                dest[y][-x-1] = max(src[y][x], dest[y][-x-1])

    def countDots(self):
        rowDots = map(lambda row: row.count(1), self.mat)
        return sum(rowDots)

    def addRow(self, row): 
        self.mat.append(row)
        self.height = len(self.mat)
        if self.width is not None:
            assert(self.width == len(row))
        else:
            self.width = len(row)


    def isLeast(self, x ,y):
        val = self.get(x,y)
        above = self.above(x,y)
        right = self.right(x,y)
        below = self.below(x,y)
        left = self.left(x,y)

        if(val < above and val < right and val < below and val < left):
            return True
        else:
            return False

    def get(self, x, y):
        if y < 0 or x < 0:
            return 10
        if y >= self.height or x >= self.width:
            return 10
        return self.mat[y][x]

    def set(self, x, y):
        if y < 0 or x < 0:
            return
        if y >= self.height or x >= self.width:
            return
        self.mat[y][x] = 1

    def reset(self, x, y):
        if y < 0 or x < 0:
            return
        if y >= self.height or x >= self.width:
            return
        self.mat[y][x] = 0

    def increaseDonut(self, x, y):
        self.above(x,y)
        self.below(x,y)
        self.left(x,y)
        self.right(x,y)
        self.upLeft(x,y)
        self.upRight(x,y)
        self.downLeft(x,y)
        self.downRight(x,y)

    def above(self, x,y):
        return self.set(x, y-1)
    
    def below(self, x, y):
        return self.set(x, y+1)

    def left(self, x, y):
        return self.set(x-1, y)

    def right(self, x, y):
        return self.set(x+1, y)

    def upLeft(self, x, y):
        return self.set(x-1, y-1)

    def upRight(self, x, y):
        return self.set(x+1, y-1)

    def downLeft(self, x, y):
        return self.set(x-1, y+1)

    def downRight(self, x, y):
        return self.set(x+1, y+1)

if __name__ == '__main__':
    unittest.main()