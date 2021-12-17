from Point2d import Point2d

class Area:
    bottomLeft = None
    topRight = None
    maxY = 0
    
    def __init__(self, bottomLeft, topRight) -> None:
        self.bottomLeft = bottomLeft
        self.topRight = topRight

    def isIn(self, point: Point2d):
        return point >= self.bottomLeft and point <= self.topRight

    def missed(self, point: Point2d):
        return self.overShot(point) or self.underShot(point)

    def overShot(self, point: Point2d):
        return point.x > self.topRight.x
    
    def underShot(self, point: Point2d):
        return point.y < self.bottomLeft.y
    