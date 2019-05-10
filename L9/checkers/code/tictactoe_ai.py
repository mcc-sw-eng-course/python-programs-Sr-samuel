from IBoard import IBoard
from IPlayer import AIPlayer

class TicTacToe_AI(AIPlayer):
    def __init__(self, selection: str):
        super(TicTacToe_AI, self).__init__(selection)
        self.opponent = ''
        if self.selection == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'

    def evaluate(self, board: list) -> int:
        # Check if there is a win in any row of the board
        for i, rows in enumerate(board):
            opponent = True
            myself = True
            for j, value in enumerate(rows):
                if value != self.opponent:
                    opponent = False
                if value != self.selection:
                    myself = False
            if opponent:
                return -10
            if myself:
                return 10

        # Check if there is a win in any column in the board
        for j in range(len(board[0])):
            opponent = True
            myself = True
            for i in range(len(board)):
                if board[i][j] != self.opponent:
                    opponent = False
                if board[i][j] != self.selection:
                    myself = False
            if opponent:
                return -10
            if myself:
                return 10

        # check win in any diagonal in the board
        opponent = True
        myself = True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == j:
                    if board[i][j] != self.opponent:
                        opponent = False
                    if board[i][j] != self.selection:
                        myself = False
        if opponent:
            return -10
        if myself:
            return 10

        opponent = True
        myself = True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if j == len(board[0])-i-1:
                    if board[i][j] != self.opponent:
                        opponent = False
                    if board[i][j] != self.selection:
                        myself = False
        if opponent:
            return -10
        if myself:
            return 10

        # no one has won!
        return 0

    def moves_left(self, board: list) -> bool:
        for i, rows in enumerate(board):
            for j, value in enumerate(rows):
                if value == ' ':
                    return True
        return False

    def minmax(self, board: list, depth: int, isMax: bool, alpha: int, beta: int):
        """
        MinMax function. Consider all possibilities of the Tic Tac Toe Game
        and return the value of the given board
        """
        score = self.evaluate(board)

        # Max has won the Game
        if score == 10:
            return score

        # Min has won the Game
        if score == -10:
            return score

        # The game is a tie when there are no moves left
        if self.moves_left(board) == False:
            return 0

        # if it's Max turn
        if True == isMax:
            best = -1000
            # iterate on all empty spaces
            for i, rows in enumerate(board):
                for j, value in enumerate(rows):
                    if value == ' ': # space is empty
                        board[i][j] = self.selection  # make the move with Max
                        # recursively call Minmax
                        best = max(best, self.minmax(board, depth + 1, not isMax, alpha, beta))
                        alpha = max(best, alpha)
                        board[i][j] = ' '  # undo the move to have a clean board
                        if beta <= alpha:
                            break
            return best
        # Min turn
        else:    
            best = 1000
            # iterate on all empty spaces
            for i, rows in enumerate(board):
                for j, value in enumerate(rows):
                    if value == ' ': # space is empty
                        board[i][j] = self.opponent  # make the move with Max
                        # recursively call Minmax
                        best = min(best, self.minmax(board, depth + 1, not isMax, alpha, beta))
                        beta = min(best, beta)
                        board[i][j] = ' '  # undo the move to have a clean board
                        if beta <= alpha:
                            break
            return best
    
    def get_move(self, iboard: IBoard):
        """
        Find the best move available fot the AI opponent.
        Iterate all cell, evaluate MinMax function for all empty cells.
        Return the cell with optimal value
        """
        best_value = -1000
        best_move = -1

        board = iboard.board

        for i, rows in enumerate(board):
            for j, value in enumerate(rows):
                if value == ' ': # space is empty
                    board[i][j] = self.selection # make the move with the opponent
                    move_value = self.minmax(board, 0, False, -1000, 1000)
                    board[i][j] = ' ' # undo the move to have a clean board

                    if move_value > best_value:
                        best_move = (i,j)
                        best_value = move_value
        return best_move


# from tictactoe_board import TicTacToe_Board

# if __name__ == '__main__':

#     b.board = [
#         ['X',' ','O'],
#         [' ','O',' '],
#         ['O',' ','X']
#     ]
#     print(t.evaluate(b.board))