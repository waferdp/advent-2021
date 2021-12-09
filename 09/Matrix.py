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
        if y < 0 or x < 0:
            return 9
        if y >= self.height or x >= self.width:
            return 9
        return self.mat[y][x]

    def above(self, x,y):
        return self.get(x, y-1)
    
    def below(self, x, y):
        return self.get(x, y+1)

    def left(self, x, y):
        return self.get(x-1, y)
        
    def right(self, x, y):
        return self.get(x+1, y)
