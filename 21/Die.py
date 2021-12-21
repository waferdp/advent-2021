class Die:
    last = 99
    rolls = 0

    def __init__(self) -> None:
        self.last = 99

    def roll(self) -> int:
        self.last =  (self.last + 1) % 100
        self.rolls += 1
        return self.last + 1

    def rollThrice(self) -> int:
        count = 0
        for i in range(3):
            count += self.roll() 
        return count