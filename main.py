import random
import unittest

class Board:
    def __init__(self):
        self.board = [[' ']*6 for _ in range(7)]

    def add_piece(self, column, piece):
        for row in range(6):
            if self.board[column][row] == ' ':
                self.board[column][row] = piece
                return True
        return False

    def is_winning_move(self, piece):
        # Check horizontal, vertical, and diagonal lines for a winning move
        for column in range(7):
            for row in range(6):
                try:
                    if (self.board[column][row] == piece and
                        self.board[column+1][row] == piece and
                        self.board[column+2][row] == piece and
                        self.board[column+3][row] == piece):
                        return True
                    if (self.board[column][row] == piece and
                        self.board[column][row+1] == piece and
                        self.board[column][row+2] == piece and
                        self.board[column][row+3] == piece):
                        return True
                    if (self.board[column][row] == piece and
                        self.board[column+1][row+1] == piece and
                        self.board[column+2][row+2] == piece and
                        self.board[column+3][row+3] == piece):
                        return True
                    if (column >= 3 and row <= 2 and
                        self.board[column][row] == piece and
                        self.board[column-1][row+1] == piece and
                        self.board[column-2][row+2] == piece and
                        self.board[column-3][row+3] == piece):
                        return True
                except IndexError:
                    pass
        return False

    def display(self):
        for row in reversed(range(6)):
            print('|' + '|'.join(self.board[column][row] for column in range(7)) + '|')
        print(' ' + ' '.join(str(i) for i in range(7)))  # print column numbers

class Player:
  
    def __init__(self, is_human, piece):
        self.is_human = is_human
        self.piece = piece


    def make_move(self, board):
            if self.is_human:
                column = int(input("Enter a column: "))
                # Find the lowest available row in the column
                row = next((r for r in range(6) if board.board[column][r] == ' '), None)
                if row is not None:
                    board.board[column][row] = self.piece
                    return True
            else:
                # Implement the computer player's strategy here
                # First, try to find a winning move
                for column in range(7):
                    for row in range(5, -1, -1):
                        if board.board[column][row] == ' ':
                            board.board[column][row] = self.piece

                            # Check for winning move horizontally, vertically, or diagonally
                            if (board.is_winning_move(self.piece) or
                                    any(board.is_winning_move(self.piece) for col in range(7))):
                                return True

                            # Reset the move
                            board.board[column][row] = ' '
                            break  # Move to the next column

                # If no winning move, then try to find a blocking move
                for column in range(7):
                    for row in range(5, -1, -1):
                        if board.board[column][row] == ' ':
                            board.board[column][row] = 'X' if self.piece == 'O' else 'O'

                            # Check for blocking move horizontally, vertically, or diagonally
                            if (board.is_winning_move('X' if self.piece == 'O' else 'O') or
                                    any(board.is_winning_move('X' if self.piece == 'O' else 'O') for col in range(7))):
                                board.board[column][row] = self.piece
                                return True

                            # Reset the move
                            board.board[column][row] = ' '
                            break  # Move to the next column

                # If no winning or blocking move is found, make a random move
                available_columns = [col for col in range(7) if board.board[col][0] == ' ']
                if available_columns:
                    column = random.choice(available_columns)
                    # Find the lowest available row in the chosen column
                    row = next((r for r in range(6) if board.board[column][r] == ' '), None)
                    if row is not None:
                        board.board[column][row] = self.piece
                        return True

                return False
            

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(True, 'X'), Player(False, 'O')]

    def play(self):
        self.board.display()
        while True:
            for player in self.players:
                if player.make_move(self.board):
                    self.board.display()
                    if self.board.is_winning_move(player.piece):
                        print(f"Player {player.piece} wins!")
                        return
    

class TestBoard(unittest.TestCase):
    def test_add_piece(self):
        board = Board()
        self.assertTrue(board.add_piece(0, 'X'))
        self.assertEqual(board.board[0][0], 'X')

    def test_is_winning_move(self):
        board = Board()
        for _ in range(4):
            board.add_piece(0, 'X')
        self.assertTrue(board.is_winning_move('X'))

if __name__ == "__main__":
    #unittest.main()
    game = Game()
    game.play()