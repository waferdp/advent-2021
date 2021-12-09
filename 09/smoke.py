import functools
import readFile as file
from Matrix import Matrix
from Basin import Basin
from Point2d import Point2d

def findLowPoints(matrix: Matrix):
    lowPoints = []
    for y in range(0, matrix.height):
        for x in range(0, matrix.width):
            if matrix.isLeast(x,y):
                lowPoint = Point2d(x, y, matrix.get(x,y))
                lowPoints.append(lowPoint)

    return lowPoints

def findThreeLargest(basins):
    three = []
    for basin in basins:
        size = len(basin.getVisited())
        if len(three) < 3:
            three.append(size)
        else:
            for i in range(0, len(three)):
                compareSize = three[i]
                if size > compareSize:
                    three[i] = size
                    break
    return three


def calculateRisk(lowPoints):
    value = 0
    for point in lowPoints:
        value += point.value + 1
    return value

def testMatrix():
    lines = file.read("test_input.txt")
    mat = Matrix(lines)
    assert(len(mat.mat[0]) == len(mat.mat[1]) == len(mat.mat[2]) == len(mat.mat[3]) == len(mat.mat[4]) == mat.width)
    assert(len(mat.mat) == mat.height == 5)

def test1():
    lines = file.read("test_input.txt")
    mat = Matrix(lines)
    lowPoints = findLowPoints(mat)
    assert(len(lowPoints) == 4)
    assert(calculateRisk(lowPoints) == 15)

def test2():
    lines = file.read("test_input.txt")
    mat = Matrix(lines)
    lowPoints = findLowPoints(mat)
    basins = []
    for lowPoint in lowPoints:
        basin = Basin(mat, lowPoint)
        basin.exploreBasin()
        basins.append(basin)

    assert(len(basins[0].getVisited()) == 3)
    assert(len(basins[1].getVisited()) == 9)
    assert(len(basins[2].getVisited()) == 14)
    assert(len(basins[3].getVisited()) == 9)

    three = findThreeLargest(basins)
    product = functools.reduce(lambda x,y: x*y, three)

    assert(product == 1134)

def run():
    lines = file.read("puzzle_input.txt")
    mat = Matrix(lines)
    lowPoints = findLowPoints(mat)
    basins = []
    for lowPoint in lowPoints:
        basin = Basin(mat, lowPoint)
        basin.exploreBasin()
        basins.append(basin)
    
    three = findThreeLargest(basins)
    product = functools.reduce(lambda x,y: x*y, three)

    return product

testMatrix()
test1()
test2()
value = run()
print(value)