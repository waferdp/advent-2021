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