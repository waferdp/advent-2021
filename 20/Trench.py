from Matrix import Matrix
import readFile as file

class Trench:
    enhance = {}
    matrix = None

    def __init__(self, input) -> None:
        self.enhance = self.parseEnhance(input)
        self.matrix = self.parseImage(input)
        self.matrix.setDefault(int(self.enhance[0]))

    def enhanceImage(self) -> Matrix:
        self.matrix.padMatrix(self.matrix.default)
        new = Matrix.generate(self.matrix.width, self.matrix.height, self.matrix.default)
        for y in range(0, self.matrix.height):
            for x in range(0, self.matrix.width):
                value = self.matrix.getSquare(x, y)
                enhanced = int(self.enhance[value])
                new.set(x,y, enhanced)
        new.default = 1 if self.matrix.default == 0 else 0

    def parseEnhance(self, lines):
        enhance = []
        data = lines[0]
        for char in  data:
            if char == '.':
                enhance.append('0')
            else:
                enhance.append('1')
        return enhance

    def parseImage(self, lines):
        imageData = lines[2:]
        values = []
        for line in imageData:
            values.append(line.replace('.', '0').replace('#', '1'))
        return Matrix(values)

if __name__ == '__main__':
    input = file.read('puzzle_input.txt')
    trench = Trench(input)
    trench.enhanceImage()
    trench.enhanceImage()
    dots = trench.matrix.countDots()
    print(dots)
