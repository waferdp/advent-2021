import unittest
import readFile as file

class testScanner(unittest.TestCase):
    def testParse(self):
        scanners = file.readScanners('test_input.txt')
        assert(len(scanners) == 5)

if __name__ == '__main__':
    unittest.main()