import readFile as file

class total:
    one = 0
    zero = 0

    def update (self, bit):
        if(bit == "1"):
            self.one += 1
        elif(bit == "0"):
            self.zero += 1

    def __str__(self):
        return "1: " + str(self.one) + ", 0: " + str(self.zero)


def getHigher(total):
    if total.one >= total.zero:
        return "1"
    else:
        return "0"

def getLower(total):
    if total.zero <= total.one:
        return "0"
    else:
        return "1"


def getBitList(str):
	return [bit for bit in str]

def calculateBit (totalBit, bits):
    for bit in bits:
        totalBit.update(bit)

def bitsAtI(lines, i):
    bits = []
    for line in lines:
        bits.append(line[i])
    return bits

def filter(lines, bit, index):
    remaining = []
    for line in lines:
        if line[index] == bit:
            remaining.append(line)
    return remaining

def calculateBits(lines, fn):
    remaining = lines.copy()
    length = len(lines[0])
    #bits = "0b"
    for i in range(0, length):
        totalBit = total()
        calculateBit(totalBit, bitsAtI(remaining, i))
        derivate = fn(totalBit)
        remaining = filter(remaining, derivate, i)
        if len(remaining) == 1:
            return remaining[0]

def addLine(total, line):
    bits = getBitList(line)
    for i in range(len(bits)):
        total[i].update(bits[i])

def initTotal(firstLine):
    length = len(firstLine)
    totals = []
    for i in range(length):
        totals.append(total())
    return totals

lines = file.read("puzzle_input.txt")
gamma = calculateBits(lines, getHigher)
epsilon = calculateBits(lines, getLower)

value = int(gamma, 2) * int(epsilon, 2)

print(gamma)
print(epsilon)
print(value)

# value in 1 = 1540244