import readFile as file
from Fish import Fish

def createFishes(line):
    fishes = {}
    fishAges = line.split(",")
    for fishAge in fishAges:
        parsed = int(fishAge)
        if parsed in fishes:
            fishes[parsed] += 1 
        else:
            fishes[parsed] = 1
    return fishes

def cascade(fishes):
    nextDay = {}
    nextDay[6] = 0
    for key in fishes:
        if key == 0:
            nextDay[6] += fishes[0]
            nextDay[8] = fishes[0]
        elif key == 7:
            nextDay[6] += fishes[7]
        else:
            nextDay[key-1] = fishes[key]
    return nextDay

def simulate(fishes, days):
    for day in range(0,days):
        fishes = cascade(fishes)
        
        #printFishes(fishes)
    count = 0
    for day in fishes:
        count += fishes[day]
    return count

def printFishes(fishes):
    string = ""
    for fish in fishes:
        string += str(fish) + ","
    print(string)

def runTest(path, days):
    lines = file.read(path)
    fishes = createFishes(lines[0])
    result = simulate(fishes, days)
    return result
 
def test2():
    result = runTest("test_input.txt", 80)
    print(result)
    assert(5934 == result)
    print("Test2 OK")

def test3():
    result = runTest("puzzle_input.txt", 80)
    print(result)
    assert(372300 == result)
    print("Test3 OK")

def test1():
    result = runTest("test_input.txt", 18)
    print(result)
    assert(result == 26)
    print("Test1 OK")

def run():
    result = runTest("puzzle_input.txt", 256)
    return result

test1()
test2()
test3()
result = run()
print(result)