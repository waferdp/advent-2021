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

    def findEdges(self, org, traversed):
        if(org == 'end'):
            return []
        withOrigin = list(filter(lambda x: x.org == org, self.edges))
        upperCaseAllowed = list(filter(lambda x: x.islower(), traversed))
        goodEdges = list(filter(lambda x: x.dest not in upperCaseAllowed, withOrigin))
        
        return goodEdges

if __name__ == '__main__':
    unittest.main()