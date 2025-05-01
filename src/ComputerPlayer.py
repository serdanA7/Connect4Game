import copy
import math


class ComputerPlayer:
    def __init__(self, symbol, human_symbol):
        self.symbol = symbol
        self.human_symbol = human_symbol

    def minimax(self, connect4, depth, maximizing_player):
        """
                Applies the Minimax algorithm to evaluate and choose the best move.

                Parameters:
                - connect4 (Connect4Board): The Connect4 board state.
                - depth (int): The depth of the Minimax algorithm, representing the look-ahead depth.
                - maximizing_player (bool): True if the current player is the maximizing player, False otherwise.

                Returns:
                - int: The evaluation score for the current move.
                """
        if depth == 0 or connect4.is_game_over():
            return self.evaluate_board(connect4)

        valid_moves = [col for col in range(connect4.cols) if connect4.is_valid_move(col)]

        if maximizing_player:
            max_eval = float('-inf')
            for col in valid_moves:
                temp_board = connect4.copy_board()
                temp_board.make_move(col, self.symbol)
                eval = self.minimax(temp_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for col in valid_moves:
                temp_board = connect4.copy_board()
                temp_board.make_move(col, 'X' if self.symbol == 'O' else 'O')
                eval = self.minimax(temp_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def evaluate_board(self, connect4):
        """
               Evaluates the Connect4 board state and assigns a score to it.

               Parameters:
               - connect4 (Connect4Board): The Connect4 board state.

               Returns:
               - int: The score representing the evaluation of the board state.
               """
        def count_consecutive_symbols_in_line(line, symbol):
            count = 0
            for cell in line:
                if cell == symbol:
                    count += 1
                else:
                    break
            return count

        def score_line(line, symbol):
            count = count_consecutive_symbols_in_line(line, symbol)
            if count >= 4:
                return 1000
            elif count == 3:
                return 50
            elif count == 2:
                return 10
            else:
                return 0

        score = 0

        for row in range(connect4.rows):
            for col in range(connect4.cols):
                # Evaluate horizontally
                score += score_line(connect4.board[row][col:col + 4], self.symbol)

                # Evaluate vertically
                score += score_line([connect4.board[row + i][col] for i in range(4) if row + i < len(connect4.board)], self.symbol)

                # Evaluate diagonally (top-left to bottom-right)
                score += score_line([connect4.board[row + i][col + i] for i in range(4) if row + i < len(connect4.board) and col + i < len(connect4.board[0])], self.symbol)

                # Evaluate diagonally (bottom-left to top-right)
                score += score_line([connect4.board[row - i][col + i] for i in range(4) if 0 <= row - i < len(connect4.board) and 0 <= col + i < len(connect4.board[0])], self.symbol)


        central_columns = [connect4.cols // 2 - 1, connect4.cols // 2, connect4.cols // 2 + 1]
        central_moves = sum([1 for move in central_columns if connect4.last_move == move])
        score += central_moves * 20

        return score

    def find_best_move(self, connect4, depth):
        """
                Finds the best move for the computer player using the Minimax algorithm.

                Parameters:
                - connect4 (Connect4Board): The Connect4 board state.
                - depth (int): The depth of the Minimax algorithm, representing the look-ahead depth.

                Returns:
                - int: The column index representing the best move for the computer player.
                """
        best_score = -math.inf
        best_move = None

        for col in range(connect4.cols):
            if connect4.is_valid_location(col):
                temp_board = copy.deepcopy(connect4)
                temp_board.make_move(col, self.human_symbol)
                if temp_board.check_winner(self.human_symbol):
                    return col


        for col in range(connect4.cols):
            temp_board = copy.deepcopy(connect4)
            if temp_board.is_valid_location(col):
                temp_board.make_move(col, self.symbol)
                score = self.minimax(temp_board, depth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = col

        return best_move


    def make_move(self, connect4):
        """
                Makes a move for the computer player using the Minimax algorithm.

                Parameters:
                - connect4 (Connect4Board): The Connect4 board state.

                Returns:
                - int: The column index representing the chosen move for the computer player.
                """
        return self.find_best_move(connect4, depth=3)


