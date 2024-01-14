class Connect4Board:
    def __init__(self, rows, cols):
        """
        Initializes a Connect4 board with the specified number of rows and columns.

        Parameters:
        - rows (int): Number of rows in the board.
        - cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.last_move = None  # Keeps track of the last move made

    def make_move(self, col, symbol):
        """
        Places a symbol in the specified column.

        Parameters:
        - col (int): Column in which the move is made.
        - symbol (str): Symbol ('X' or 'O') to be placed in the column.
        """
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = symbol
                self.last_move = col  # Update last_move every time a move is made
                return

    def display_board(self):
        """
        Prints the current state of the Connect4 board to the console,
        including the row and column indices.
        """
        for row in self.board:
            print('|'.join(row))
        print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def is_valid_location(self, col):
        """
        Checks if the top row of the specified column is empty,
        indicating a valid move can be made.

        Parameters:
        - col (int): Column to check for validity.

        Returns:
        - bool: True if the column is a valid location for a move, False otherwise.
        """
        return self.board[0][col] == ' '

    def is_valid_move(self, col):
        """
        Checks if the specified column is within the valid range and
        the top row is empty.

        Parameters:
        - col (int): Column to check for validity.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def is_draw(self):
        """
        Checks if the game is a draw (no empty spaces left on the board).

        Returns:
        - bool: True if the game is a draw, False otherwise.
        """
        return all(self.board[0][col] != ' ' for col in range(self.cols))

    # ... (continuing with the remaining functions)
    def copy_board(self):
        """
        Creates a copy of the current board.

        Returns:
        - Connect4Board: Copy of the current board.
        """
        board_copy = Connect4Board(self.rows, self.cols)
        board_copy.board = [row[:] for row in self.board]
        return board_copy

    def count_consecutive_symbols(self, symbol):
        count = 0
        # Check rows
        for row in self.board:
            count += self.count_consecutive_in_list(row, symbol)
        # Check columns
        for col in range(self.cols):
            column = [self.board[row][col] for row in range(self.rows)]
            count += self.count_consecutive_in_list(column, symbol)
        # Check diagonals
        for diff in range(-self.rows + 1, self.cols):
            diag1 = [self.board[row][row + diff] for row in range(max(diff, 0), min(self.cols + diff, self.rows)) if
                     row < len(self.board) and row + diff < len(self.board[0])]
            diag2 = [self.board[row][self.cols - 1 - row + diff] for row in
                     range(max(diff, 0), min(self.cols + diff, self.rows))]
            count += self.count_consecutive_in_list(diag1, symbol)
            count += self.count_consecutive_in_list(diag2, symbol)
        return count

    @staticmethod
    def count_consecutive_in_list(lst, symbol):
        str_lst = ''.join(lst)
        return str_lst.count(symbol * 3)

    def is_game_over(self):
        # Check if there's a winner
        for symbol in ['X', 'O']:
            if self.check_winner(symbol):
                return True

        # Check if the board is full
        for row in self.board:
            if ' ' in row:
                return False

        return True

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
