import unittest
import readFile as file
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
        snailFish.splitNode(node)
        assert(str(node) == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
    
    def testReduce(self):
        input = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
        snailFish = SnailFish(input)
        snailFish.addLines()
        assert(str(snailFish.lines[0]) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def testSmall(self):
        input = file.read('test_input.txt')
        magnitude = Main.run1(input)
        assert(magnitude == 4140)

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
        while first.isnumeric() and line[0] not in '[],':
            first += line[0]
            line = line[1:]
        if first == '[':
            left, line = SnailFish.parseLine(line)
            right, line = SnailFish.parseLine(line)
            return Node(left, right), line
        elif first.isnumeric():
            return int(first), line

    def addLines(self):
        while len(self.lines) > 1:
            first = Node(self.lines[0], self.lines[1])
            self.lines = self.lines[1:]
            self.lines[0] = first
            self.reduceIt(first)

    def reduceIt(self, node):
        change = True
        while change:
            change = self.reduceNode(node)

    def reduceNode(self, node):
        before = str(node)
        self.explode(node)
        if before != str(node):
            return True
        self.splitNode(node)
        return before != str(node)

    def explode(self, node, depth = 0):
        typeLeft = type(node.left)
        typeRight = type(node.right)
        if typeLeft is not Node and typeRight is not Node:
            if depth >= 4:
                return node, True
        if typeLeft is Node:
            explode, childExploded = self.explode(node.left, depth + 1)
            if childExploded:
                node.left = 0
            if explode is not None:
                if explode.right is not None:
                    if typeRight is not Node:
                        node.right += explode.right
                    else:
                        node.right.addFromLeft(explode.right)
                return Node(explode.left, None), False
        if typeRight is Node:
            explode, childExploded = self.explode(node.right, depth + 1)
            if childExploded:
                node.right = 0
            if explode is not None:
                if explode.left is not None:
                    if typeLeft is not Node:
                        node.left += explode.left
                    else:
                        node.left.addFromRight(explode.left)
                return Node(None, explode.right), False
        return None, False

    def splitNode(self, node):
        typeLeft = type(node.left)
        typeRight = type(node.right)
        if typeLeft is Node:
            if self.splitNode(node.left): 
                return True
        else:
            if node.left > 10:
                node.left = Node.createFrom(node.left)
                return True
        if typeRight is Node:
            if self.splitNode(node.right): 
                return True
        else:
            if node.right > 10:
                node.right = Node.createFrom(node.right)
                return True
        return False

class Main:
    def run1(input):
        snailFish = SnailFish(input)
        snailFish.addLines()
        return snailFish.lines[0].getMagnitude()

if __name__ == '__main__':
    unittest.main()