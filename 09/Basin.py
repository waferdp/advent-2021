class Basin:
    visited = {}
    matrix = None

    def __init__(self, matrix) -> None:
        self.visited = {}
        self.matrix = matrix

    def add(self, x,y):
        if y not in self.visited:
            self.visited[y] = {}
        self.visited[x] += 1

    def isVisited(self, x,y):
        if y not in self.visited:
            return False
        return x in self.visited

    def getEdges(self):
        edges = []

