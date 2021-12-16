import unittest
import readFile as file 

class TestDecode(unittest.TestCase):

    # def testLiteral(self):
    #     input = 'D2FE28'
    #     decoder = Decoder(input)
    #     value = decoder.decode()
    #     decoded = 

    def testOperator1(self):
        input = '8A004A801A8002F478'
        decoded = Main.run1(input)
        assert(decoded == 16)   

    # def testOperator2(self):
    #     input = '620080001611562C8802118E34'
    #     decoded = Main.run1(input)
    #     assert(decoded == 12)   

    def testOperator3(self):
        input = 'C0015000016115A2E0802F182340'
        decoded = Main.run1(input)
        assert(decoded == 23)   

    def testOperator4(self):
        input = 'A0016C880162017C3686B18A3D4780'
        decoded = Main.run1(input)
        assert(decoded == 31) 

class Decoder:
    hex = ""
    bits = ""
    versions = []

    def __init__(self, hex) -> None:
        self.hex = hex
        self.versions = []

    def decode(self):
        self.bits = bin(int(self.hex, 16))[2:]
        while "1" in self.bits:
            self.nextPacket()
        return sum(self.versions)
        

    def nextPacket(self):
        version, type = self.decodeHeader()
        self.versions.append(version)
        if type == 4:
            return self.decodeLiteralValue()
        else:
            return self.decodeOperator()

    def decodeHeader(self):
        version = self.popValueFromBits(3)
        type = self.popValueFromBits(3)
        return (version, type)

    def popValueFromBits(self, length):
        return int(self.popFromBits(length), 2) 

    def popFromBits(self, length):
        popped = self.bits[:length]
        self.bits = self.bits[length:]
        return popped

    def decodeLiteralValue(self):
        value = ""
        while True:
            part = self.popFromBits(5)
            value += part[1:]
            if part[0] == '0':
                break
        return int(value, 2)

    def decodeOperator(self):
        mode = self.popFromBits(1)
        length = 0
        packets = []
        if mode == "0":
            length = self.popValueFromBits(15)
            left = len(self.bits)
            while len(self.bits) > left - length and '1' in self.bits :
                self.nextPacket()
        else:
            packets = self.popValueFromBits(11)
            for i in range(packets):
                self.nextPacket()
        return 
        
class Main():
    def run1(input):
        decoder = Decoder(input)
        return decoder.decode()


if __name__ == '__main__':
    #unittest.main()

    input = file.read('puzzle_input.txt')[0]
    result = Main.run1(input)
    print(result)