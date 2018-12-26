"""
    The Bowling Game - Score calcolator
"""

class Game(object):
    """ Class that calculates a Bowling Score."""

    def __init__(self):
        """ init method """
        # self.score = 0
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """ records a roll """
        # self.score += pins
        self.rolls.append(pins)

    def is_spare(self, i):
        """ """
        if self.rolls[i] + self.rolls[i+1] == 10:
            return True
        return False

    def get_score(self):
        """ calculates final score """
        score = 0
        frames = 10
        for i in range(frames):
            j = 2*i
            score += self.rolls[j] + self.rolls[j+1]
            if self.is_spare(j):
                score += self.rolls[j+2]


        return score
