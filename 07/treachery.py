import readFile as file
from enum import Enum

class Direction(Enum):
    LEFT = -1
    RIGHT = 1


def createCostDict(high):
    costs = {}
    costs[0] = 0
    
    for i in range(1, high+1):
        costs[i] = costs[i-1] + i
    return costs

def bruteForceCost(crabs, costs):
    low = min(crabs)
    high = max(crabs)
    lowestCost = None

    for i in range(low , high):
        cost = calculateCost(crabs, costs, i)
        if lowestCost is None or cost < lowestCost:
            lowestCost = cost
    return lowestCost

def calculateCost(crabs, costs, position):
    cost = 0
    for crab in crabs:
        distance = abs(crab - position)
        cost += costs[distance]
    return cost

def calcMiddle(large, small):
    return int( (large - small) / 2 )

def test1():
    input = file.readSingleSeparated("test_input.txt")
    costs = createCostDict(max(input))
    cost = calculateCost([16], costs, 5)
    assert(cost == 66)

def test2():
    input = file.readSingleSeparated("test_input.txt")
    costs = createCostDict(max(input))
    cost = bruteForceCost(input, costs)
    assert(cost == 168)

def run():
    input = file.readSingleSeparated("puzzle_input.txt")
    costs = createCostDict(max(input))
    cost = bruteForceCost(input, costs)
    return cost

test1()
test2()
cost = run()
print(cost)