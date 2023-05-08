"""Tests of Deck class"""
from card import Card
from deck import Deck


class TestDeck:
    def test_creation_length_of_deck(self):
        """Check that the length of the deck of cards is 52"""
        assert len(Deck()) == 52

    def test_cards_count_in_each_suit(self):
        """Check that the length of each suit of deck is 13"""
        my_deck = Deck()
        list_of_cards = [(card.number_or_face, card.suit) for card in my_deck.list_of_cards]
        for suit in Card.possible_suits.values():
            suit_of_cards = [card for card in list_of_cards if card[1] == suit]
            assert len(suit_of_cards) == 13

    def test_draw_card(self):
        """Check that drew card is not in deck"""
        my_deck = Deck()
        drew_card = my_deck.draw_card()
        assert drew_card not in my_deck.list_of_cards
