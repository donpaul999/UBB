import copy
'''
Write a ClientRepository class:
    - it keeps a list of clients(private)
    - function to add a new client(raise exception if client with same ID already in repo)
    - function that returns all clients
'''

class ClientRepository:
    def __init__(self):
        self._data = []
    
    def store(self, client):
        pass
    
    def delete(self, clientID):
        pass

    def find(self, clientID):
        pass
    
    def getAll(self):
        #Returns a refference to the live list
        return self._data
        #maybe copy here for safety?
        return self._data[:]
        #Even safer
        return copy.deepcopy(self._data)

