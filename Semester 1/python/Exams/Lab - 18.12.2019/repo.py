from domain import *

class Repository:
    def __init__(self):
        self._data = []

    def add(self, object):
        '''
        Append new object to the list
        '''
        self._data.append(object)

    def find(self, id):
        for s in self._data:
            if int(s.ID) == int(id):
                return 1
        raise ValueError("ID not found")

    def getAll(self):
        return self._data

class TextRepository(Repository):
    def __init__(self, fileName, type):
        super().__init__()
        self._fileName = fileName
        self._type = type
        self._loadFile()

    def _loadFile(self):
        f = open(self._fileName, 'r')
        while True:
            s = f.readline().strip()
            if not s:
                break
            list = s.split(',')
            if self._type == 'o':
                object = Order(*list)
            else:
                object = Driver(*list)
            self.store(object)
        f.close()

    def store(self, object):
        Repository.add(self, object)

    def add(self, object):
        '''
        If we add a new order we need to update the file
        '''
        Repository.add(self, object)
        self._saveFile(object)

    def _saveFile(self, object):
        f = open(self._fileName, 'a')
        try:
            s = str(object.ID) + "," + str(object.Name) + '\n'
            f.write(s)
        except:
            s = str(object.ID) + "," + str(object.km) + '\n'
            f.write(s)
        f.close()