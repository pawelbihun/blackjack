"""Class of card with exception"""


class InvalidSuit(Exception):
    """Exception when suit of card is invalid"""


class InvalidValue(Exception):
    """Exception when value of card is invalid"""


class Card:
    """Class represents a single playing card"""
    possible_values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    possible_suits = {
        'clubs': '\u2663',
        'spades': '\u2660',
        'hearts': '\u2665',
        'diamonds': '\u2666'
    }

    def __init__(self, value: str, suit: str) -> None:
        if value not in self.possible_values:
            raise InvalidValue('Invalid card value')
        self.number_or_face = value

        if suit not in self.possible_suits:
            raise InvalidSuit('Invalid card suit')
        self.suit = self.possible_suits[suit]

    def __repr__(self) -> str:
        return f'{self.number_or_face}{self.suit} '

    def __str__(self) -> str:
        return f'{self.number_or_face}{self.suit} '
