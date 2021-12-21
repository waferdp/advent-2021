import readFile as file
from Player import Player
from Die import Die

class Dirac:
    players = []
    die = None

    def __init__(self, input) -> None:
        self.players = self.parsePlayers(input)
        self.die = Die()

    def parsePlayers(self, input):
        players = []
        index = 1
        for line in input:
            startingPos = int(line[-1])
            players.append(Player(startingPos, str(index)))
            index += 1
        return players
    
    def findWinner(self):
        for player in self.players:
            if player.score >= 1000:
                print('Winner winner chicken dinner: player ' + player.name)
        minimumScore = min(map(lambda x: x.score, self.players))
        return minimumScore * self.die.rolls

    def practice(self):
        while True:
            for player in self.players:
                roll = self.die.rollThrice()
                player.move(roll)
                if player.score >= 1000:
                    return self.findWinner()
           

    def play(self):
        pass
        

class Main:
    def run1(input):
        dirac = Dirac(input)
        return dirac.practice()

if __name__ == '__main__':
      input = file.read('puzzle_input.txt')
      fnord = Main.run1(input)
      print(fnord)