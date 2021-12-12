import unittest
import readFile as file
from Matrix import Matrix
from Step import Step

class TestOctopus(unittest.TestCase):
   
    def testPart1(self):
        octopus = Octopus('test_input.txt')
        octopus.run1()
        assert(octopus.flashes == 1656)

    def testPart2(self):
        octopus = Octopus('test_input.txt')
        octopus.run2()
        assert(octopus.steps == 195)


class Octopus():
    
    lines = []
    flashes = 0
    steps = 0

    def __init__(self, path):
        self.lines = file.read(path)
        self.flashes = 0
    
    def run1(self):
        matrix = Matrix(self.lines)
        step = Step(matrix) 
        for i in range(100):
            self.flashes += step.takeStep()

    def run2(self):
        matrix = Matrix(self.lines)
        step = Step(matrix) 
        size = matrix.width * matrix.height
        while self.flashes < size:
            self.flashes = step.takeStep()
        self.steps = step.steps

if __name__ == '__main__':
    #unittest.main()
    octopus = Octopus('puzzle_input.txt')
    octopus.run2()
    print(octopus.steps)