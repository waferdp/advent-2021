def formatLines(lines):
    formatted = []
    for line in lines:
        value = int(line)
        formatted.append(value)
    return formatted

def getWindow(lines, index):
    if index + 2 < len(lines):
        return lines[index] + lines[index + 1] + lines[index + 2]

def countIncrements(lines):
    
    currentValue = 1000000
    increments = 0
    for i in range(len(lines)):
        value = getWindow(lines, i)
        if value is not None and value > currentValue:
           increments += 1
        currentValue = value 
    return increments

f = open("01_input.txt")
lines = formatLines(f.readlines())
increments = countIncrements(lines)
print(increments)
