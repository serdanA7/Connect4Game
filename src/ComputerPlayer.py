import random

class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, connect4):
        # Function to check if there are three consecutive symbols in a list
        def has_three_consecutive(lst, symbol):
            count = 0
            for cell in lst:
                if cell == symbol:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 0
            return False

        winning_move = self.check_winning_move(connect4, has_three_consecutive)
        if winning_move is not None:
            return winning_move

        blocking_move = self.check_blocking_move(connect4, has_three_consecutive)
        if blocking_move is not None:
            return blocking_move

        competitive_move = self.check_competitive_move(connect4, has_three_consecutive)
        if competitive_move is not None:
            return competitive_move

        # If no winning, blocking or competitive move, make a random move
        valid_moves = [col for col in range(connect4.cols) if connect4.is_valid_move(col)]
        return random.choice(valid_moves)

    def check_winning_move(self, connect4, has_three_consecutive):
        for col in range(connect4.cols):
            if connect4.is_valid_move(col):
                temp_board = [row[:] for row in connect4.board]
                # Find the first row in the column that contains a space
                for row in reversed(range(connect4.rows)):
                    if temp_board[row][col] == ' ':
                        temp_board[row][col] = self.symbol
                        break
                if connect4.check_winner(self.symbol):
                    return col
        return None

    def check_blocking_move(self, connect4, has_three_consecutive):
        # Check horizontally
        for row in range(connect4.rows):
            for col in range(connect4.cols - 2):
                if has_three_consecutive(connect4.board[row][col:col+3], 'X'):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        # Check vertically
        for col in range(connect4.cols):
            for row in range(connect4.rows - 2):
                if has_three_consecutive([connect4.board[row+i][col] for i in range(3)], 'X'):
                    if connect4.is_valid_move(col):
                        return col

        # Check diagonally (top-left to bottom-right)
        for row in range(connect4.rows - 2):
            for col in range(connect4.cols - 2):
                if has_three_consecutive([connect4.board[row+i][col+i] for i in range(3)], 'X'):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        # Check diagonally (bottom-left to top-right)
        for row in range(2, connect4.rows):
            for col in range(connect4.cols - 2):
                if has_three_consecutive([connect4.board[row-i][col+i] for i in range(3)], 'X'):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        return None

    def check_competitive_move(self, connect4, has_three_consecutive):
        # Check for competitive horizontal move
        for row in range(connect4.rows):
            for col in range(connect4.cols - 2):
                if has_three_consecutive(connect4.board[row][col:col+3], self.symbol):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        # Check for competitive vertical move
        for col in range(connect4.cols):
            for row in range(connect4.rows - 2):
                if has_three_consecutive([connect4.board[row+i][col] for i in range(3)], self.symbol):
                    if connect4.is_valid_move(col):
                        return col

        # Check for competitive diagonal move (top-left to bottom-right)
        for row in range(connect4.rows - 2):
            for col in range(connect4.cols - 2):
                if has_three_consecutive([connect4.board[row+i][col+i] for i in range(3)], self.symbol):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        # Check for competitive diagonal move (bottom-left to top-right)
        for row in range(2, connect4.rows):
            for col in range(connect4.cols - 2):
                if has_three_consecutive([connect4.board[row-i][col+i] for i in range(3)], self.symbol):
                    if connect4.is_valid_move(col + 2):
                        return col + 2

        return None