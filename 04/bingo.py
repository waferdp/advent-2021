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

    def allChecked(rowOrColumn) -> bool:
        areChecked = True
        for tile in rowOrColumn:
            if not tile.checked:
                areChecked = False
        return areChecked
        
    def __str__(self) -> str:
        return str(self.rows)

    def any(self) -> bool:
        return len(self.rows) > 0
        
    def update(rowOrColumn, number) -> bool:
        isBingo = False
        for tile in rowOrColumn:
            if tile.number == number:
                tile.checked = True
                if bingo.allChecked(rowOrColumn) == True:
                    isBingo = True
        return isBingo


    def draw(self, number) -> bool:
        isBingo = False
        for row in self.rows:
            isBingo += bingo.update(row, number)
        for column in self.columns:
            isBingo += bingo.update(column, number)
        return isBingo

    def getUnmarkedSum(self) -> int:
        unmarked = 0
        for row in self.rows:
            for tile in row:
                if not tile.checked:
                    unmarked += int(tile.number)
        return unmarked