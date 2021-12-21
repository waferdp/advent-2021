class Player:
    pos = 0
    score = 0
    name = ""

    def __init__(self, pos: int, name: str) -> None:
        self.pos = pos-1
        self.score = 0
        self.name = name
    
    def __str__(self) -> str:
        return "Player " + self.name + " @" + str(self.pos) + ": " + str(self.score)

    def __repr__(self):
        return str(self)

    def move(self, steps):
        self.pos = (self.pos + steps) % 10
        self.score += self.pos + 1 