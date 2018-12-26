"""
    The Bowling Game - Score calcolator
"""

class Game(object):
    """ Class that calculates a Bowling Score."""

    def __init__(self):
        """ init method """
        self.score = 0

    def roll(self, pins):
        """ records a roll """
        self.score += pins

    def get_score(self):
        """ calculates final score """
        return self.score
