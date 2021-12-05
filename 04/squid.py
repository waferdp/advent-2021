import readFile as file

class tile:
    number = 0
    checked = False

    def __init__(self, number):
        self.number = number
        self.checked = False

    def __str__(self):
        if self.checked:
            return "*" + str(self.number) + "*"
        else:
            return str(self.number)

class bingo:

    index = 0
    rows = []
    checkedRows = []
    columns = []   
    checkedColumns = []
    haswon = False

    def __init__(self, index):
        self.rows = []
        self.columns = []
        self.index = index

    def build(self):
        width = len(self.rows[0])
        for i in range(0, width):
            column = []
            for row in self.rows:
                column.append(row[i])
            self.columns.append(column)

    def allChecked(rowOrColumn):
        areChecked = True
        for tile in rowOrColumn:
            if not tile.checked:
                areChecked = False
        return areChecked
        
    def __str__(self):
        return str(self.rows)

    def any(self):
        return len(self.rows) > 0
        
    def update(rowOrColumn, number):
        isBingo = False
        for tile in rowOrColumn:
            if tile.number == number:
                tile.checked = True
                if bingo.allChecked(rowOrColumn) == True:
                    isBingo = True
        return isBingo


    def draw(self, number):
        isBingo = False
        for row in self.rows:
            isBingo += bingo.update(row, number)
        for column in self.columns:
            isBingo += bingo.update(column, number)
        return isBingo

    def getUnmarkedSum(self):
        unmarked = 0
        for row in self.rows:
            for tile in row:
                if not tile.checked:
                    unmarked += int(tile.number)
        return unmarked

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


