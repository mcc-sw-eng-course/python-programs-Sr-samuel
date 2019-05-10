from IBoard import IBoard, Square, Piece
from colorama import Fore, Back, Style 

# Colors

BLACK = '_'
WHITE = ' '

PLAYER1 = 'B'
PLAYER2 = 'W'

class Checkers_Board(IBoard):
    def __init__(self, size = 8):
        super(Checkers_Board, self).__init__(size)
        # Initialize colors for the board
        for i, _ in enumerate(self.board):
            for j, _ in enumerate(self.board[0]):
                if (i % 2 != 0) and (j % 2 == 0):
                    self.board[j][i] = Square(WHITE)
                elif (i % 2 != 0) and (j % 2 != 0):
                    self.board[j][i] = Square(BLACK)
                elif (i % 2 == 0) and (j % 2 != 0):
                    self.board[j][i] = Square(WHITE)
                elif (i % 2 == 0) and (j % 2 == 0): 
                    self.board[j][i] = Square(BLACK)
        
        # initialize the piece for each player
        for i, _ in enumerate(self.board):
            for j in range(3):
                if self.board[i][j].color == BLACK:
                    self.board[i][j].piece = Piece(PLAYER1)
            for j in range(5,8):
                if self.board[i][j].color == BLACK:
                    self.board[i][j].piece = Piece(PLAYER2)

    def render(self):
        board = self.board
        print("   ", end = '')
        for x in range(len(board[0])):
            print("\033[04m{0}\033[04m".format(x), end = ' ')
        print(Style.RESET_ALL)
        for i, rows in enumerate(board):
            print("{0} |".format(i) ,end = '')
            for j, val in enumerate(rows):
                if val.piece == None:
                    print(val.color, end = '')
                else:
                    print(val.piece.selection, end = '')
                if j != len(rows)-1:
                    print('|', end = '')
            print("| {0}".format(i) ,end = '')
            print()

    def position_inside_board(self,i,j):
        if (i >= 0 and i < 8 and j >= 0 and j < 8):
            return True
        else:
            return False

    def get_valid_moves(self, player):
        valid_moves = []
        for i, _ in enumerate(self.board):
            for j, _ in enumerate(self.board[0]):
                b = self.board[i][j]
                if (b.piece != None) and (b.piece.selection == player):
                    moves = self.get_moves_from((i,j))
                    if moves:
                        for move in moves:
                            valid_moves.append(move)
        return valid_moves

    def get_moves_from(self, pos: tuple):
        all_moves = []
        b = self.board
        x = pos[0]
        y = pos[1]
        # if the current position is not empty
        if b[x][y].piece != None:
            if b[x][y].piece.special == None and b[x][y].piece.selection == PLAYER2:
                all_moves = [(x-1, y-1), (x+1, y-1)]
            elif b[x][y].piece.special == None and b[x][y].piece.selection == PLAYER1:
                all_moves = [(x-1, y+1), (x+1, y+1)]
            else:
                all_moves = [(x-1, y-1), (x+1, y-1),(x-1, y+1), (x+1, y+1)]
        valid_moves = []
        for move in all_moves:
            # move inside the board
            i = move[0]
            j = move[1]
            eat_move = (i-x,j+(j-y))
            if self.position_inside_board(i,j):
                # if location in empty, we can move there
                if b[i][j].piece == None:
                    valid_moves.append([(pos),move, None])
                # if there is an enemy piece, we eat the piece
                elif (
                        (b[i][j].piece.selection != b[x][y].piece.selection) # if is my opponent
                        and (self.position_inside_board(eat_move[0], eat_move[1])) # the location to eat the piece is inside the board
                        and (b[eat_move[0]][eat_move[1]].piece == None) # the location to eat the piece is empty
                      ):
                    valid_moves.append([(pos),(i+(i-x),j+(j-y)),move])
        return valid_moves

    def make_move(self, move, player = None):
        start, end, eat = move
        self.board[end[0]][end[1]].piece = self.board[start[0]][start[1]].piece
        self.board[start[0]][start[1]].piece = None

        if eat:
            self.board[eat[0]][eat[1]].piece = None        

        # check if we are in an edge and make it king
        if ((self.board[end[0]][end[1]].piece.selection == PLAYER1 and end[1] == 0)
            or (self.board[end[0]][end[1]].piece.selection == PLAYER2 and end[1] == 7)):
            self.board[end[0]][end[1]].piece.special = True

    def player_won(self, player) -> bool:
        p1_pieces = 0
        p2_pieces = 0
        for i, _ in enumerate(self.board):
            for j, _ in enumerate(self.board[0]):
                b = self.board[i][j]
                if (b.piece != None) and b.piece.selection == PLAYER1:
                    p1_pieces += 1
                elif (b.piece != None) and b.piece.selection == PLAYER2:
                    p2_pieces += 1
        if PLAYER1 == player and p2_pieces == 0:
            return True
        elif PLAYER2 == player and p1_pieces == 0:
            return True
        else:
            return False

    def game_tied(self) -> bool:
        p1_moves = self.get_valid_moves(PLAYER1)
        p2_moves = self.get_valid_moves(PLAYER2)
        if p1_moves or p2_moves:
            return False
        else:
            return True



if __name__ == '__main__':
    cb = Checkers_Board()
    
    # cb.board[1][3].piece = Piece(PLAYER2)
    # cb.make_move((1,5),(0,4))
    cb.render()
    moves = cb.get_valid_moves(PLAYER2)
    print(moves)
    cb.make_move(moves[1])
    cb.render()
