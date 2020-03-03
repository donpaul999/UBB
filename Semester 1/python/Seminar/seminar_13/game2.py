from texttable import Texttable
import random

class SteppedOnMineException(Exception):
    pass

class Field:
    '''
    Represents one square of minefield
    Has coordinates, and a state value (mine or non-mine)
    '''
    def __init__(self, x, y,state):
        self._x = x
        self._y = y
        self._state = state

    def reveal(self):
        self._revealed = True

class Board:
    def __init__(self, width, height, mines):
        self._w = width
        self._h = height
        self._mines = mines
        self._data = []
        #Have a matrix of revealed fields
        self._reveal = []
        for i in range(height):
            self._data.append([0] * self._w)
        for i in range(height):
            self._reveal.append([0] * self._w)
        #Lay the mines
        self._layMines()
        self._computeNeighbours()


    def _computeNeighbours(self):
        for x in range(self._h):
            for y in range(self._w):
                if self._data[x][y] == -1:
                    continue
                mines = 0
                for ng in self._neighbours(x,y):
                    if self._data[ng[0]][ng[1]] == -1:
                        mines += 1
                self._data[x][y] = mines


    def _layMines(self):
        indices = list(range(0,self._w * self._h))
        for i in range(self._mines):
            val = random.choice(indices)
            indices.remove(val)
            self._data[val // self._w][val % self._w] = -1

    def _neighbours(self, x, y):
        w = self._w
        h = self._h
        res = []
        res.append((x - 1, y - 1))
        res.append((x - 1, y))
        res.append((x - 1, y + 1))
        res.append((x, y - 1))
        res.append((x,y + 1))
        res.append((x + 1, y - 1))
        res.append((x + 1, y))
        res.append((x + 1, y + 1))
        poz = 0
        while poz < len(res):
            sq = res[poz]
            if sq[0] < 0 or sq[0] >= h or sq[1] < 0 or sq[1] >= w:
                res.remove(sq)
            else:
                poz += 1
        return res

    def move(self,x,y):
        if x < 0 or y < 0 or x >= self._h or y >= self._w:
            raise ValueError("Step in the minefield!")
        if self._data[x][y] == -1:
            raise SteppedOnMineException()
        #no mine neighbours
        stack = []
        stack.append((x,y))
        while len(stack) > 0:
            f = stack.pop()
            self._reveal[f[0]][f[1]] = self._data[f[0]][f[1]]
            for n in self._neighbours(f[0], f[1]):
                self._reveal[n[0]][n[1]] = self._data[n[0]][n[1]]
                if self._data[n[0]][n[1]] == 0:
                    stack.append(n)


    def __str__(self):
        #Debug purposes
        t = Texttable()
        for i in range(self._h):
            t.add_row(self._data[i])
        print(t.draw())

        #until here
        t = Texttable()
        for i in range(self._h):
            t.add_row(self._reveal[i])

        return t.draw()


b = Board(6,6,5)
b.move(0,0)
print(b)