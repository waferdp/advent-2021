import unittest
import readFile as file
from Dirac import *

class TestDirac(unittest.TestCase):
    def testPlay(self):
        input = file.read('test_input.txt')
        fnord = Main.run1(input)
        assert(fnord == 739785)

if __name__ == '__main__':
      unittest.main()