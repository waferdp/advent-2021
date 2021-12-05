from Point2d import Point2d
from Line import Line

class Grid:

    points = {}

    def __init__(self):
        self.points = {}

    def findPoint(self, point: Point2d) -> int:
        if point.x not in self.points:
            return None
        elif point.y not in (self.points[point.x]):
            return None 
        else:
            return self.points[point.x][point.y]

    def addPoint(self, point: Point2d):
        if point.x not in self.points:
            point.x = {}
        self.points[point.x][point.y] = point

    def addLine(self, line: Line):
        for point in line.points:
            found = self.findPoint(point)
            if found is not None:
                found.vents += 1
                print("Intersect at " + str(found))
            else:
                self.addPoint(point)
