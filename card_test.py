"""Tests of Card class"""
import pytest
from card import Card, InvalidValue, InvalidSuit


class TestCard:
    def test_creation(self):
        card = Card('A', 'clubs')
        assert card.number_or_face == 'A'
        assert card.suit == '♣'

    def test_creation_wrong_value(self):
        with pytest.raises(InvalidValue) as message:
            Card('1', 'clubs')
            assert message == 'Invalid card value'

    def test_creation_wrong_suit(self):
        with pytest.raises(InvalidSuit) as message:
            Card('Q', 'Heart')
            assert message == 'Invalid card suit'

    def test_card_representation(self):
        assert repr(Card('2', 'clubs')) == '2♣ '
        assert repr(Card('2', 'spades')) == '2♠ '
        assert repr(Card('2', 'hearts')) == '2♥ '
        assert repr(Card('2', 'diamonds')) == '2♦ '
