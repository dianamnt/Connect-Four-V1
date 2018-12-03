class Square:
    def __init__(self,x,y):
        '''
        Constructor for square class
        A square has 2 coordinates one for the line and one for the column
        '''
        self.__x = x 
        self.__y = y 
    
    def getX(self):
        '''
        Getter for lines
        '''
        return self.__x
    
    def getY(self):
        '''
        Getter for columns
        '''
        return self.__y