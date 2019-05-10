from IPlayer import IPlayer
from IBoard import IBoard

class HumanPlayer(IPlayer):
    def __init__(self, selection: str):
        super(HumanPlayer, self).__init__(selection)

    def get_move(self, board: IBoard) -> tuple:
        valid_moves = board.get_valid_moves(self.selection)
        for i, move in enumerate(valid_moves):
            print("{0}: {1}".format(i, move), end=', ')
        move = input()
        move = int(move)
        return valid_moves[move]