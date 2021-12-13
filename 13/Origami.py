import unittest
import readFile as file
from Point2d import Point2d
from Matrix import Matrix

class TestOrigami(unittest.TestCase):
    def testDots(self):
        input = file.read("test_input.txt")
        dots = Main.findDots(input)
        assert(len(dots) == 18)
        assert(dots[4].x == 10 and dots[4].y == 4)

    def testFolds(self):
        input = file.read("test_input.txt")
        folds = Main.findFoldInstructions(input)
        assert(len(folds) == 2)

    def testSmall(self):
        input = file.read("test_input.txt")
        dots = Main.run1(input)
        assert(dots == 17)
       
    def testPrint(self):
        input = file.read("test_input.txt")
        text = Main.run2(input)
        assert("\n" in text and text.count("#") == 16)

class Main:
    def run1(input):
        dots = Main.findDots(input)
        width = max(map(lambda dot: dot.x, dots)) + 1
        height = max(map(lambda dot: dot.y, dots)) + 1

        foldInstructions = Main.findFoldInstructions(input)

        matrix = Matrix.generate(width, height)
        for dot in dots:
            matrix.set(dot.x, dot.y)

        matrix.fold(foldInstructions[0].x, foldInstructions[0].y)
            
        return matrix.countDots()

    def run2(input):
        dots = Main.findDots(input)
        width = max(map(lambda dot: dot.x, dots)) + 1
        height = max(map(lambda dot: dot.y, dots)) + 1

        foldInstructions = Main.findFoldInstructions(input)

        matrix = Matrix.generate(width, height)
        for dot in dots:
            matrix.set(dot.x, dot.y)
        
        for foldInstruction in foldInstructions:
            matrix.fold(foldInstruction.x, foldInstruction.y)
        return str(matrix)

    def findDots(input):
        dots = []
        for line in input:
            if "," in line:
                x, y = list(map(lambda x: int(x), line.split(",")))
                dots.append(Point2d(x, y))
        return dots

    def findFoldInstructions(input):
        folds = []
        for line in input:
            if "fold along " in line:
                foldRaw = line.replace("fold along ", "")
                axis, index = foldRaw.split("=")
                if axis == 'y':
                    folds.append(Point2d(None, int(index)))
                else:
                    folds.append(Point2d(int(index), None))
        return folds

if __name__ == '__main__':
    #unittest.main()

    input = file.read('puzzle_input.txt')
    dots = Main.run1(input)
    text = Main.run2(input)
    print(dots)
    print(text) 