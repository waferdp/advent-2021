import readFile as file 
from functools import reduce
class Decoder:
    hex = ""
    bits = ""
    versions = []

    def __init__(self, hex) -> None:
        self.hex = hex
        self.versions = []

    def decode(self):
        if self.hex[0] == '0':
            self.bits = '0000'
            self.hex[1:]
        self.bits += bin(int(self.hex, 16))[2:]
        return self.nextPacket()
        

    def nextPacket(self):
        version, type = self.decodeHeader()
        self.versions.append(version)
        if type == 0:
            return sum(self.decodeOperator())
        elif type == 1:
            return reduce(lambda x, y: x * y, self.decodeOperator())
        elif type == 2:
            return min(self.decodeOperator())
        elif type == 3:
            return max(self.decodeOperator())
        elif type == 4:
            return self.decodeLiteralValue()
        elif type == 5:
            first, second = self.decodeOperator()
            if first > second:
                return 1
            else: 
                return 0
        elif type == 6:
            first, second = self.decodeOperator()
            if first < second:
                return 1
            else: 
                return 0
        else:
            first, second = self.decodeOperator()
            if first == second:
                return 1
            else: 
                return 0


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
                result = self.nextPacket()
                packets.append(result)
        else:
            amount = self.popValueFromBits(11)
            for i in range(amount):
                result = self.nextPacket()
                packets.append(result)
        return packets
        
class Main():
    def run(input):
        decoder = Decoder(input)
        return decoder.decode()

if __name__ == '__main__':
    # unittest.main()

    input = file.read('puzzle_input.txt')[0]
    result = Main.run(input)
    print(result)