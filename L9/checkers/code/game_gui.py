

from IBoard import IBoard
from IPlayer import IPlayer
from tictactoe_human import HumanPlayer
from tictactoe_ai import TicTacToe_AI
from random import randint
from tictactoe_board import TicTacToe_Board

from tkinter import Tk, Button, Label
from tkinter.font import Font

class GUI():
    def __init__(self, board: IBoard, player1: IPlayer, player2: IPlayer):
        self.gui = Tk()
        self.gui.title('TicTacToe')
        self.gui.resizable(width=False, height=False) # Can not resize the window

        self.buttons = []

        self.m_board = board
        self.m_player1 = player1
        self.m_player2 = player2

        # fonts used for the GUI
        gui_font = Font(family='Arial', size=32)
        message_font = Font(family='Helvetica', size=22)

        """
        The GUI will be order like this:
        |  Message  | -> Label showing the message
        |   |   |   | -> 3x3 Grid, containing the board
        |   |   |   |  -> Buttons clickable by User
        |   |   |   | 
        | Reset Btn | -> Reset Button, to start a new game
        """

        self.size = len(self.m_board.board)

        # Add the label to the GUI
        self.message = Label(self.gui, text="Your turn", font=message_font)
        self.message.grid(row=0, column=0, columnspan=self.size) # row 0

        # Creates a GRID of button, each button represent a space in the board
        for y in range(self.size):
            for x in range(self.size):
                # handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self.gui, command=None, font=gui_font, width=2, height=1)
                button.grid(row=y+1, column=x) # add one to row to consider the label
                self.buttons.append(button)

        # add the Reset Button
        reset_handle = lambda: self.new_game()
        button = Button(self.gui, text='Reset', command=reset_handle)
        button.grid(row=self.size+2, column=0, columnspan=self.size, sticky="WE")

        self.gui.update()

    def select_first_turn(self):
        if randint(0, 1) == 0:
            self.m_current_turn = 0
        else:
            self.m_current_turn = 1

    def new_game(self):
        self.m_current_turn = -1
        self.m_playing = True

    def render(self):
        pass

    def mainloop(self):
        self.gui.mainloop()

if __name__ == '__main__':
    GUI(TicTacToe_Board(3), HumanPlayer("X"), TicTacToe_AI("O")).mainloop()