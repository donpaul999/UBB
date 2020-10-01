from Repo import *
from domain import *

class TextRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self._fileName = fileName
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, 'r')
        while True:
            s = f.readline()
            if not s:
                break
            self.store(String(s))
        f.close()

    def store(self, object):
        Repository.add(self, object)


