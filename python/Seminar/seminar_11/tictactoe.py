'''
TicTacToe
Player vs Computer (player moves first)
Validate everything
Computer moves
    Lvl1 always make valid moves
    Lvl2 takes all 1-move wins
    Lvl3 prevent player's 1-move wins
'''

from texttable import Texttable #! THIS IS IMPORTANT FOR THIS CODE TO WORK - download texttable.py from here: https://github.com/foutaise/texttable
                                # and insert it into lib folder

import random

#decide the computer's next move
class RandomMoveComputer:
    def calculateMove(self, board):
        candidates = []
        for i in range(3):
            for j in range(3):
                if board.get(i, j) == 0:
                    candidates.append((i, j))
        return random.choice(candidates)

class SimpletonComputer:
    def calculateMove(self, board):
        # returns (x,y) fot computer move
        for i in range(3):
            for j in range(3):
                if board.get(i, j) == 0:
                    return (i, j)
        raise ValueError("Board is full!")


class Game: # a kind of controller/service
    def __init__(self, board, computerPlayer):
        self._board = board
        self._computerPlayer = computerPlayer

    def playerMove(self, x, y):
        self._board.move(x,y,'X')

    def getBoard(self):
        return self._board

    def computerMove(self):
        move = self._computerPlayer.calculateMove(self._board)
        # computer must generate valid moves only
        # this should raise no exceptions
        self._board.move(move[0], move[1], 'O')


class Board:
    def __init__(self):
        self._data = [0] * 9
        self._moves = 0
        # empty square - 0
        # X - 1
        # O - -1

    def get(self, x, y):
        # maybe transform to X, O
        return self._data[3 * x + y]

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
        self._moves += 1

    def isWon(self):
        #check rows and columns
        for i in range(3):
            row = self._data[3*i:3*i+3]
            col = self._data[i:i+7:3]
            if abs(sum(row)) == 3 or abs(sum(col)) == 3:
                return True
        d = self._data
        if abs(d[0] + d[4] + d[8]) == 3:
            return True
        if abs(d[2] + d[4] + d[6]) == 3:
            return True

        return False

    def isTie(self):
        return self.isWon() == False and self._moves  == 9

    def __str__(self):
        t = Texttable()
        d = {-1: 'O', 0: ' ', 1: 'X'}
        for i in range(0, 8, 3):
            row = self._data[i:i+3]
            for j in range(3):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()


class UI:
    def __init__(self, game):
        self._game = game

    def _readPlayerMove(self):
        # Return the (x,y) tuple that represents the player's move
        # > 1 2
        while True:
            try:
                cmd = input("Insert move:").split(" ")
                return(int(cmd[0]), int(cmd[1]))
            except Exception:
                print("Invalid coordinates!")

    def start(self):
        b = self._game.getBoard()
        playerMove = True
        while b.isWon() == False and b.isTie() == False:
            #while condition must be checked after each move
            print(b)
            if playerMove == True:
                try:
                    move = self._readPlayerMove()
                    self._game.playerMove(move[0], move[1])
                except Exception as e:
                    print(e)
                    continue
            else:
                self._game.computerMove()
            playerMove = not playerMove

        if b.isTie():
            print("It's a draw!")
        elif playerMove == False:
            print("Congrats! You won!")
        else:
            print("You were defeated!")
        print(b)


b = Board()
ai = RandomMoveComputer()
g = Game(b, ai)
ui = UI(g)
ui.start()
'''
b.move(1,1,'X')
b.move(0,0, 'X')
b.move(2,2, 'X')
print(b.isWon())
print(b)
'''