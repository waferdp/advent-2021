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

    rows = []
    checkedRows = []
    columns = []   
    checkedColumns = []
    haswon = False

    def __init__(self):
        self.rows = []
        self.columns = []

    def build(self):
        width = len(self.rows[0])
        for i in range(0, width):
            column = []
            for row in self.rows:
                column.append(row[i])
            self.columns.append(column)

    def allChecked(self, rowOrColumn):
        areChecked = True
        for tile in rowOrColumn:
            if not tile.checked:
                areChecked = False
        return areChecked
        
    def __str__(self):
        return str(self.rows)

    def any(self):
        return len(self.rows) > 0
        
    def draw(self, number):
        isBingo = False
        for row in self.rows:
            for tile in row:
                if tile.number == number:
                    tile.checked = True
                    if self.allChecked(row) == True:
                        isBingo = True
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
    board = bingo()
    
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
                # print(board)
                boards.append(board)
                board = bingo()
                
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
            print("BINGO! at " + number)
            if len(boards) == 1:
                print("Last board")
                print(boards[0].getUnmarkedSum() * int(number))

            #print(board.getUnmarkedSum() * int(number))
            temp.remove(board)
    return temp


def drawNumbers(boards, numbers):
    for number in numbers:
        boards = drawNumber(boards, number)


lines = file.read("test_input.txt")
boards = getBoards(lines)
numbers = getNumbers(lines)
drawNumbers(boards, numbers)


