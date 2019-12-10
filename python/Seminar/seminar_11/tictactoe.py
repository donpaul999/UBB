'''
TicTacToe
Player vs Computer (player moves first)
Validate everything
Computer moves
    Lvl1 always make valid moves
    Lvl2 takes all 1-move wins
    Lvl3 prevent player's 1-move wins
'''

from texttable import Texttable


class UI:
    pass

#decide the computer's next move
class SimpletonComputer:
    def calculateMove(self, ):
        pass


class Game: # a kind of controller/service
    pass

class Board:
    def __init__(self):
        self._data = [0] * 9
        # empty square - 0
        # X - 1
        # O - -1

    def move(self, x, y, symbol):
        #x, y in [0,1,2], symbol in [X,O]
        d = {'O': -1 , 'X': 1}
        if x not in [0,1,2] or y not in [0,1,2]:
            raise ValueError("Move not inside the board!")
        if self._data[3 * x + y] != 0:
            raise ValueError("Square is already taken!")
        if symbol not in ['X', 'O']:
            raise ValueError("Bad Symbol!")

        self._data[3 * x + y] = d[symbol]


    def __str__(self):
        t = Texttable()
        d = {-1: 'O', 0: ' ', 1: 'X'}
        for i in range(0, 8, 3):
            row = self._data[i:i+3]
            for j in range(3):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()


b = Board()
b.move(1,1,'X')
b.move(0,0, 'O')
b.move(2,2, 'X')
print(b)
