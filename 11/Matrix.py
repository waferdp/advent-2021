import unittest
import readFile as file

class TestMatrix(unittest.TestCase):

    def testMatrix(self):
        lines = file.read('test_input.txt')
        matrix = Matrix(lines)
        assert(matrix.height == 10 and matrix.width == 10)


class Matrix:
    mat = []

    def __init__(self, lines :list = []):
        self.mat = []
        self.height = 0
        self.width = None
        self.parseLines(lines)

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
        self.mat[y][x] += 1

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