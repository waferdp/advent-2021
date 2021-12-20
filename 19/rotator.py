from collections import defaultdict
import unittest
from vec3 import vec3
from scanner import scanner

class testRotator(unittest.TestCase):

    def verifyExpected(self, rotationIndex, expected):
        rotator = Rotator()
        point = vec3(1, 2, 3)
        rotated = point.rotateMany(rotator.rotations[rotationIndex])
        assert(rotated == expected)

    def testNoRotation(self):
        point = vec3(1, 2, 3)
        self.verifyExpected(0, point)

    def testFlipY(self):
        expected = vec3(-1, -2, 3)
        self.verifyExpected(4, expected)

    def testOrient3(self):
        expected = vec3(2, 3, 1)
        self.verifyExpected(8, expected)

    def testOrient4(self):
        expected = vec3(-2, -3, 1)
        self.verifyExpected(12, expected)

    def testOrient5(self):
        expected = vec3(3, 1, 2)
        self.verifyExpected(16, expected)
    
    def testOrient6(self):
        expected = vec3(-3, -1, 2)
        self.verifyExpected(20, expected)

class Rotator:
    count = 0
    rotations = []
    tested = {}
    

    def __init__(self) -> None:
        self.count = 0
        self.tested = {}
        self.rotations = []
        self.buildRotations()

    def buildRotations(self):
        self.rotations.append([])
        self.rotations.append(['x'])
        self.rotations.append(['x','x'])
        self.rotations.append(['x','x','x'])

        #Flip Y
        orient = ['z','z']
        self.rotations.append(orient)
        self.rotations.append(orient + ['x'])
        self.rotations.append(orient + ['x','x'])
        self.rotations.append(orient + ['x','x','x'])

        # Orientation 3
        orient = ['x', 'x', 'x', 'y', 'y', 'y']
        self.rotations.append(orient)
        self.rotations.append(orient + ['x'])
        self.rotations.append(orient + ['x','x'])
        self.rotations.append(orient + ['x','x','x'])

        #Orientation 4
        orient = ['z','x']
        self.rotations.append(orient)
        self.rotations.append(orient + ['x'])
        self.rotations.append(orient + ['x','x'])
        self.rotations.append(orient + ['x','x','x'])

        #Orientation 5
        orient = ['z', 'y']
        self.rotations.append(orient)
        self.rotations.append(orient + ['x'])
        self.rotations.append(orient + ['x','x'])
        self.rotations.append(orient + ['x','x','x'])

        #Orientation 6
        orient = ['z', 'z', 'z', 'y', 'y', 'y']
        self.rotations.append(orient)
        self.rotations.append(orient + ['x'])
        self.rotations.append(orient + ['x','x'])
        self.rotations.append(orient + ['x','x','x'])


    def rotate(self, vectors, rotations) -> list:
        rotated = map(lambda vector: vector.rotateMany(rotations), vectors)
        return list(rotated)

    def rotateAndFind(self, a: list, b: list):
        xRot = None
        yRot = None
        zRot = None
        
        for x in range(4):
            if x == 0:
                xRot = b
            else:
                xRot = self.rotate(xRot, 'x')
            for y in range(4):
                if y == 0:
                    yRot = xRot
                else:
                    yRot = self.rotate(yRot, 'y')
                for z in range(4):
                    if z == 0:
                        zRot = yRot
                    else:
                        zRot = self.rotate(zRot, 'z')

                    overlap = self.findOverlap(a, b)
            if overlap:
                return overlap
        return False

    def findOverlap(self, a: list, b: list):
        self.count += 1
        for beacon in a:
            oA = list(map(lambda x: x-beacon, a))
            for otherBeacon in b:
                oB = list(map(lambda x: x-otherBeacon, b))
                overlaps = len(set(oA) & set(oB))
                if overlaps >= 12:
                    return True

        return False


    def checkSame(self, located_scanner: scanner, unlocated_scanner: scanner):
        for rotation in self.rotations:
            rotated = self.rotate(unlocated_scanner.points, rotation)            

            counts = defaultdict(int)
    
            for p1 in rotated:
                for p2 in located_scanner.points:
                    counts[p2 - p1] += 1
    
            for k in counts:
                if counts[k] >= 12:
                    return True, k, rotated
    
        return False, None, None

if __name__ == '__main__':
    unittest.main()