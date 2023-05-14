from deck import Deck
from player import Player


class GameOverPlayer(Exception):
    """ Game over player.
    """


class GameOverCroupier(Exception):
    """ Game over croupier.
    """


class Game:
    """ Class represents the game
    """

    PLAYER: int = 0
    CROUPIER: int = 1

    def __init__(self):
        self.players: list[Player] = [Player('Player'), Player('Croupier')]
        self.playing_deck: Deck = Deck()

    def players_turn(self) -> int:
        """Return player score after drawing cards"""
        print('Player turn')
        player = self.players[self.PLAYER]
        self.first_deal(self.PLAYER)
        player.add_score()

        if not self.is_instant_winner(self.PLAYER):
            player.show_cards()
            answer = input('[D]raw another card or press any key to pass : ')
            while answer in ['d', 'D']:
                if answer in ['d', 'D']:
                    player.take_card(self.playing_deck.draw_card())
                    player.show_cards()
                    player.add_score()
                    if self.check_limit(self.PLAYER):
                        raise GameOverPlayer
                answer = input('[D]raw another card or press any key to pass : ')

            return player.score

        else:
            print(f'{player.name} you are the winner!')
            return 21

    def croupiers_turn(self) -> int:
        """Return croupier score after drawing cards"""
        print('\nCroupier turn')
        croupier = self.players[self.CROUPIER]
        self.first_deal(self.CROUPIER)
        croupier.add_score()
        croupier.show_cards()

        while croupier.score <= self.players[self.PLAYER].score and croupier.score < 20:
            croupier.take_card(self.playing_deck.draw_card())
            croupier.add_score()
            croupier.show_cards()
            if self.check_limit(self.CROUPIER):
                raise GameOverCroupier

        return croupier.score

    def first_deal(self, player_index: int) -> None:
        for _ in range(2):
            self.players[player_index].take_card(self.playing_deck.draw_card())

    def is_instant_winner(self, player_index) -> bool:
        if self.players[player_index].score == 21:
            return True
        return False

    def check_limit(self, player_index) -> bool:
        if self.players[player_index].score > 21:
            return True
        return False

    @staticmethod
    def who_is_winner(player_score, croupier_score) -> None:
        if player_score == 21:
            print('\nPlayer is the winner! You scored 21 points!')
        elif player_score == croupier_score:
            print('\nDraw')
        elif player_score > croupier_score:
            print('\nPlayer is the winner!')
        else:
            print('\nCroupier is the winner!')
