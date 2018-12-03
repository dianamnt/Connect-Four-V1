from board.board import Board
from square.square import Square
from random import randint
class Game:
    def __init__(self):
        '''
        Constructor for game class
        '''
        self._board = Board()
        
    def playerMove(self,l,c):
        '''
        Assigns the sing 'x' to the square wanted by the player if the conditions for doing so are met
        '''
        self._board.play('x', l, c)
        
    def computerMove(self):
        '''
        Assigns the sing 'q' to the square wanted by the computer
        '''
        empty = self._board.getFreeSquares()
        s = 0
        if len(empty) != 0:
            work = True
            while work:
                c = randint(0,6)
                l = self._board.detLine(c)
                if l != -1:
                    s = Square(l,c)
                    work = False 
        self._board.play('q', s.getX(), s.getY())
        return s
    
    def isFull(self):
        '''
        Determines whether the board is full or not
        '''
        if self._board.isFull() == True:
            return True
        else:
            return False
        
    def __str__(self):
        '''
        Depicts graphically the board
        '''
        return self._board.__str__()
    
    def getBoard(self):
        return self._board
    
    def isWon(self):
        '''
        Determines whether the game is won, unfinished or a draw
        '''
        b = self._board.getBoard()
        '''
        Verifies groups of 4 on lines
        '''
        for i in range(0,6):
            if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] == b[i][3] and b[i][0] in ['x','q']:
                return True
            if b[i][1] == b[i][2] and b[i][1] == b[i][3] and b[i][1] == b[i][4] and b[i][1] in ['x','q']:
                return True
            if b[i][2] == b[i][3] and b[i][2] == b[i][4] and b[i][2] == b[i][5] and b[i][2] in ['x','q']:
                return True
            if b[i][3] == b[i][4] and b[i][3] == b[i][5] and b[i][3] == b[i][6] and b[i][3] in ['x','q']:
                return True
        '''
        Verifies groups of 4 on columns
        '''
        for i in range(0,7):
            if b[0][i] == b[1][i] and b[0][i] == b[2][i] and b[0][i] == b[3][i] and b[0][i] in ['x','q']:
                return True
            if b[1][i] == b[2][i] and b[1][i] == b[3][i] and b[1][i] == b[4][i] and b[1][i] in ['x','q']:
                return True
            if b[2][i] == b[3][i] and b[2][i] == b[4][i] and b[2][i] == b[5][i] and b[2][i] in ['x','q']:
                return True
        '''
        Verifies groups of 4 on diagonals
        '''
        # secondary diagonals
        if b[3][0] == b[2][1] and b[3][0] == b[1][2] and b[3][0] == b[0][3] and b[3][0] in ['x','q']:
            return True
        if b[4][0] == b[3][1] and b[4][0] == b[2][2] and b[4][0] == b[1][3] and b[4][0] in ['x','q']:
            return True
        if b[3][1] == b[2][2] and b[3][1] == b[1][3] and b[3][1] == b[0][4] and b[3][1] in ['x','q']:
            return True
        if b[5][0] == b[4][1] and b[5][0] == b[3][2] and b[5][0] == b[2][3] and b[5][0] in ['x','q']:
            return True
        if b[4][1] == b[3][2] and b[4][1] == b[2][3] and b[4][1] == b[1][4] and b[4][1] in ['x','q']:
            return True
        if b[3][2] == b[2][3] and b[3][2] == b[1][4] and b[3][2] == b[0][5] and b[3][2] in ['x','q']:
            return True
        if b[5][1] == b[4][2] and b[5][1] == b[3][3] and b[5][1] == b[2][4] and b[5][1] in ['x','q']:
            return True
        if b[4][2] == b[3][3] and b[4][2] == b[2][4] and b[4][2] == b[1][5] and b[4][2] in ['x','q']:
            return True
        if b[3][3] == b[2][4] and b[3][3] == b[1][5] and b[3][3] == b[0][6] and b[3][3] in ['x','q']:
            return True
        if b[5][2] == b[4][3] and b[5][2] == b[3][4] and b[5][2] == b[2][5] and b[5][2] in ['x','q']:
            return True
        if b[4][3] == b[3][4] and b[4][3] == b[2][5] and b[4][3] == b[1][6] and b[4][3] in ['x','q']:
            return True
        if b[5][3] == b[4][4] and b[5][3] == b[3][5] and b[5][3] == b[2][6] and b[5][3] in ['x','q']:
            return True
        
        # main diagonals
        if b[5][3] == b[4][2] and b[5][3] == b[3][1] and b[5][3] == b[2][0] and b[5][3] in ['x','q']:
            return True
        if b[5][4] == b[4][3] and b[5][4] == b[3][2] and b[5][4] == b[2][1] and b[5][4] in ['x','q']:
            return True
        if b[4][3] == b[3][2] and b[4][3] == b[2][1] and b[4][3] == b[1][0] and b[4][3] in ['x','q']:
            return True
        if b[5][5] == b[4][4] and b[5][5] == b[3][3] and b[5][5] == b[2][2] and b[5][5] in ['x','q']:
            return True
        if b[4][4] == b[3][3] and b[4][4] == b[2][2] and b[4][4] == b[1][1] and b[4][4] in ['x','q']:
            return True
        if b[3][3] == b[2][2] and b[3][3] == b[1][1] and b[3][3] == b[0][0] and b[3][3] in ['x','q']:
            return True
        if b[5][6] == b[4][5] and b[5][6] == b[3][4] and b[5][6] == b[2][3] and b[5][6] in ['x','q']:
            return True
        if b[4][5] == b[3][4] and b[4][5] == b[2][3] and b[4][5] == b[1][2] and b[4][5] in ['x','q']:
            return True
        if b[3][4] == b[2][3] and b[3][4] == b[1][2] and b[3][4] == b[0][1] and b[3][4] in ['x','q']:
            return True
        if b[4][6] == b[3][5] and b[4][6] == b[2][4] and b[4][6] == b[1][3] and b[4][6] in ['x','q']:
            return True
        if b[3][5] == b[2][4] and b[3][5] == b[1][3] and b[3][5] == b[0][2] and b[3][5] in ['x','q']:
            return True
        if b[3][6] == b[2][5] and b[3][6] == b[1][4] and b[3][6] == b[0][3] and b[3][6] in ['x','q']:
            return True
        
        return False