
from abc import ABC
from IBoard import IBoard
from colorama import Fore, Back, Style 

class TicTacToe_Board(IBoard):
    def __init__(self, size: int):
        super(TicTacToe_Board, self).__init__(size)

    def render(self):
        """
        Draws the board to the standard output
        """
        board = self.board
        print("   ", end = '')
        for x in range(len(board[0])):
            print("\033[04m{0}\033[04m".format(x), end = ' ')
        print(Style.RESET_ALL)
        for i, rows in enumerate(board):
            divider = '  |'
            print("{0} |".format(i) ,end = '')
            for j, val in enumerate(rows):
                print(val, end = '')
                if j != len(rows)-1:
                    print('|', end = '')
                    divider += '-+'
            print("| {0}".format(i) ,end = '')
            print()
            if i != len(board)-1:
                divider += '-|'
                print(divider)

    def player_won(self, player) -> bool:
        """
        Evaluates the board, to check if the given selection has won the match
        """
        board = self.board

        # check for rows
        for i, rows in enumerate(board):
            winner = True
            for j, value in enumerate(rows):
                if value != player:
                    winner = False
            if winner:
                return True

        # check for rows
        for j in range(len(board[0])):
            winner = True
            for i in range(len(board)):
                if board[i][j] != player:
                    winner = False
            if winner:
                return ("cols", True)

        # check diags
        winner = True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == j:
                    if board[i][j] != player:
                        winner = False
        if winner == True:
            return True

        # check diags
        winner = True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if j == len(board[0])-i-1:
                    if board[i][j] != player:
                        winner = False
        if winner == True:
            return True

        return False

    def game_tied(self) -> bool:
        if self.get_valid_moves(): # there are valid moves left
            return False
        else:
            return True

    def get_valid_moves(self) -> list:
        """
        Return a list with all the Valid Moves.
        A valid move is when there is a " " in the board
        """
        valid_moves = []
        board = self.board
        for i, rows in enumerate(board):
            for j, value in enumerate(rows):
                if value == ' ':
                    valid_moves.append((i,j))
        return valid_moves

    def is_move_valid(self, move: tuple) -> bool:
        if not isinstance(move, tuple):
            return False

        if not isinstance(move[0], int) and not isinstance(move[1], int):
            return False

        board = self.board
        if board[move[0]][move[1]] == ' ':
            return True
        else:
            return False

    def make_move(self, move: tuple, player) -> bool:
        if not self.is_move_valid(move):
            return False
        
        board = self.board
        board[move[0]][move[1]] = player
