import readFile as file
from Point2d import Point2d 
from Line import Line

class Grid:

    points = []

    def __init__(self):
        self.points = []

    def findPoint(self, point: Point2d) -> Point2d:
        for existing in self.points:
            if existing == point:
                return existing

    def addLine(self, line: Line):
        for point in line.points:
            found = self.findPoint(point)
            if found is not None:
                found.vents += 1
                print("Intersect at " + str(found))
            else:
                self.points.append(point)

def parseLines(lines):
    ventGrid = Grid()
    counter = 0
    for line in lines:
        points = line.split("->")
        start = Point2d(int(points[0].split(",")[0]), int(points[0].split(",")[1]))
        end = Point2d(int(points[1].split(",")[0]), int(points[1].split(",")[1]))
        
        ventLine = Line(start, end)
        if ventLine.isStraight():
            ventGrid.addLine(ventLine)
        counter += 1
        if counter % 10 == 0:
            print(counter)

    intersects = 0

    for point in ventGrid.points:
        if point.vents > 1:
            intersects += 1
            #print(point)

    return intersects

def test():
    lines = file.read("test_input.txt")
    assert(5 == parseLines(lines))


def run():
    lines = file.read("puzzle_input.txt")
    print("Intersections: " + str(parseLines(lines)))

test()
run()