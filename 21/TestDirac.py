import unittest
import readFile as file
from Dirac import *

class TestDirac(unittest.TestCase):
    def testPractice(self):
        input = file.read('test_input.txt')
        fnord = Main.run1(input)
        assert(fnord == 739785)

    def testPlay(self):
        input = file.read('test_input.txt')
        fnord = Main.run2(input)
        assert(fnord == 444356092776315)

if __name__ == '__main__':
      unittest.main()