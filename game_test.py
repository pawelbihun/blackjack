"""Test of Game class"""
from game import Game


def test_creation():
    """Constructor test"""
    game = Game()
    assert len(game.players) > 0
    assert game.players[0].name == 'Player'
    assert len(game.playing_deck) == 52

