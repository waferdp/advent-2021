from typing import Dict
import unittest
import time
import readFile as file

class TestPoly(unittest.TestCase):
    def testOneStep(self):
        input = file.read("test_input.txt")
        poly = Poly(input)
        poly.grow(1)
        assert(poly.polymer == "NCNBCHB")

    def testFourSteps(self):
        input = file.read("test_input.txt")
        poly = Poly(input)
        poly.grow(4)
        assert(poly.polymer == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

    def testTenSteps(self):
        input = file.read("test_input.txt")
        poly = Poly(input)
        poly.grow(10)
        assert(len(poly.polymer) == 3073)

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

    # def testRun2(self):        
    #     input = file.read("test_input.txt")
    #     start = time.time()
    #     diff = Main.run(input, 26)
    #     done = time.time()
    #     print ("26 steps: " + str(done - start))
    #     #assert(diff == 1588)

class Poly:
    instructions = {}
    polymer = ""

    def __init__(self, input) -> None:
        self.polymer = input[0]
        self.instructions = self.__findInstructions(input)
        self.elements = list(set(self.instructions.values())) 

    def __findInstructions(self, input) -> dict:
        instructions = {}
        for row in input:
            if "->" in row:
                pair, insert = map(lambda x: x.strip(), row.split("->"))
                instructions[pair] = insert
        return instructions

    def findTemplate(input):
        return input[0]

    def step(self, template):
        result = ""
        for i in range(0, len(template)-1):
            pair = template[i] + template[i+1]
            instruction = self.instructions[pair]
            result += pair[0] + instruction
        return result + template[-1]

    def grow(self, steps):
        for i in range(steps):
            self.polymer = self.step(self.polymer)
            #print("Step " + str(i))
        self.count()

    def count(self):
        self.count = {}
        for element in self.elements:
            self.count[element] = self.polymer.count(element)

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

    # input = file.read('puzzle_input.txt')
    # result = Main.run(input, 40)
    # print(result)
    