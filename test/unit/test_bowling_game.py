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

def test_one_spare(request):
    """
        test one spare
    """
    log("""
        ... {} ...""".format(request.node.name))
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.get_score() == 16

def test_one_strike(request):
    """
        test one strike
    """
    log("""
        ... {} ...""".format(request.node.name))
    game = Game()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    assert game.get_score() == 24
