from unittest.suite import TestSuite
from Area import Area
from Point2d import Point2d
import readFile as file

class Trick:
    area = None
    tests = 0
    maxY = 0

    def __init__(self, input) -> None:
        self.area = Trick.parseTarget(input)
        self.maxY = 0

    def getMinXVelocity(self):
        for i in range(self.area.topRight.x+1):
            if self.area.bottomLeft.x <= i * (i + 1) // 2 <= self.area.topRight.x:
                return i
        return -1

    def loop(self):
        minX = self.getMinXVelocity()
        maxVelY = 0
        maxX = 0
        count = 0
        velX = minX

        for velX in range(minX, self.area.topRight.x+1):
            for velY in range(self.area.bottomLeft.y, abs(self.area.bottomLeft.y)):
                if self.testShoot(Point2d(velX, velY)):
                    count += 1
                    maxVelY = max(maxVelY, velY)
        self.maxY = maxVelY * (maxVelY + 1) // 2
        self.count = count
        return 

    def parseTarget(row):
        row = row.replace('target area: ', '')
        xs, ys = row.split(', ')
        xL, xH = Trick.parseInterval(xs.replace('x=', ''))
        yL, yH = Trick.parseInterval(ys.replace('y=', ''))
        
        return Area(Point2d(xL, yL), Point2d(xH, yH))

    def parseInterval(interval):
        low, high = sorted(list(map(lambda x: int(x), interval.split('..'))))
        return low, high

    def testShoot(self, v: Point2d ):
        position = Point2d(0,0)
        maxY = -999999999
        while not self.area.missed(position):
            position, v = self.inc(position, v)
            maxY = max(maxY, position.y)
            if self.area.isIn(position):
                return True
        return False
            

    def inc(self, position, velocity):
        pos = position
        pos += velocity
        if velocity.x > 0:
            velocity.x -= 1
        elif velocity.x < 0:
            velocity.x + 1
        velocity.y -= 1
        return pos, velocity

class Main:
    def run(input):
        trick = Trick(input)
        trick.loop()
        return (trick.maxY, trick.count)

if __name__ == '__main__':
    input = file.read('input.txt')[0]
    maxY, count = Main.run(input)
    print(maxY, count)