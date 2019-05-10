
class Piece():
    def __init__(self, selection, special = None):
        # Checkers: [WHITE, BLACK] 
        # TicTacToe: [X,Y]
        self.selection = selection
        # special attributes, i.e King in checkers
        self.special = special

class Square():
    def __init__(self, color, piece = None):
        self.color = color
        self.piece = piece

class IBoard():
    def __init__(self, size: int):
        self.board = []
        if isinstance(size, int):
            self.board = [[None] * size for i in range(size)]
            for i, _ in enumerate(self.board):
                for j, _ in enumerate(self.board[0]):
                    self.board[i][j] = Square('.')

    def render(self):
        raise NotImplementedError

    def player_won(self, player) -> bool:
        raise NotImplementedError

    def game_tied(self) -> bool:
        raise NotImplementedError

    def get_valid_moves(self) -> list:
        raise NotImplementedError

    def is_move_valid(self, move: tuple) -> bool:
        raise NotImplementedError

    def make_move(self, move, player) -> bool:
        raise NotImplementedError