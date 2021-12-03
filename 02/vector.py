class vector:
    horizontal = 0
    depth = 0
    aim = 0

    def add(a, b):
        sum = vector()
        sum.horizontal = a.horizontal + b.horizontal
        sum.depth = a.depth + b.depth
        sum.aim = a.aim + b.aim
        return sum
