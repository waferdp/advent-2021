import readFile as file
from enum import Enum

class Direction(Enum):
    LEFT = -1
    RIGHT = 1


def createCostDict(high):
    costs = {}
    costs[0] = 0
    
    for i in range(1, high):
        costs[i] = costs[i-1] + 1
    return costs

def bruteForceCost(crabs, costs):
    low = min(crabs)
    high = max(crabs)
    lowestCost = None

    for i in range(low , high):
        cost = calculateCost(crabs, i)
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

def findBestSpot(input):
    smallest = min(input)
    largest = max(input)
    middle = calcMiddle(largest, smallest)
    cost = calculateCost(input, middle)

    leftCost = findRecurse(input, cost, smallest, middle, Direction.LEFT)
    rightCost = findRecurse(input, cost, middle, largest, Direction.RIGHT)

    return min([cost, leftCost, rightCost])

def findRecurse(input, baseCost, small, large, lastdir):
    
    middle = calcMiddle(large, small)
    cost = calculateCost(input, middle)

    if baseCost <= cost:
        if lastdir == Direction.LEFT:
            if calcMiddle(large, middle) - middle < 1:
                return baseCost
            else:
                rightCost = findRecurse(input, cost, middle, large, Direction.RIGHT)
                return min([baseCost, rightCost])
        elif lastdir == Direction.RIGHT:
            if middle - calcMiddle(middle, small) < 1:
                return baseCost
            else:
                leftCost = findRecurse(input, cost, small, middle, Direction.LEFT)
                return min([baseCost, leftCost])
    else:
        leftCost = findRecurse(input, cost, small, middle, Direction.LEFT)
        rightCost = findRecurse(input, cost, middle, large, Direction.RIGHT)
        return min([cost, leftCost, rightCost])

def test1():
    input = file.readSingleSeparated("test_input.txt")
    costs = createCostDict(max(input))
    cost = calculateCost([16], 5)
    assert(cost == 66)

def test2():
    input = file.readSingleSeparated("test_input.txt")
    costs = createCostDict(max(input))
    cost = bruteForceCost(input)
    assert(cost == 37)

def run():
    input = file.readSingleSeparated("puzzle_input.txt")
    costs = createCostDict(max(input))
    cost = bruteForceCost(input)
    return cost

test1()
test2()
cost = run()
print(cost)