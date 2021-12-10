from typing import DefaultDict
import readFile as file

pointsTable = DefaultDict ()
pointsTable[")"] = 3
pointsTable["]"] = 57
pointsTable["}"] = 1197
pointsTable[">"] = 25137

completeTable = DefaultDict()
completeTable[")"] = 1
completeTable["]"] = 2
completeTable["}"] = 3
completeTable[">"] = 4

def isIncrease(char):
    return char in "([{<" 

def getMatch(char):
    if char == "(":
        return ")"
    if char == "[":
        return "]"
    if char == "{":
        return "}"
    if char == "<":
        return ">"

def parseLine(line):
    points = 0 
    stack = []
    lookingFor = ""
    for char in line:
        if isIncrease(char):
            stack.append(lookingFor)
            lookingFor = getMatch(char)
        else:
            if char == lookingFor:
                lookingFor = stack.pop()
            else:
                points += pointsTable[char]
                return []
    stack.append(lookingFor)
    return stack 

def calculatePoints(stack):
    ordered = "".join(stack)[::-1]
    points = 0
    for char in ordered:
        points *= 5
        points += completeTable[char]
    return points

def getMiddle(points):
    points.sort()
    middle = int(len(points) /2)
    return points[middle]


def testLine(line, expected):
    actual = "".join(parseLine(line))[::-1]
    assert(expected == actual)

def test1():
    line = "[({(<(())[]>[[{[]{<()<>>"
    testLine(line, "}}]])})]")

def test2():
    line = "[(()[<>])]({[<{<<[]>>("
    testLine(line, ")}>]})")

def test3():
    line = "(((({<>}<{<{<>}{[]{[]{}"
    testLine(line, "}}>}>))))")

def test4():
    line = "{<[[]]>}<{[{[{[]{()[[[]"
    testLine(line, "]]}}]}]}>")

def test5():
    line = "<{([{{}}[<[[[<>{}]]]>[]]"
    testLine(line, "])}>")

def test6():
    lines = file.read("test_input.txt")
    points = []
    for line in lines:
        stack = parseLine(line)
        if len(stack) > 0:
            points.append(calculatePoints(stack))
    assert(getMiddle(points) == 288957)

def run():
    lines = file.read("puzzle_input.txt")
    points = []
    for line in lines:
        stack = parseLine(line)
        if len(stack) > 0:
            points.append(calculatePoints(stack))
    return getMiddle(points)

test1()
test2()
test3()
test4()
test5()
test6()

value = run()
print(value)