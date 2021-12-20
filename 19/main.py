from vec3 import vec3
from scanner import scanner
from rotator import Rotator
import readFile as file
import itertools

class Main:

    def run1(input):
        scanners = Main.locate(input)
        points = set()

        for scanner in scanners:
            points.update(scanner.points)
        
        return len(points)

    def run2(input):
        mMax = 0
        scanners = Main.locate(input)
        combinations = list(itertools.combinations(scanners, 2))
        for s1, s2 in combinations:
            mMax = max(mMax, s1.position.manhattan(s2.position), s2.position.manhattan(s1.position))
        return mMax

    def locate(input):
        rotator = Rotator()
        scanners = []
        total = len(input)

        found = [ scanner(input.pop(0), vec3(0,0,0)) ]
        for beacons in input:
            scanners.append(scanner(beacons))
        
        last = len(found)
        while len(found) < total:
            if len(found) > last:
                print(len(found))
                last = len(found)
            for unlocated in scanners:
                isFound = False
                if unlocated.position is not None:
                    found.append(unlocated)
                    scanners.remove(unlocated)
                    continue
                for located in found:
                    isFound, location, rotation = rotator.checkSame(located, unlocated)

                    if not isFound:
                        continue
                    
                    newFoundScanner = scanner.createWithOffset(location, rotation)
                    found.append(newFoundScanner)
                    if unlocated in scanners: 
                        scanners.remove(unlocated)
                    break
                if isFound:
                    break
        return found


if __name__ == '__main__':
   
    input = file.readScanners('puzzle_input.txt')
    #count = Main.run1(input)
    mMax = Main.run2(input)
    print(mMax)