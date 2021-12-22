import readFile as file
from Player import Player
from Die import Die
from functools import lru_cache

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
        a = (self.players[0].pos, self.players[0].score)
        b = (self.players[1].pos, self.players[1].score)
        a,b = Dirac.round(a,b)
        return max(a, b)

    diracSums = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

    @lru_cache(maxsize=None) 
    def round(a, b):
        if a[1] >= 21:
            return 1, 0
        elif b[1] >= 21:
            return 0, 1
        tot_a_wins = 0
        tot_b_wins = 0

        for x in range (1,4):
            for y in range (1, 4):
                for z in range(1, 4):
                    pos, score = a
                    pos = (pos + x+y+z) % 10
                    score += pos+1
                    b_wins, a_wins = Dirac.round(b, (pos, score))
                    tot_b_wins += b_wins
                    tot_a_wins += a_wins
        return tot_a_wins, tot_b_wins
class Main:
    def run1(input):
        dirac = Dirac(input)
        return dirac.practice()

    def run2(input):
        dirac = Dirac(input)
        max = dirac.play()
        return max

if __name__ == '__main__':
      input = file.read('puzzle_input.txt')
      fnord = Main.run2(input)
      print(fnord)