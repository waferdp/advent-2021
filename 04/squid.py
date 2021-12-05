import readFile as file
from bingo import bingo

def getBoards(inputLines):
    lines = inputLines.copy()
    lines.pop(0)
    boards = []
    board = bingo(1)

    
    for line in lines:
        numbers = line.split()
        if(len(numbers)):
            row = []
            for number in numbers:
                row.append(tile(number))
            board.rows.append(row)
        else:
            if board.any():
                board.build()
                index = board.index
                # print(board)
                boards.append(board)
                board = bingo(index + 1)
                
    if board.any():
        board.build()
        # print(board)
        boards.append(board)
    return boards

def getNumbers(lines):
    return lines[0].split(",")

def drawNumber(boards, number):
    temp = boards.copy()
    for board in boards:
        isBingo = board.draw(number)
        if isBingo:
            print("BINGO! board " + str(board.index) + " at " + number)
            if len(boards) == 1:
                print("Last board")
                print(boards[0].getUnmarkedSum() * int(number))

            #print(board.getUnmarkedSum() * int(number))
            temp.remove(board)
    return temp


def drawNumbers(boards, numbers):
    for number in numbers:
        boards = drawNumber(boards, number)


lines = file.read("puzzle_input.txt")
boards = getBoards(lines)
numbers = getNumbers(lines)
drawNumbers(boards, numbers)


