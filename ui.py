from game.game import Game
class UI:
    def __init__(self):
        '''
        Constructor for UI class
        '''
        self.__game = Game()
        
    def gameUI(self):
        print("~~~ START GAME ~~~")
        player = True
        name = str(input("Enter your name: "))
        print(self.__game.__str__())
        while self.__game.isFull() == False and self.__game.isWon() == False:
            if player:
                try:
                    cmd = input("Enter the coordinates to your next move in the following way: <line>,<column>   --->   ")
                    cmd = cmd.strip().split(',')
                    cmd = [int(x) for x in cmd]
                    if len(cmd) != 2:
                        raise Exception("Invalid command format! Command must given as: <line>,<column>")
                    player = False
                    self.__game.playerMove(cmd[0], cmd[1])
                except Exception as e:
                    print(e)
                    player = True
            else:
                s = self.__game.computerMove()
                player = True
            print(self.__game.__str__())
        
        if player == False:
            print(str(name) + " WON!")
        else:
            print("COMPUTER WON!")