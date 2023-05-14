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
        print('You crossed the limit of 21 scores.\nGAME OVER!!!')
    except GameOverCroupier:
        print('Croupier crossed the limit of 21 scores.\nPlayer won!')

