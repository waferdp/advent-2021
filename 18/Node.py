import math

class Node:
    left = None
    right = None

    def __init__(self, a= None, b = None) -> None:
        self.left = a
        self.right = b

    def __str__(self) -> str:
        return '[' + str(self.left) + ',' + str(self.right) + ']'

    def __repr__(self) -> str:
        return str(self)

    def createFrom(value):
        half = value / 2
        left = math.floor(half)
        right = math.ceil(half)
        return Node(left, right)
        
    
    def addFromLeft(self, value):
        if type(self.left) is Node:
            self.addFromLeft(value)
        else:
            self.left += value
        
    def addFromRight(self, value):
        if type(self.right) is Node:
            self.addFromRight(value)
        else:
            self.right += value

    def getMagnitude(self):    
        if type(self.left) is Node:
            leftValue = 3 * self.left.getMagnitude()
        else:
            leftValue = 3 * self.left
        if type(self.right) is Node:
            rightValue = 2 * self.right.getMagnitude()
        else:
            rightValue = 2 * self.right
        return leftValue + rightValue