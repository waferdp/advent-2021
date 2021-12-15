import unittest
import heapq
from Point2d import Point2d
from Matrix import Matrix
import readFile as file

class TestChiton(unittest.TestCase):
    def testHeapq(self):
        a = Point2d(10,10,1)
        b = Point2d(2,2,2)
        heap = [a, b]
        heapq.heapify(heap)
        smallest = heapq.heappop(heap)
        assert(smallest == a)
    
    def testSmall1(self):
        input = file.read("test_input.txt")
        risk = Main.run1(input)
        assert(risk == 40)

    def testSmall2(self):
        input = file.read("test_input.txt")
        risk = Main.run2(input)
        assert(risk == 315)

class Chiton:
    matrix = None
    visited = []
    lastVisited = None
    routes = []
    visitable = []
    destination = None

    def __init__(self, matrix: Matrix, destination: Point2d) -> None:
        self.matrix = matrix
        self.lastVisited = Point2d(0, 0, 0)
        self.visited = Matrix.generate(matrix.width, matrix.height)
        self.visited.set(self.lastVisited.x, self.lastVisited.y)

        self.destination = destination

    def navigate(self):
        count = 0
        while self.lastVisited != self.destination:
            count += 1 
            self.addNext()
            self.step()
            if count % 1000 == 0:
                print(str(count) + ": " + str(self.lastVisited))
        return self.lastVisited.value


    def addNext(self):
        last = self.lastVisited

        #Clockwise add directions
        next = []
        next.append(self.matrix.above(last.x, last.y)) 
        next.append(self.matrix.right(last.x, last.y)) 
        next.append(self.matrix.below(last.x, last.y)) 
        next.append(self.matrix.left(last.x, last.y))

        good = []
        for item in next:
            item.value += last.value
            if item.value < Matrix.inf():
                if not self.visited.contains(item):
                    good.append(item)

        #next = list(filter(lambda x: x.value < Matrix.inf() and not self.visited.contains(x), next))
        self.visitable += good

    def step(self):
        heapq.heapify(self.visitable)
        self.lastVisited = heapq.heappop(self.visitable)
        self.visited.set(self.lastVisited.x, self.lastVisited.y)
        self.visitable = list(filter(lambda x: not self.visited.contains(x), self.visitable))

class Main:
    def run1(input):
        matrix = Matrix(input)
        chiton = Chiton(matrix, Point2d(matrix.width-1, matrix.height-1))
        return chiton.navigate()

    def run2(input):
        matrix = Matrix(input)
        matrix.multiplyRight(5)
        matrix.multiplyDown(5)
        chiton = Chiton(matrix, Point2d(matrix.width-1, matrix.height-1))
        return chiton.navigate()
        

if __name__ == '__main__':
    #unittest.main()

    input = file.read('puzzle_input.txt')
    result = Main.run2(input)
    print(result)