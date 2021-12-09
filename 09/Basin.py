from Matrix import Matrix
from Point2d import Point2d

class Basin:
    visited = {}
    matrix = None
    center = None

    def __init__(self, matrix: Matrix, center: Point2d) -> None:
        self.visited = {}
        self.matrix = matrix
        if matrix is not None:
            self.center = center
        if center is not None:
            self.add(center.x, center.y)


    def add(self, x,y):
        if y not in self.visited:
            self.visited[y] = {}
        if x not in self.visited[y]:
            self.visited[y][x] = 1
        self.visited[y][x] += 1

    def isVisitable(self, x, y):
        if y in self.visited:
            if x in self.visited[y]:
                return False
        return self.matrix.get(x,y) < 9

    def findNext(self, x,y):

        if self.isVisitable(x, y-1):
            self.add(x, y-1)
            self.findNext(x, y-1)

        if self.isVisitable(x+1, y):
            self.add(x+1, y)
            self.findNext(x+1,y)

        if self.isVisitable(x, y+1):
            self.add(x, y+1)
            self.findNext(x, y+1)
        
        if self.isVisitable(x-1, y):
            self.add(x-1, y)
            self.findNext(x-1, y)

    def exploreBasin(self):
        self.findNext(self.center.x, self.center.y)

    def getVisited(self):
        visited = []
        for y in self.visited:
            for x in self.visited[y]:
                visited.append(Point2d(x, y, self.matrix.get(x,y)))
        return visited