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

    def get_score(self):
        """ calculates final score """
        score = 0
        for i in self.rolls:
            score = score + i

        return score
