from _typeshed import Self


class vec3:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z 
    
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def rotate(self, axis):
        if axis == 'x':
            return vec3(self.x, self.z * -1, self.y)
        elif axis == 'y':
            return vec3(self.z, self.y, self.x * -1)
        elif axis == 'z':
            return vec3(self.y * -1, self.x, self.z)
        else:
            print('wat')
