"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez

Development Exercises - L8
Unit Testing for MinMax Algorithm
"""

import unittest

from tictactoe_ai import TicTacToe_AI
from tictactoe_board import TicTacToe_Board

class test_tictactoe_ai(unittest.TestCase):

    def setUp(self):
        self.t = TicTacToe_AI("X")
        self.b = TicTacToe_Board(3)
        self.MIN = -1000
        self.MAX = +1000

    def tearDown(self):
        self. b = None

    # Testing Evaluate Function
    def test_evaluate_first_row(self):
        self.b.board = [
            ['X','X','X'],
            [' ','O',' '],
            ['O',' ','X']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            ['O','O','O'],
            [' ','O',' '],
            ['O',' ','X']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_middle_row(self):
        self.b.board = [
            [' ',' ',' '],
            ['X','X','X'],
            [' ',' ',' ']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            [' ',' ',' '],
            ['O','O','O'],
            [' ',' ',' ']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_last_row(self):
        self.b.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            ['X','X','X']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            ['O','O','O']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_first_col(self):
        self.b.board = [
            ['X',' ',' '],
            ['X',' ',' '],
            ['X',' ',' ']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            ['O',' ',' '],
            ['O',' ',' '],
            ['O',' ',' ']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_middle_col(self):
        self.b.board = [
            [' ','X',' '],
            [' ','X',' '],
            [' ','X',' ']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            [' ','O',' '],
            [' ','O',' '],
            [' ','O',' ']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_last_col(self):
        self.b.board = [
            [' ',' ','X'],
            [' ',' ','X'],
            [' ',' ','X']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            [' ',' ','O'],
            [' ',' ','O'],
            [' ',' ','O']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_first_diag(self):
        self.b.board = [
            ['X',' ',' '],
            [' ','X',' '],
            [' ',' ','X']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            ['O',' ',' '],
            [' ','O',' '],
            [' ',' ','O']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_second_diag(self):
        self.b.board = [
            [' ',' ','X'],
            [' ','X',' '],
            ['X',' ',' ']
        ]
        self.assertEqual(10, self.t.evaluate(self.b.board))
        self.b.board = [
            [' ',' ','O'],
            [' ','O',' '],
            ['O',' ',' ']
        ]
        self.assertEqual(-10, self.t.evaluate(self.b.board))

    def test_evaluate_no_winner(self):
        self.b.board = [
            ['O','O','X'],
            ['X','X','O'],
            ['O','X','X']
        ]
        self.assertEqual(0, self.t.evaluate(self.b.board))

    # Testing MoveLeft Function
    def test_MovesLeft_true(self):
        self.b.board = [
            [' ','O','X'],
            ['X','X','O'],
            ['O','X','X']
        ]
        self.assertEqual(True, self.t.moves_left(self.b.board))

    def test_MovesLeft_false(self):
        self.b.board = [
            ['X','O','X'],
            ['X','X','O'],
            ['O','X','X']
        ]
        self.assertEqual(False, self.t.moves_left(self.b.board))

    # Testing MinMax Function
    def test_minmax_MaxWin(self):
        self.b.board = [
            ['X','O','X'],
            ['O','O','X'],
            [' ',' ',' ']
        ]
        self.assertEqual(10, self.t.minmax(self.b.board, 0, True, self.MIN, self.MAX))
    
    def test_minmax_MinWin(self):
        self.b.board = [
            ['X','O','X'],
            ['O','O','X'],
            [' ',' ',' ']
        ]
        self.assertEqual(-10, self.t.minmax(self.b.board, 0, False, self.MIN, self.MAX))

    def test_minmax_BestMove_O(self):
        self.t = TicTacToe_AI('O')
        self.b.board = [
            ['X','O','X'],
            ['O','O','X'],
            [' ',' ',' ']
        ]
        self.assertEqual((2,1), self.t.get_move(self.b))

    def test_minmax_BestMove_X(self):
        self.t = TicTacToe_AI('X')
        self.b.board = [
            ['X','O','X'],
            ['O','O','X'],
            [' ',' ',' ']
        ]
        self.assertEqual((2,2), self.t.get_move(self.b))

if __name__ == '__main__':
    unittest.main()