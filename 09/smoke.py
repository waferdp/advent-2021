import readFile as file
from Matrix import Matrix

def findLowPoints(matrix: Matrix):
    lowPoints = []
    for y in range(0, matrix.height):
        for x in range(0, matrix.width):
            if matrix.isLeast(x,y):
                lowPoints.append(matrix.get(x,y))

    return lowPoints

def calculateRisk(lowPoints):
    return sum(lowPoints) + len(lowPoints)

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

def run():
    lines = file.read("puzzle_input.txt")
    mat = Matrix(lines)
    lowPoints = findLowPoints(mat)
    return calculateRisk(lowPoints)

testMatrix()
test1()
value = run()
print(value)