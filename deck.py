import random

from card import Card


class Deck:
    """Class represents a deck of playing cards"""

    def __init__(self):
        self.list_of_cards = self.create_deck()

    def __str__(self):
        return f'{self.list_of_cards}'

    def __len__(self):
        return len(self.list_of_cards)

    @staticmethod
    def create_deck() -> list[Card]:
        """While class is initialization method creates a deck of playing cards"""
        cards = []
        for value in Card.possible_values:
            for color in Card.possible_suits:
                cards.append(Card(value, color))

        return cards

    def draw_card(self) -> Card:
        """Return a random draw card from the deck"""
        return self.list_of_cards.pop(self.list_of_cards.index(random.choice(self.list_of_cards)))
