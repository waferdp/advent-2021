import unittest
from Edge import Edge

class TestGraph(unittest.TestCase):
    def testMap(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        assert(len(graph.nodes) == 6)
        assert(len(graph.edges) == 14)

    def testOrigins(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("A", ["start"])
        assert(len(edges) == 3)

    def testTerminates(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("end", ["start", "b", "end"])
        assert(len(edges) == 0)

    def testReVisit(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("c", ["start", "A", "c"])
        assert(len(edges) > 0)

    def testStopVisit(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("A", ["start", "A", "c", "A", "c", "A"])
        assert(len(edges) == 2)

    def testOnlyFirstSmallCase(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("A", ["start", "A", "c", "A", "c", "A", "b", "A"])
        assert(len(edges) == 1)
        
    def testFindBug1(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("A", ["start", "A", "b", "A", "c", "A"])
        assert(len(edges) == 3)

    def testFindBug1(self):
        input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
        graph = Graph(input)
        edges = graph.findEdges("A", ['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A'])
        assert(len(edges) == 1)
        

class Graph:
    nodes = []
    edges = []

    def __init__(self, input):
        self.nodes = []
        self.edges = []

        for row in input:

            nodes = row.split("-")
            org = nodes[0]
            dest = nodes[1]
            edge = Edge(org, dest)
            reverse = Edge(dest, org)

            if org not in self.nodes:
                self.nodes.append(org)
            if dest not in self.nodes:
                self.nodes.append(dest)

            if edge not in self.edges:
                self.edges.append(edge)
            if reverse not in self.edges:
                self.edges.append(reverse)

    def filterLowerCase(traversed):
        hasDoubleSmallCase = len(traversed) > len(set(traversed))

        if hasDoubleSmallCase:
            return traversed
        else:
            return ['start']
            

    def findEdges(self, org, traversed):
        if(org == 'end'):
            return []
        upperCaseAllowed = list(filter(lambda x: x.islower(), traversed))
        lowerCaseAllowedOnce = Graph.filterLowerCase(upperCaseAllowed)
        withOrigin = list(filter(lambda x: x.org == org, self.edges))
        goodEdges = list(filter(lambda x: x.dest not in lowerCaseAllowedOnce, withOrigin))
        
        return goodEdges

if __name__ == '__main__':
    unittest.main()