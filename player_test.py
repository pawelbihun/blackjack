"""Tests of Player class"""
import pytest

from card import Card
from deck import Deck
from player import Player


class TestPlayer:
    @pytest.fixture
    def player(self) -> Player:
        return Player('Player')

    def test_creation(self, player):
        """Constructor test"""
        assert player.name == 'Player'
        assert player.score == 0
        assert player.my_cards == []

    def test_take_card(self, player):
        """Check that after drawing player has one card"""
        playing_deck = Deck()
        player.take_card((playing_deck.draw_card()))
        assert len(player.my_cards) == 1

    def test_calculate_scores(self, player):
        """Check that scores are properly calculated"""
        ace_card = Card('A', 'clubs')  # represent ace cards
        king_card = Card('K', 'clubs')  # represent face cards
        two_card = Card('2', 'clubs')  # represent number cards

        # test case no cards
        score = player.calculate_scores()
        assert score == 0

        # test case 1 card - 1 ace = 10 scores
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 10
        player.put_cards_away()

        # test case 1 card - 1 king = 10 scores
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 10
        player.put_cards_away()

        # test case 1 card - 2 number = 2 scores
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 2
        player.put_cards_away()

        # test case 2 cards - 2 aces = 21 scores
        player.take_card(ace_card)
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 21
        player.put_cards_away()

        # test case 2 cards - 1 ace + 1 king = 20 scores
        player.take_card(ace_card)
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 20
        player.put_cards_away()

        # test case 2 cards - 1 ace + 2 number = 12 scores
        player.take_card(ace_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 12
        player.put_cards_away()

        # test case 2 cards - 2 kings = 20 scores
        player.take_card(king_card)
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 20
        player.put_cards_away()

        # test case 2 cards - 1 king + 2 number = 12 scores
        player.take_card(king_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 12
        player.put_cards_away()

        # test case 2 cards - 2 times 2 number = 4 scores
        player.take_card(two_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 4
        player.put_cards_away()

        # if there is more than 2 cards then only first ace has 10 scores rest has 1 score!!!

        # test case 3 cards - AAA = 30 scores  - NEVER EXIST

        # test case 3 cards - AKA = 21 scores
        player.take_card(ace_card)
        player.take_card(king_card)
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 21
        player.put_cards_away()

        # test case 3 cards - A2A = 13 scores
        player.take_card(ace_card)
        player.take_card(two_card)
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 13
        player.put_cards_away()

        # test case 3 cards - AKK = 30 scores
        player.take_card(ace_card)
        player.take_card(king_card)
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 30
        player.put_cards_away()

        # test case 3 cards - A22 = 14 scores
        player.take_card(ace_card)
        player.take_card(two_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 14
        player.put_cards_away()

        # test case 3 cards - AK2 = 22 scores
        player.take_card(ace_card)
        player.take_card(king_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 22
        player.put_cards_away()

        # test case 3 cards - KKK = 30 scores
        player.take_card(king_card)
        player.take_card(king_card)
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 30
        player.put_cards_away()

        # test case 3 cards - KKA = 30 scores
        player.take_card(king_card)
        player.take_card(king_card)
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 30
        player.put_cards_away()

        # test case 3 cards - KK2 = 22 scores
        player.take_card(king_card)
        player.take_card(king_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 22
        player.put_cards_away()

        # test case 3 cards - 222 = 6 scores
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 6
        player.put_cards_away()

        # test case 3 cards - 22A = 14 scores
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(ace_card)
        score = player.calculate_scores()
        assert score == 14
        player.put_cards_away()

        # test case 3 cards - 22K = 14 scores
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(king_card)
        score = player.calculate_scores()
        assert score == 14
        player.put_cards_away()

        # test case 4 cards - K222 = 16 scores
        player.take_card(king_card)
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 16
        player.put_cards_away()

        # test case 4 cards - 2222 = 8 scores
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(two_card)
        player.take_card(two_card)
        score = player.calculate_scores()
        assert score == 8
        player.put_cards_away()
