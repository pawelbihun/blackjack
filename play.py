"""Playing modul - starting file"""
import os

from game import Game, GameOverPlayer, GameOverCroupier

if __name__ == '__main__':
    # clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    # play the game
    game = Game()
    try:
        ps = game.players_turn()
        cs = game.croupiers_turn()
        game.who_is_winner(ps, cs)
    except GameOverPlayer:
        print(f'You got {game.players[0].score} score and crossed the limit of 21 scores.\nGAME OVER!!!')
    except GameOverCroupier:
        print(f'Croupier got {game.players[1].score} score and crossed the limit of 21 scores.\nPlayer won!')

