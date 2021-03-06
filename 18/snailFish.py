import readFile as file
import itertools
from Node import Node

class SnailFish:
    rawLines = []
    lines = []
    magnitude = 0
    
    def __init__(self, input) -> None:
        self.rawLines = input
        self.lines = []
        for line in input:
            node, rest = SnailFish.parseLine(line)
            self.lines.append(node)
        self.magnitude = 0

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

    def permuteLines(self):
        #var combinations = itertools.combinations(range(100), 2)
        for i in range (0, len(self.lines)):
            for j in range(0, len(self.lines)):
                if i == j:
                    continue
                a, rest  = SnailFish.parseLine(self.rawLines[i])
                b, rest  = SnailFish.parseLine(self.rawLines[j])
                node = Node(a, b)
                self.reduceIt(node)
                self.magnitude = max(self.magnitude, node.getMagnitude())

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
            if node.left > 9:
                node.left = Node.createFrom(node.left)
                return True
        if typeRight is Node:
            if self.splitNode(node.right): 
                return True
        else:
            if node.right > 9:
                node.right = Node.createFrom(node.right)
                return True
        return False

class Main:
    def run1(input):
        snailFish = SnailFish(input)
        snailFish.addLines()
        return snailFish.lines[0].getMagnitude()

    def run2(input):
        snailFish = SnailFish(input)
        snailFish.permuteLines()
        return snailFish.magnitude

input = file.read('puzzle_input.txt')
magnitude = Main.run2(input)
print(magnitude)
