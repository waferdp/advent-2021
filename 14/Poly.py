from typing import DefaultDict, Dict
import unittest
import readFile as file

class TestPoly(unittest.TestCase):
    def testPairs(self):
        input = "NNCB"
        pairs = Poly.findPairs(input)
        assert(len(pairs) == 3)

    def testCount(self):
        input = file.read("test_input.txt")
        poly = Poly(input)
        poly.grow(10)
        assert(poly.count['B'] == 1749)
        assert(list(poly.reverse.keys())[-1] == 1749)
        
    def testRun1(self):
        input = file.read("test_input.txt")
        diff = Main.run(input, 10)
        assert(diff == 1588)

    def testRun2(self):        
        input = file.read("test_input.txt")
        diff = Main.run(input, 40)
        assert(diff == 2188189693529)

class Poly:
    polymer : str = ""
    occurs = {}

    def __init__(self, input) -> None:
        self.polymer = input[0]
        self.instructions = self.__findInstructions(input)
        pairs = Poly.findPairs(self.polymer)
        
        self.occurs = {}
        for pair in pairs:
            self.occurs[pair] = self.polymer.count(pair)

    def __findInstructions(self, input) -> dict:
        instructions = {}
        for row in input:
            if "->" in row:
                pair, insert = map(lambda x: x.strip(), row.split(" -> "))
                instructions[pair] = insert
        return instructions

    def findTemplate(input):
        return input[0]

    def findPairs(template):
        pairs = []
        for i in range(0, len(template)-1):
            pairs.append(template[i] + template[i+1])
        return pairs
        
    def grow(self, steps):
        
        for i in range(steps):
            nextStep = DefaultDict(int)
            for pair in self.occurs:
                left, right = pair
                next = self.instructions[pair]
                occurs = self.occurs[pair]
                nextStep[left + next] += occurs
                nextStep[next + right] += occurs
            self.occurs = nextStep
        self.count()

    def count(self):
        counts = DefaultDict(int)
        for key in self.occurs:
            left = key[0]
            counts[left] += self.occurs[key]
        counts[self.polymer[-1]] += 1
        self.count = counts

        self.reverse = {}
        for c in sorted(self.count, key=self.count.get):
            self.reverse[self.count[c]] = c


class Main:
    def run(input, steps):
        poly = Poly(input)
        poly.grow(steps)
        most = list(poly.reverse.keys())[-1]
        least = list(poly.reverse.keys())[0]
        return most - least

if __name__ == '__main__':
    unittest.main()

    input = file.read('puzzle_input.txt')
    result = Main.run(input, 40)
    print(result)
    