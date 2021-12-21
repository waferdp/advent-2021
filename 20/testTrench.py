import unittest
import readFile as file
from Matrix import Matrix

from Trench import *

class TestTrench(unittest.TestCase):

    def testParse(self):
        input = file.read('test_input.txt')
        trench = Trench(input)
        assert(str(trench.matrix) == '#..#.\n#....\n##..#\n..#..\n..###\n')

    def testEnhance(self):
        input = file.read('test_input.txt')
        trench = Trench(input)
        trench.enhanceImage()
        assert(str(trench.matrix) == '.##.##.\n#..#.#.\n##.#..#\n####..#\n.#..##.\n..##..#\n...#.#.\n')

    def testEnhanceTwice(self):
        input = file.read('test_input.txt')
        trench = Trench(input)
        trench.enhanceImage()
        trench.enhanceImage()
        assert(str(trench.matrix) == '.......#.\n.#..#.#..\n#.#...###\n#...##.#.\n#.....#.#\n.#.#####.\n..#.#####\n...##.##.\n....###..\n')

    def testRun1(self):
        input = file.read('test_input.txt')
        dots = Main.run1(input)
        assert(dots == 35)
        
    def testEnhanceFittyTimes(self):
        input = file.read('test_input.txt')
        dots = Main.run2(input)
        assert(dots == 3351)

if __name__ == '__main__':
      unittest.main()