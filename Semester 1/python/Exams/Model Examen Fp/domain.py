class String:
    def __init__(self, string):
        self._start = string
        self._string = string
        self._score = 0
        self._history = ""

    def __len__(self):
        return len(self._start)

    @property
    def Sentence(self):
        return self._string

    @property
    def Display(self):
        return self._start

    @Display.setter
    def Display(self, value):
        self._string = value

    @property
    def Score(self):
        return self._score

    @Score.setter
    def Score(self, value):
        self._score = value

    @property
    def History(self):
        return self._history

    @History.setter
    def History(self, value):
        self._history = value

    def __str__(self):
        return str(self.Sentence)

    @staticmethod
    def readEntity(line):
        sentence = line.strip()
        return String(sentence)
