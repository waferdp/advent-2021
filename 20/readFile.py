import os
import sys

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
