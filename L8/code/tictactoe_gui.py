"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez

Development Exercises - L8
GUI for Tic Tac Toe Game using Tkinter
"""

from tkinter import Tk, Button, Label
from tkinter.font import Font
from tictactoe_board import tictactoe_board
from random import randint

class GUI:
    def __init__(self):
        """
        Creates the GUI for the Tic Tac Toe Game
        """
        self.gui = Tk()
        self.gui.title('TicTacToe')
        self.gui.resizable(width=False, height=False) # Can not resize the window
        
        self.buttons = []

        # In GUI mode the player is always X and the ai is always O
        self.player_selection = 'X'
        self.computer_selection = 'O'
        self.board = tictactoe_board(self.player_selection)

        self.size = 3 # size of the Tic Tac Toe board

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

        # Add the label to the GUI
        self.message = Label(self.gui, text="Your turn", font=message_font)
        self.message.grid(row=0, column=0, columnspan=self.size) # row 0

        # Creates a GRID of button, each button represent a space in the board
        for y in range(self.size):
            for x in range(self.size):
                handler = lambda x=x,y=y: self.move(x,y)
                button = Button(self.gui, command=handler, font=gui_font, width=2, height=1)
                button.grid(row=y+1, column=x) # add one to row to consider the label
                self.buttons.append(button)

        # add the Reset Button
        reset_handle = lambda: self.new_game()
        button = Button(self.gui, text='Reset', command=reset_handle)
        button.grid(row=self.size+2, column=0, columnspan=self.size, sticky="WE") # row grid.size + 2 (1 for the label, and 1 for the grid)

        # randomly select Player or AI
        self.select_turn() # Randomly select who will play first
        self.repaint_gui() # repaint the GUI

    def select_turn(self):
        if randint(0, 1) == 0: # AI goes first...
            # AI plays first
            self.message['text'] = "AI Turn"
            self.gui.config(cursor="watch") # make the cursos showing that we are thinking...
            self.gui.update()
            self.board.do_ai_move() # select the best move
            self.message['text'] = "Your Turn"
            self.gui.config(cursor="") # return to normal cursor
            
        else:
            # user goes first, wait for him to click...
            self.message['text'] = "Your Turn"
        self.gui.update()

    def new_game(self):
        self.board = tictactoe_board('X')
        self.select_turn() # Randomly select who will play first
        self.repaint_gui()

    def move(self, x, y):
        # convert the move from 2D to a 1D array as we need it
        move = (y * self.size + x) + 1  # we  ignore the 0 position, we add 1
        self.gui.config(cursor="watch") # make the cursos showing that we are thinking...
        self.gui.update()               # update the gui
        self.board.do_player_move(move) # Update the board with the players move
        self.message['text'] = "AI Turn"
        self.repaint_gui()              # repaint the GRID, to show the X where the player clicked
        self.board.do_ai_move()         # select the best move for the AI
        self.message['text'] = "Your Turn"
        self.repaint_gui()              # repaint the GRID, to show the O where the AI selected
        self.gui.config(cursor="")      # return to normal cursor
        self.gui.update()               # update the GUI
        pass

    def repaint_gui(self):
        bo = self.board.board
        iterboard = iter(bo)    # Get Iterator for Board
        next(iterboard)         # Skip the first position 0
        # iterate on all empty spaces
        for i, space in enumerate(iterboard):
            self.buttons[i]['text'] = space                 # Update the text of the button can be empty, X or O
            self.buttons[i]['disabledforeground'] = 'gray'  # change the color to white
            if space == ' ':
                self.buttons[i]['state'] = 'normal'         # make the button clickable when its empty
            else:
                self.buttons[i]['state'] = 'disabled'       # make the button un-clickable when it has an X or O
            self.buttons[i].update()

        if self.board.player_won() or self.board.ai_won() or self.board.tied():
            # disable all buttons when the game is over
            for button in self.buttons:
                button['state'] = 'disabled'

        if self.board.player_won():
            moves = self.board.get_winning_moves(self.player_selection)
            self.paint_winning_moves(moves, 'red')
            self.message['text'] = "You Won :)"
        elif self.board.ai_won():
            moves = self.board.get_winning_moves(self.computer_selection)
            self.paint_winning_moves(moves, 'red')
            self.message['text'] = "AI Won :("
        elif self.board.tied():
            self.message['text'] = "Game is tied"
            for button in self.buttons:
                button['disabledforeground'] = 'black'
        else:
            pass

    def paint_winning_moves(self, moves: list, color: str):
        for i, button in enumerate(self.buttons): # iterate through all the button and paint red to show winning moves
            i += 1
            if i in moves:
                button['disabledforeground'] = color


    def mainloop(self):
        self.gui.mainloop()


if __name__ == '__main__':
    GUI().mainloop()