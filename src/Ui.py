from src.board import Connect4Board
from src.ComputerPlayer import ComputerPlayer
from src.HumanPlayer import HumanPlayer


class Connect4Game:
    def __init__(self):
        self.connect4 = Connect4Board(6,7)
        self.human_player = HumanPlayer('X')
        self.computer_player = ComputerPlayer('O', 'X')

    def play_game(self):
        while True:
            self.connect4.display_board()

            # Human player's turn
            human_col = self.human_player.make_move(self.connect4)
            self.connect4.make_move(human_col, 'X')
            if self.connect4.check_winner('X'):
                self.connect4.display_board()
                print("Congratulations! You win!")
                break
            elif self.connect4.is_draw():
                self.connect4.display_board()
                print("It's a draw!")
                break

            # Computer player's turn
            computer_col = self.computer_player.make_move(self.connect4)
            self.connect4.make_move(computer_col, 'O')
            if self.connect4.check_winner('O'):
                self.connect4.display_board()
                print("Computer wins!")
                break
            elif self.connect4.is_draw():
                self.connect4.display_board()
                print("It's a draw!")
                break
