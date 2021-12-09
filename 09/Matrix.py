class Matrix:
    mat = []

    def __init__(self, lines :list = []):
        self.mat = []
        self.height = 0
        self.width = None
        self.parseLines(lines)

    def parseLines(self, lines):
        for line in lines:
            numbers = []
            for raw in line:
                numbers.append(int(raw))
            self.addRow(numbers)

    def addRow(self, row): 
        self.mat.append(row)
        self.height = len(self.mat)
        if self.width is not None:
            assert(self.width == len(row))
        else:
            self.width = len(row)

    def isLeast(self, x ,y):
        val = self.get(x,y)
        above = self.above(x,y)
        right = self.right(x,y)
        below = self.below(x,y)
        left = self.left(x,y)

        if(val < above and val < right and val < below and val < left):
            return True
        else:
            return False

    def get(self, x, y):
        return self.mat[y][x]

    def above(self, x,y):
        if y == 0:
            return 10
        return self.mat[y-1][x]
    
    def below(self, x, y):
        if y + 1 >= self.height:
            return 10
        return self.mat[y+1][x]

    def left(self, x, y):
        if x == 0:
            return 10
        return self.mat[y][x-1]
        
    def right(self, x, y):
        if x +1 >= self.width:
            return 10
        return self.mat[y][x+1]
