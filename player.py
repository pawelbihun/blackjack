"""Module with Players class"""
from card import Card


class Player:
    """Class represents playing person"""

    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 0
        self.my_cards: list[Card] = []
        self.loser = False

    def add_score(self) -> None:
        self.score = self.calculate_scores()

    def show_cards(self) -> None:
        print(f'{self.name}, this are your cards:')
        print(self.my_cards)

    def take_card(self, new_card: Card) -> None:
        self.my_cards.append(new_card)

    def put_cards_away(self) -> None:
        self.my_cards.clear()

    def calculate_scores(self) -> int:
        cards_amount = len(self.my_cards)
        score = 0

        if cards_amount == 0:
            return 0

        if cards_amount == 1:
            for card in self.my_cards:
                if card.number_or_face in ('J', 'Q', 'K', 'A'):
                    return 10
                return int(card.number_or_face)

        if cards_amount == 2:
            number_of_aces = 0
            for card in self.my_cards:
                if card.number_or_face in ('J', 'Q', 'K', 'A'):
                    if card.number_or_face == 'A':
                        number_of_aces += 1
                        if number_of_aces == 2:
                            return 21
                    score += 10
                else:
                    score += int(card.number_or_face)
            return score

        # 3 or more cards
        else:
            number_of_aces = 0
            for card in self.my_cards:
                if card.number_or_face in ('J', 'Q', 'K', 'A'):
                    if card.number_or_face == 'A':
                        if number_of_aces >= 1:
                            score += 1
                        else:
                            score += 10
                        number_of_aces += 1
                        continue
                    score += 10
                else:
                    score += int(card.number_or_face)
            return score
