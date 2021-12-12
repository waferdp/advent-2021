from Matrix import Matrix
from Point2d import Point2d
import unittest

class TestStep(unittest.TestCase):
    def testFlash(self):
        lines = ['11111', '19991', '19191', '19991', '11111']
        matrix = Matrix(lines)
        step = Step(matrix)
        flashes = step.takeStep()
        assert(flashes == 9)
        assert(matrix.get(2,2) == 0)
        assert(step.steps == 1)

    def testTwoSteps(self):
            lines = ['11111', '19991', '19191', '19991', '11111']
            matrix = Matrix(lines)
            flashes = 0
            step = Step(matrix)
            for i in range(2):
                flashes += step.takeStep()
            assert(flashes == 9)
            assert(matrix.get(2,2) == 1)
            assert(step.steps == 2)

class Step:
    
    flashed = {}
    matrix: Matrix = {}
    steps = 0
    
    def __init__(self, matrix: Matrix):
        self.flashed = {}
        self.matrix = matrix

    def takeStep(self):
        self.increaseLevel()
        flashes = self.findFlashes()
        self.cascade(flashes)
        flashes = self.countFlashes()
        self.reset()
        self.steps += 1
        return flashes

    def increaseLevel(self):
        for y in range(0, self.matrix.height):
            for x in range(0, self.matrix.width):
                self.matrix.set(x, y)

    def findFlashes(self):
        flashes = []
        for y in range(0, self.matrix.height):
            for x in range(0, self.matrix.width):
                if self.matrix.get(x,y) > 9:
                    flashes += self.add(x, y)
        return flashes    

    def cascade(self, flashes):
        while len(flashes) > 0:
            newFlashes = []
            for flash in flashes:
                self.matrix.increaseDonut(flash.x, flash.y)
                newFlashes += self.findFlashes()
            flashes = newFlashes
        
    def reset(self):
        for y in self.flashed:
            for x in self.flashed[y]:
                self.matrix.reset(x,y)
        self.flashed = {}

    def add(self, x, y):
        if y not in self.flashed:
            self.flashed[y] = {}
        if x not in self.flashed[y]:
            self.flashed[y][x] = 1
            return [Point2d(x,y)]
        return []

    def countFlashes(self):
        count = 0
        for y in self.flashed:
            for x in self.flashed[y]:
                count += 1
        return count

if __name__ == '__main__':
    unittest.main()