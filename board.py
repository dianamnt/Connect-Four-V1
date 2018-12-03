from square.square import Square
class Board:
    def __init__(self):
        '''
        Constructor for board class
        A board is a matrix with 7 columns and 6 lines
        '''
        self._b = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    
    def isFree(self,l,c):
        '''
        Determines whether a square is free or not
        Free squares are represented by 0 elements in the board matrix
        '''
        if self._b[l][c] == 0:
            return True
        else: 
            return False
        
    def getFreeSquares(self):
        '''
        Gets all the free squares on the board 
        '''
        rez = []
        for i in range(0,6):
            for j in range(0,7):
                if self.isFree(i, j) == True:
                    rez.append(Square(i,j))
        return rez
    
    def isFull(self):
        '''
        Determines whether the board is full or not
        '''
        if len(self.getFreeSquares()) == 0:
            return True
        else:
            return False
        
    def getBoard(self):
        '''
        Getter for the board matrix
        '''
        return self._b 
    
    def __str__(self):
        '''
        Graphical depiction of the board
        '''
        s = ""
        for i in reversed(range(0,6)):
            for j in range(0,7):
                s = s + str(self._b[i][j]) + " "
            s = s + "\n"
        return s 
    
    def detLine(self, c):
        '''
        Determines the lowest empty line from the specified column
        '''
        for i in range(0,6):
            if self.isFree(i, c) == True:
                return i
        return -1
         
    def play(self,player,l,c):
        '''
        Determines the conditions on which the game may be played
        '''
        if l < 0 or l > 5 or c < 0 or c > 6:
            raise Exception("Wrong coordinates!")
        if player not in ['x','q']:
            raise Exception("Wrong sign used!")
        if self.isFree(l, c) == False:
            raise Exception("Position already occupied!")
        if self.detLine(c) != l:
            raise Exception("Invalid position!")
        self._b[l][c] = player