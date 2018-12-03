import unittest
from square.square import Square
from board.board import Board
from game.game import Game

class TestSquare(unittest.TestCase):
    def testGetX(self):
        self.s = Square(0,3)
        self.assertEqual(self.s.getX(),0)
        
    def testGetY(self):
        self.s = Square(4,5)
        self.assertEqual(self.s.getY(),5)
        
class TestBoard(unittest.TestCase):
    def setUp(self):
        self._b = Board()
        
    def testIsFree(self):
        for i in range(0,6):
            for j in range(0,7):
                self.assertEqual(self._b.isFree(i, j),True)
    
    def testGetFreeSquares(self):
        self.assertEqual(len(self._b.getFreeSquares()),42)
        
    def testIsFull(self):
        self.assertEqual(self._b.isFull(),False)
        
    def test__str__(self):
        self.assertEqual(self._b.__str__(),"0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n")
        
    def testDetLine(self):
        for i in range(0,7):
            self.assertEqual(self._b.detLine(i),0)
    
    def testPlay(self):
        with self.assertRaises(Exception):
            self._b.play('x',-1,-1)
            
        with self.assertRaises(Exception):
            self._b.play('x',2,3)
        
        with self.assertRaises(Exception):
            self._b.play('0',0,0)
    
class TestGame(unittest.TestCase):
    def setUp(self):
        self._g = Game()
        
    def testPlayerMove(self):
        self._g.playerMove(0, 0)
        b = self._g._board.getBoard()
        self.assertEqual(b[0][0],'x')
    
    def testComputerMove(self):
        s = self._g.computerMove()
        sl = s.getX()
        sc = s.getY()
        b = self._g._board.getBoard()
        self.assertEqual(b[sl][sc],'q')
    
    def testIsWon(self):
        self.assertEqual(self._g.isWon(),False)
        
    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()