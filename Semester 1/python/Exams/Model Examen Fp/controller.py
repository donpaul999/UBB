from Repo import *

class Service:
    def __init__(self, Repo):
        self._Repo = Repo

    def calcScore(self, string):
        self._Repo.calcScore(string)

    def selectS(self):
        return self._Repo.selectS()

    def verify(self, obj):
        if obj._string == obj._start:
            return True
        return False

    def shuffle(self, obj):
        str = obj._start
        words = 0
        for i in range(1, len(str) - 1):
            if str[i] == " " and str[i - 1] != " ":
                words += 1
        shuffles = obj._score - words * 2
        


    def swap(self, w1, p1, w2, p2, string):
        if w1 > w2:
            raise ValueError("Bad order for the parameters!")
        string._history = string._string
        str = string._string
        words = 1
        i = 1
        while i < len(str) - 1:
           if words < w1:
               if str[i] == " " and str[i + 1] != " ":
                    words += 1
           else:
               break
           i += 1
        if words < w1 or i == len(str) - 1:
            raise ValueError("Bad parameters!")
        j = i
        while j < p1 + i and str[j] != ' ':
            j += 1
        if str[j] == ' ':
            raise ValueError("Bad parameters!")

        while i < len(str) - 1:
           if words < w2:
               if str[i] == " " and str[i + 1] != " ":
                    words += 1
           else:
               break
           i += 1

        if i == len(str) - 1 or words < w2:
            raise ValueError("Bad parameters!")

        k = i
        while k < p2 + i and str[k] != ' ':
            k += 1
        if str[k] == ' ':
            raise ValueError("Bad parameters!")

        aux = str[j]
        str[j] = str[k]
        str[k] = aux

        string._string = str
        string._score -= 1

    def score(self, obj):
        return obj._score



