from Graph import Graph
import unittest
import readFile as file

class TestPassage(unittest.TestCase):
    def testSmall(self):
        input = ['start-A', 'start-b', 'A-b', 'A-c', 'b-d', 'A-end', 'b-end']
        allPaths = Main.run1(input)
        assert(allPaths == 36)

    def testMedium(self):
        input = ['dc-end', 'HN-start', 'start-kj', 'dc-start', 'dc-HN', 'LN-dc', 'HN-end', 'kj-sa', 'kj-HN', 'kj-dc']
        allPaths = Main.run1(input)
        assert(allPaths == 103)

    def testLarge(self):
        input = ['fs-end', 'he-DX', 'fs-he', 'start-DX', 'pj-DX', 'end-zg', 'zg-sl', 'zg-pj', 'pj-he']
        input += ['RW-he', 'fs-DX', 'pj-RW', 'zg-RW', 'start-pj', 'he-WI', 'zg-he', 'pj-fs', 'start-RW']
        allPaths = Main.run1(input)
        assert(allPaths == 3509)

class Passage:
    
    path = []
    graph = None
    allPaths = None

    def __init__(self, path, graph, allPaths):
        self.path = path
        if self.graph is None:
            self.graph = graph
        if self.allPaths is None:
            self.allPaths = allPaths

    def traverse(self):
        edges = self.graph.findEdges(self.path[-1], self.path)
        if len(edges) == 0:
            if self.path[-1] == 'end':
                self.allPaths.append(self.path)
        for edge in edges:
            newPassage = Passage(self.path + [edge.dest], self.graph, self. allPaths)
            newPassage.traverse()
            
class Main:
    def run1(input):
        graph = Graph(input)
        allPaths = []
        passage = Passage(['start'], graph, allPaths)
        passage.traverse()
        return len(allPaths)

if __name__ == '__main__':
    # unittest.main()

    input = file.read('puzzle_input.txt')
    paths = Main.run1(input)
    print(paths)