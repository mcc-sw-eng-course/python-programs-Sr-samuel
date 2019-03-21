# Python Programs for MCC SW Engineering Course

Author: Samuel Solorzano Ramirez (A00354798)

Course: Analysis, Design, and Construction of Software Systems

Teacher: Dr. Gerardo Padilla

## L8 Development Exercise

- Design a game to play Tic-Tac-Toe (Gato)
- The interface could be text-based or graphical
- The program should implement the logic to play against one human player
- Add a test file explaining how you design the game
- Be prepare to define classes for a future checkers game


## Coverage Report

| Module                | Stmts| Miss|Branch|BrPart| Cover|
|-----------------------|------|-----|------|------|------|
|tictactoe_board.py     |    71|    7|    38|     7|   87%|
|tictactoe_ai.py        |    96|    1|    60|     3|   97%|
|test_tictactoe_board.py|    89|    4|     2|     1|   95%|
|test_tictactoe_ai.py   |    74|    0|     2|     1|   99%|
|TOTAL                  |   330|   12|   102|    12|   94%|

Files:

- tictactoe_board.py
  - Board Class, handle all the logic for the Tic Tac Toe Game
- tictactoe_ai.py
  - AI for the Tic Tac Toe AI player, selects the Best Move based on the Min Max Algorithm optimized with AB Pruning.
- tictactoe_text.py
  - Text Interface for the Tic Tac Toe, uses the board class.
- tictactoe_gui.py
  - GUI Interface for the Tic Tac Toe game, uses the board class.
- test_tictactoe_board.py
  - Unit testing for the Board class
- test_tictactoe_ai.py
  - Unit testing for the AI class.

![Tic Tac Toe Class](tictactoe_class_diagram.png "Tic Tac Toe Class")