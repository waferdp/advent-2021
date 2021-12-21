import unittest
import readFile as file
from Matrix import Matrix

from Trench import Trench

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

    # def testSneakySmall(self):
    #     input = file.read('puzzle_input.txt')
    #     trench = Trench(input)
    #     trench.matrix = Matrix([0,0,0],[0,1,0], [0,0,0])


if __name__ == '__main__':
      unittest.main()