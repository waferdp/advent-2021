from Point2d import Point2d 

class Line:

    start = None
    end = None
    points = []

    def __init__(self, start: Point2d, end: Point2d):
        self.start = start
        self.end = end
        self.points = []
        self.build()        

    def isStraight(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def build(self):
        current = self.start
        self.points.append(current)
        while current != self.end:
            current = Line.nextPoint(current, self.end)
            self.points.append(current)

    def nextPoint(a: Point2d, b: Point2d):
        xDir = b.x - a.x
        xDir = int(xDir/ abs(xDir)) if xDir != 0 else 0

        yDir = b.y - a.y
        yDir = int(yDir / abs(yDir)) if yDir != 0 else 0
        
        if xDir == 0 and yDir == 0:
            return b
        return Point2d(a.x + xDir, a.y + yDir)