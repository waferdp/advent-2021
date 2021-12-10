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
    points =0 
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
                stack = []
                points += pointsTable[char]
                break
    # if len(stack) > 0:
    #     for char in stack:
    #         points *= 5
    #         points += completeTable[char]
    return points

def testLine(line, expected):
    actual = parseLine(line)
    assert(expected == actual)

def test1():
    line = "{([(<{}[<>[]}>{[]{[(<()>"
    testLine(line, 1197)

def test2():
    line = "[[<[([]))<([[{}[[()]]]"
    testLine(line, 3)

def test3():
    line = "[{[{({}]{}}([{[{{{}}([]"
    testLine(line, 57)

def test4():
    line = "[<(<(<(<{}))><([]([]()"
    testLine(line, 3)

def test5():
    line = "<{([([[(<>()){}]>(<<{{"
    testLine(line, 25137)

def test6():
    lines = file.read("test_input.txt")
    points = 0
    for line in lines:
        points += parseLine(line)
    assert(points == 26397)

def run():
    lines = file.read("puzzle_input.txt")
    points = 0
    for line in lines:
        points += parseLine(line)
    return points

test1()
test2()
test3()
test4()
test5()
test6()

value = run()
print(value)