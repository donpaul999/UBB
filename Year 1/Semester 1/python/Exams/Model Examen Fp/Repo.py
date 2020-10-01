import random

class Repository:
    def __init__(self):
        self._data = []

    def add(self, object):
        self._data.append(object)

    def selectS(self):
        self._loadFile()
        string = random.choice(self._data)
        return string

    def calcScore(self, string):
        score = 0
        for i in range(len(string._start)):
            if string._start[i] != ' ':
                score += 1
        return score
