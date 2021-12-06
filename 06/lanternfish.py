import readFile as file
from Fish import Fish

def createFishes(line):
    fishes = []
    fishAges = line.split(",")
    for fishAge in fishAges:
        fish = Fish(int(fishAge))
        fishes.append(fish)
    return fishes

def simulate(fishes):
    for day in range(0,80):
        fishesToday = fishes.copy()
        for fish in fishesToday:
            aNewFish = fish.nextDay()
            if aNewFish is not None:
                fishes.append(aNewFish)
        
        #printFishes(fishes)
    return len(fishes)

def printFishes(fishes):
    string = ""
    for fish in fishes:
        string += str(fish) + ","
    print(string)

def test():
    lines = file.read("test_input.txt")
    fishes = createFishes(lines[0])
    result = simulate(fishes)
    assert(5934 == result)

def run():
    lines = file.read("puzzle_input.txt")
    fishes = createFishes(lines[0])
    result = simulate(fishes)
    return result

test()
result =run()
print(result)