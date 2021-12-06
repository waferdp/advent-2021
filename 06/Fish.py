class Fish:

    timer = 0

    def __init__(self, timer) -> None:
        self.timer = timer

    def nextDay(self):
        if self.timer == 0:
            self.timer = 6
            return Fish(8)
        else: 
            self.timer -= 1
            return None

    def __str__(self) -> str:
        return str(self.timer)