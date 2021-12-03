import os
import sys

def open(file):
    path = os.path.join(sys.path[0], file)
    return open(path)

def read(file):
    lines = []
    with open(file) as f:
        lines = f.readLines()
    return lines