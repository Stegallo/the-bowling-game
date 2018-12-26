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
        """ checks if there is a spare in the frame having first roll i """
        if self.rolls[i] + self.rolls[i+1] == 10:
            return True
        return False

    def is_strike(self, i):
        """ checks if there is a strike in the frame having first roll i """
        if self.rolls[i] == 10:
            return True
        return False

    def get_score(self):
        """ calculates final score """
        score = 0
        roll = 0
        frames = 10
        for _ in range(frames):
            score += self.rolls[roll] + self.rolls[roll+1]
            if self.is_spare(roll):
                score += self.rolls[roll+2]
            if self.is_strike(roll):
                score += self.rolls[roll+2]
                roll += -1
            roll += 2

        return score
