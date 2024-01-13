from src.board import Connect4Board
from src.ComputerPlayer import ComputerPlayer
from src.HumanPlayer import HumanPlayer


class Connect4Game:
    def __init__(self):
        self.connect4 = Connect4Board()
        self.human_player = HumanPlayer('X')
        self.computer_player = ComputerPlayer('O')

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

            # Computer player's turn
            computer_col = self.computer_player.make_move(self.connect4)
            self.connect4.make_move(computer_col, 'O')
            if self.connect4.check_winner('O'):
                self.connect4.display_board()
                print("Sorry, you lose. Better luck next time!")
                break

            # Check for a tie
            if all(cell != ' ' for row in self.connect4.board for cell in row):
                self.connect4.display_board()
                print("It's a tie!")
                break

        print("Game Over")
