"""
    Test cases for The Bowling Game - Score calcolator
"""

from bowling_game import Game
from .test_environment_setup import log

def test_gutter_game(request):
    """
        test all 0s
    """
    log("""
        ... {} ...""".format(request.node.name))
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.get_score() == 0

def test_all_ones(request):
    """
        test all 1s
    """
    log("""
        ... {} ...""".format(request.node.name))
    game = Game()
    for _ in range(20):
        game.roll(1)
    assert game.get_score() == 20
