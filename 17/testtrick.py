import unittest
from trick import Trick
from Point2d import Point2d

class TestTrick(unittest.TestCase):
    def testParse(self):
        input = 'target area: x=20..30, y=-10..-5'
        target = Trick.parseTarget(input)
        assert(target.topRight == Point2d(30, -5))
        assert(target.bottomLeft == Point2d(20, -10))

    def testShoot(self):
        input = 'target area: x=20..30, y=-10..-5'
        trick = Trick(input)
        trick.loop()
        assert(trick.maxY == 45)
        assert(trick.count == 112)

if __name__ == '__main__':
    unittest.main()