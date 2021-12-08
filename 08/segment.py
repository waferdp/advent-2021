import readFile as file

def countDigit(digits, length):
    count = 0
    for digit in digits:
        if len(digit) == length:
            count += 1
    return count

def getInputDigits(line):
    output = line.split("|")
    return output[0].split()

def getOutputDigits(line):
    output = line.split("|")
    return output[1].split()

def findDigit(digits, length):
    for digit in digits:
        if len(digit) == length:
            return digit
    return None

def cleanDigits(digits, numbers):
    for i in numbers:
        if numbers[i] in digits:
            digits.remove(numbers[i])
    return digits

def findNine(numbers, digits):
    almostNine = getCombination(numbers[4], numbers[7])
    for digit in digits:
        if len(digit) == 6 and isSubstringOf(almostNine, digit):
            return digit

def findThree(numbers, digits):
    nine = numbers[9]
    one = numbers[1]
    for digit in digits:
        if len(digit) == 5 and isSubstringOf(digit, nine) and isSubstringOf(one, digit):
            return digit

def findZero(numbers, digits):
    eight = numbers[8]
    one = numbers[1]
    for digit in digits:
        if len(digit) == 6 and isSubstringOf(digit, eight) and isSubstringOf(one, digit):
            return digit

def findSix(digits):
    for digit in digits:
        if len(digit) == 6:
            return digit

def findFive(numbers, digits):
    six = numbers[6]
    for digit in digits:
        if len(digit) == 5 and isSubstringOf(digit, six):
            return digit

def findNumbers(line):
    numbers = {}
    digits = getInputDigits(line)

    #Easy
    numbers[1] = findDigit(digits, 2)
    numbers[4] = findDigit(digits, 4)
    numbers[7] = findDigit(digits, 3)
    numbers[8] = findDigit(digits, 7)
    digits = cleanDigits(digits, numbers)

    #Medium
    numbers[9] = findNine(numbers, digits)
    numbers[3] = findThree(numbers, digits)

    #Tricky 
    digits = cleanDigits(digits, numbers)
    numbers[0] = findZero(numbers, digits)
    cleanDigits(digits, numbers)
    numbers[6] = findSix(digits)
    cleanDigits(digits, numbers)

    #Most tricky
    numbers[5] = findFive(numbers, digits)
    cleanDigits(digits, numbers)
    numbers[2] = digits[0]
    return numbers

def findSegments(numbers):
    segments = {}

    segments['a'] = findDiff(numbers[7], numbers[1])
    segments['b'] = findDiff(numbers[4], numbers[3])
    segments['c'] = findDiff(numbers[1], numbers[5])
    segments['d'] = findDiff(numbers[8], numbers[0])
    segments['e'] = findDiff(numbers[8], numbers[9])
    segments['f'] = findDiff(numbers[3], numbers[2])
    segments['g'] = findDiff(findDiff(numbers[3], numbers[4]), numbers[7])

    return segments

def whatNumber(numbers, digit):
    for i in numbers:
        if areEqual(numbers[i], digit):
            return str(i)

def findDiff(long, short):
    for letter in short:
        long = long.replace(letter, "")
    return long

def getCombination(long, short):
    for letter in short:
        if letter not in long:
            long += letter
    return long

def isSubstringOf(subString, fullString):
    for letter in subString:
        if letter not in fullString:
            return False
    return True

def areEqual(a, b):
    if len(a) != len(b):
        return False
    for letter in a:
        if letter not in b:
            return False
    return True

def deduceSegments(digits):
    segments = []
    segments['a'] = findDiff(digits[7], digits[1])


def decodeLine(line, numbers):
    digits = getOutputDigits(line)
    output = ""
    for digit in digits:
        output += whatNumber(numbers, digit)
    return output

def sumLines(lines):
    sum = 0
    for line in lines:
        numbers = findNumbers(line)
        sum += int(decodeLine(line, numbers))
    return sum

def testStrings():
    a = "hello"
    b = a
    b = b.replace("l", "")
    assert(a != b)

def testDiff():
    seven = "acf"
    one = "cf"
    diff = findDiff(seven, one)
    assert(seven == "acf")
    assert (diff == "a")

def testCombine():
    four = "bcdf"
    seven = "acf"
    combination = getCombination(four, seven)
    assert("bcdfa" == combination)

def testFind():
    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    numbers = findNumbers(line)
    assert(numbers[1] == "ab")
    assert(numbers[4] == "eafb")
    assert(numbers[7] == "dab")
    assert(numbers[8] == "acedgfb")
    assert(numbers[9] == "cefabd")
    assert(numbers[3] == "fbcad")
    assert(numbers[0] == "cagedb")
    assert(numbers[6] == "cdfgeb")
    assert(numbers[5] == "cdfbe")
    assert(numbers[2] == "gcdfa")

def testSegments():
    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    numbers = findNumbers(line)
    segments = findSegments(numbers)
    assert(segments['a'] == 'd')
    assert(segments['b'] == 'e')
    assert(segments['c'] == 'a')
    assert(segments['d'] == 'f')
    assert(segments['e'] == 'g')
    assert(segments['f'] == 'b')
    assert(segments['g'] == 'c')


def testDecode():
    line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    numbers = findNumbers(line)
    decoded = decodeLine(line, numbers)
    assert(decoded == "5353")

def test1():
    lines = file.read("test_input.txt")
    sum = sumLines(lines)
    assert(sum == 61229)


def run():
    lines = file.read("puzzle_input.txt")
    return sumLines(lines)

testStrings()
testDiff()
testCombine()
testFind()
testSegments()
testDecode()
test1()
value = run()
print(value)