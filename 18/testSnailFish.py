import unittest
import readFile as file
from snailFish import *

class TestSnailFish(unittest.TestCase):
    def testParse(self):
        input = '[[[[[9,8],1],2],3],4]'
        node, rest = SnailFish.parseLine(input)
        assert(node is not None)
        assert(str(node) == input)

    def testExplode(self):
        input = ['[[[[[9,8],1],2],3],4]']
        snailFish = SnailFish(input)
        node = snailFish.lines[0]
        snailFish.explode(node)
        assert(str(node) == '[[[[0,9],2],3],4]')

    def testExplode2(self):
        input = ['[7,[6,[5,[4,[3,2]]]]]']
        snailFish = SnailFish(input)
        node = snailFish.lines[0]
        snailFish.explode(node)
        assert(str(node) == '[7,[6,[5,[7,0]]]]')

    def testExplode3(self):
        input = ['[[6,[5,[4,[3,2]]]],1]']
        snailFish = SnailFish(input)
        node = snailFish.lines[0]
        snailFish.explode(node)
        assert(str(node) == '[[6,[5,[7,0]]],3]')

    def testSplit(self):
        input = ['[[[[0,7],4],[15,[0,13]]],[1,1]]']
        snailFish = SnailFish(input)
        node = snailFish.lines[0]
        snailFish.splitNode(node)
        assert(str(node) == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
    
    def testReduce(self):
        input = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
        snailFish = SnailFish(input)
        snailFish.addLines()
        assert(str(snailFish.lines[0]) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def testAdd1(self):
        input = ['[1,1]', '[2,2]', '[3,3]', '[4,4]']
        snailFish = SnailFish(input)
        snailFish.addLines()
        assert(str(snailFish.lines[0]) == '[[[[1,1],[2,2]],[3,3]],[4,4]]')

    def testAdd2(self):
        input = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']
        snailFish = SnailFish(input)
        snailFish.addLines()
        assert(str(snailFish.lines[0]) == '[[[[3,0],[5,3]],[4,4]],[5,5]]')
        
    # def testSmall(self):
    #     input = file.read('test_input.txt')
    #     snailFish = SnailFish(input)
    #     snailFish.addLines()
    #     assert(str(snailFish.lines[0]) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
    #     assert(snailFish.lines[0].getMagnitude() == 4140)

if __name__ == '__main__':
    unittest.main()