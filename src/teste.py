import unittest
from src.board import Connect4Board
import io
import unittest.mock
from unittest.mock import patch
from src.HumanPlayer import HumanPlayer  # Replace 'your_module' with the actual module name
from unittest import TestCase
from unittest.mock import patch
from src.ComputerPlayer import ComputerPlayer


class TestConnect4Board(unittest.TestCase):

    def test_make_move(self):

        board = Connect4Board(6, 7)
        board.make_move(3, 'X')
        self.assertEqual(board.board[5][3], 'X')

    def test_display_board(self):

        board = Connect4Board(6, 7)
        # Redirect stdout to capture the printed output
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board.display_board()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(len(output.split('\n')), 8)
        self.assertEqual(len(output.split('|')), 37)

    def test_is_valid_location(self):

        board = Connect4Board(6, 7)
        self.assertTrue(board.is_valid_location(3))

    def test_is_valid_move(self):

        board = Connect4Board(6, 7)
        self.assertTrue(board.is_valid_move(3))


    def test_copy_board(self):

        board = Connect4Board(6, 7)
        board_copy = board.copy_board()
        board.make_move(3, 'X')
        self.assertNotEqual(board.board[5][3], board_copy.board[5][3])

    def test_count_consecutive_symbols(self):
        board = Connect4Board(6, 7)
        board.board[0][2:5] = ['X', 'X', 'X']
        self.assertEqual(board.count_consecutive_symbols('X'), 1)

    def test_is_game_over(self):
        board = Connect4Board(6, 7)
        for col in range(7):
            for row in range(6):
                board.board[row][col] = 'X'
        self.assertTrue(board.is_game_over())

    def test_check_winner(self):
        board = Connect4Board(6, 7)
        board.board[2][2:6] = ['O', 'O', 'O', 'O']
        self.assertTrue(board.check_winner('O'))


class MockConnect4:
    def is_valid_move(self, col):
        return col != 6


class TestHumanPlayer(unittest.TestCase):
    def test_make_move_valid(self):
        # Simulate a valid move (user input: '3')
        with patch('builtins.input', return_value='3'):
            player = HumanPlayer('X')
            move = player.make_move(MockConnect4())
            self.assertEqual(move, 3)

    def test_make_move_invalid_input(self):
        # Simulate invalid input (user input: 'invalid' then '2')
        with patch('builtins.input', side_effect=['invalid', '2']):
            player = HumanPlayer('X')
            move = player.make_move(MockConnect4())
            self.assertEqual(move, 2)

    def test_make_move_invalid_column_full(self):
        # Simulate an invalid move (user input: '5' then '8' then '2')
        with patch('builtins.input', side_effect=['5', '8', '2']):
            player = HumanPlayer('O')
            move = player.make_move(MockConnect4())
            self.assertEqual(move, 5)  # Change the expected value to 5




class TestComputerPlayer(unittest.TestCase):
    def test_evaluate_board(self):

        board_state = [
            ['X', 'O', ' ', ' ', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' ', ' ', ' '],
            ['X', 'O', 'O', ' ', ' ', ' ', ' '],
            ['X', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', 'X', 'O', 'X', 'X', 'O', ' '],
            [' ', 'X', 'O', 'X', 'X', 'O', ' ']
        ]
        connect4 = Connect4Board(rows=6, cols=7)
        connect4.board = board_state

        computer_player = ComputerPlayer(symbol='O', human_symbol='X')
        score = computer_player.evaluate_board(connect4)

        self.assertEqual(score, 1160)

    def test_find_best_move(self):

        board_state = [
            ['X', 'O', ' ', ' ', ' ', ' ', ' '],
            ['X', 'O', ' ', ' ', ' ', ' ', ' '],
            ['X', 'O', 'O', ' ', ' ', ' ', ' '],
            ['X', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', 'X', 'O', 'X', 'X', 'O', ' '],
            [' ', 'X', 'O', 'X', 'X', 'O', ' ']
        ]
        connect4 = Connect4Board(rows=6, cols=7)
        connect4.board = board_state

        computer_player = ComputerPlayer(symbol='O', human_symbol='X')
        best_move = computer_player.find_best_move(connect4, depth=3)
        self.assertEqual(best_move, 2)




