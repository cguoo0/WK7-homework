from game import TicTacToe

if __name__ == '__main__':
    single_player = input("Single player mode? (yes/no): ")
    game = TicTacToe(single_player)
    game.play_game()
