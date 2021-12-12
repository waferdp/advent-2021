import unittest

class TestEdge(unittest.TestCase):
     
    def testEquality(self):
        a = Edge("a", "b")
        a2 = Edge("a", "b")
        assert(a == a2)
    
    def testNotEquality(self):
        a = Edge("a", "b")
        b = Edge("b", "a")
        assert(a != b)

    def testArrayEquality(self):
        a = Edge("a", "b")
        a2 = Edge("a", "b")
        assert (a2 in [a])

    def testArrayInEquality(self):
        a = Edge("a", "b")
        b = Edge("b", "a")
        assert (b not in [a])


class Edge:
    org = None
    dest = None

    def __init__(self, org, dest) -> None:
        self.org = org
        self.dest = dest

    def __eq__(self, __o: object) -> bool:
        return __o.org == self.org and __o.dest == self.dest

    def __repr__(self) -> str:
        return self.org + ' -> ' + self.dest

if __name__ == '__main__':
    unittest.main()