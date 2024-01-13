class Connect4Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def make_move(self, col, symbol):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = symbol
                break

    def check_winner(self, symbol):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == symbol for i in range(4)):
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == symbol for i in range(4)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == symbol for i in range(4)):
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == symbol for i in range(4)):
                    return True

        return False