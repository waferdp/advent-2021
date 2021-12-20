import unittest
import readFile as file
from rotator import Rotator
from scanner import scanner
from main import Main
from vec3 import vec3

class testScanner(unittest.TestCase):
    def testParse(self):
        scanners = file.readScanners('test_input.txt')
        assert(len(scanners) == 5)

    def testRotate(self):
        scanners = file.readScanners('test_input.txt')
        rotator = Rotator()
        rotated = rotator.rotate(scanners[0], 'y')
        for i in range(0,len(scanners[0])):
            assert(rotated[i].x == scanners[0][i].z)
            assert(rotated[i].y == scanners[0][i].y)
            assert(rotated[i].z == scanners[0][i].x * -1)

    def testOverlap(self):
        scanners = file.readScanners('test_input.txt')
        rotator = Rotator()
        
        found, scannerPosition, rotation = rotator.checkSame(scanner(scanners[0]), scanner(scanners[1]))
        assert(found)
        assert(scannerPosition == vec3(68, -1246, -43))

    def testFindAllScanners(self):
        scanners = file.readScanners('test_input.txt')
        count = Main.run1(scanners)
        assert(count == 79)

    def testManhattan(self):
        scanners = file.readScanners('test_input.txt')
        mMax = Main.run2(scanners)
        assert(mMax == 3621)

if __name__ == '__main__':
    unittest.main()