from typing import Any
import unittest
from Node import Node

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

    def testSplit(self):
        input = ['[[[[0,7],4],[15,[0,13]]],[1,1]]']
        snailFish = SnailFish(input)
        node = snailFish.lines[0]
        snailFish.split(node)
        assert(str(node) == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')

class SnailFish:
    lines = []
    explosion = False
    split = False
    reduction = False
    
    def __init__(self, input) -> None:
        self.lines = []
        for line in input:
            node, rest = SnailFish.parseLine(line)
            self.lines.append(node)
        self.explosion = False
        self.split = False
        self.reduction = False          

    def parseLine(line):
        while line[0] in ',]':
            line = line[1:]
        first, line = line[0],line[1:]
        if first == '[':
            left, line = SnailFish.parseLine(line)
            right, line = SnailFish.parseLine(line)
            return Node(left, right), line
        elif first.isnumeric():
            return int(first), line

    def explode(self, node, depth = 0):
        typeLeft = type(node.left)
        typeRight = type(node.right)
        if typeLeft is not Node and typeRight is not Node:
            if depth >= 4:
                print('Explode ' + str(node))
                return node
        if typeLeft is Node:
            explode = self.explode(node.left, depth + 1)
            if explode is not None:
                node.left = 0
                if typeRight is not Node:
                    node.right += explode.right
                else:
                    node.right.addFromLeft(explode.right)
            return None
        if typeRight is Node:
            explode = self.explode(node.left, depth + 1)
            if explode is not None:
                node.left = 0
                if typeLeft is not Node:
                    node.left += explode.left
                else:
                    node.left.addFromRight(explode.left)
            return None

    def split(self, node):
        typeLeft = type(node.left)
        typeRight = type(node.right)
        if typeLeft is Node:
            if self.split(node.left): 
                return True
        else:
            if node.left > 10:
                node.left = Node.createFrom(node.left)
                return True
        if typeRight is Node:
            if self.split(node.right): 
                return True
        else:
            if node.right > 10:
                node.right = Node.createFrom(node.right)
                return True
        return False

if __name__ == '__main__':
    unittest.main()