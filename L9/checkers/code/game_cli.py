
from IBoard import IBoard
from IPlayer import IPlayer
from tictactoe_human import HumanPlayer
from tictactoe_ai import TicTacToe_AI
from random import randint
from tictactoe_board import TicTacToe_Board
from checkers_board import Checkers_Board, PLAYER1, PLAYER2

class CLI():
    def __init__(self, board: IBoard, player1: IPlayer, player2: IPlayer):
        self.m_board = board
        self.m_player1 = player1
        self.m_player2 = player2
        self.new_game()

    def select_first_turn(self):
        if randint(0, 1) == 0:
            self.m_current_turn = 0
        else:
            self.m_current_turn = 1

    def new_game(self):
        self.m_current_turn = -1
        self.m_playing = True

    def render(self):
        self.m_board.render()

    def mainloop(self):
        self.select_first_turn()
        while self.m_playing:
            self.render()
            if self.m_current_turn == 0:
                print("Player 1 Turn")
                move = self.m_player1.get_move(self.m_board)
                self.m_board.make_move(move, self.m_player1.selection)
                if self.m_board.player_won(self.m_player1.selection):
                    self.render()
                    print("Player 1 Won")
                    self.m_playing = False
                self.m_current_turn = 1
                    
            elif self.m_current_turn == 1:
                print("Player 2 Turn")
                move = self.m_player2.get_move(self.m_board)
                self.m_board.make_move(move, self.m_player2.selection)
                if self.m_board.player_won(self.m_player2.selection):
                    self.render()
                    print("Player 2 Won")
                    self.m_playing = False
                self.m_current_turn = 0

            if self.m_board.game_tied():
                self.render()
                print("Game is a tie")
                self.m_playing = False

if __name__ == '__main__':
    CLI(TicTacToe_Board(3), TicTacToe_AI("X"), TicTacToe_AI("O")).mainloop()
    # CLI(Checkers_Board(), HumanPlayer(PLAYER1), HumanPlayer(PLAYER2)).mainloop()
    
