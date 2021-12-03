from vector import vector
import readFile

def addChange(a, b):
    sum = vector()
    sum.horizontal = a.horizontal + b.horizontal
    sum.depth = a.depth + b.depth
    sum.aim = a.aim + b.aim
    return sum

def parseInstruction(line, aim):
    change = vector()
    words = line.split()
    instruction = words[0]
    value = int(words[1])
    if instruction == "forward":
        change.horizontal += value
        change.depth = value * aim
    elif instruction == "down":
        change.aim += value
    elif instruction == "up":
        change.aim -= value
    return change

def readInstructions(lines):
    position = vector()
    for line in lines:
        change = parseInstruction(line, position.aim)
        position = position.add(change)
    return(position)


lines = readFile.read("test_input.txt")
position = readInstructions(lines)
print('Horizontal: ' + str(position.horizontal))
print('Depth: ' + str(position.depth))
multiple = position.horizontal * position.depth
print (str(multiple))