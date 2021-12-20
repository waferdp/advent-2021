import readFile as file
from vec3 import vec3

class scanner:
    points = []
    position = None

    def __init__(self, points = [], position = None) -> None:
        self.points = points
        self.position = position

    def findScanners(self):
        pass

    def createWithOffset(center, beacons):
        points = list(map(lambda point: point + center, beacons))
        return scanner(points, center)
