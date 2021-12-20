import os
import sys
from vec3 import vec3 

def read(file):
    path = os.path.join(sys.path[0], file)
    lines = []
    with open(path, "r") as f:
        rawLines = f.readlines()
    for line in rawLines:
        lines.append(line.rstrip())
    return lines

def readSingleSeparated(file) -> list:
    lines = read(file)
    line = lines[0]
    separated = []
    for number in line.split(","):
        separated.append(int(number))
    return separated

def readScanners(file) -> list:
    lines = read(file)
    scanners = []
    beacons = []
    for line in lines:
        if '--- scanner ' in line:
            if len(beacons):
                scanners.append(beacons)
                beacons = []
        elif line.strip() == '':
            continue
        else:
            x,y,z = map(lambda a: int(a), line.split(','))
            beacons.append(vec3(x,y,z))
    if len(beacons):
        scanners.append(beacons)
    return scanners
