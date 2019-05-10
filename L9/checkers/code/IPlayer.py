from IBoard import IBoard

class IPlayer():
    def __init__(self, selection: str):
        self.selection = selection

    def get_move(self, board: IBoard):
        raise NotImplementedError


class AIPlayer(IPlayer):
    def __init__(self, selection: str):
        super(AIPlayer, self).__init__(selection)

    def evaluate(self):
        raise NotImplementedError

    def minmax(self):
        raise NotImplementedError

    def get_move(self, board: IBoard):
        raise NotImplementedError

