import unittest
from Decoder import Main

class TestDecoder(unittest.TestCase):

    def quickTest(self, input, expected):
        value = Main.run(input)
        assert(value == expected)

    def testLiteral(self):
        self.quickTest('D2FE28', 2021)

    def testSum(self):
        self.quickTest('C200B40A82', 3)

    # def testProduct(self):
    #     self.quickTest('04005AC33890', 54)
        
    def testMin(self):
        self.quickTest('880086C3E88112', 7)

    def testMax(self):
        self.quickTest('CE00C43D881120', 9)

    def testLessThan(self):
        self.quickTest('D8005AC2A8F0', 1)
        
    def testNotGreaterThan(self):
        self.quickTest('F600BC2D8F', 0)
    
    def testNotEqualTo(self):
        self.quickTest('9C005AC2F8F0', 0)

    def testMultiple(self):
        self.quickTest('9C0141080250320F1802104A08', 1)

if __name__ == '__main__':
    unittest.main()