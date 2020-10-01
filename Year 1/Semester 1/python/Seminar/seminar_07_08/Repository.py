import copy
import unittest
'''
Write a ClientRepository class:
    - it keeps a list of clients(private)
    - function to add a new client(raise exception if client with same ID already in repo)
    - function that returns all clients

several lists in one Repo class is not a good idea

    how to implrement repo
    -> 1. Separate repo class for each entity(CarRepo, ClientRepo, RentalRepo)
        + Different functionalities for each entity
        - More code
    -> 2. A general Repo class
        + Less code (No code duplication) -> fewer opportunities for bugs, easier to understand
        - Only common stuff


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

class Repository:
    def __init__(self):
        self._data = []
        
        
    def size(self):
        return len(self._data)
    
    def find(self, value):
        if value not in self._data:
            raise RepoError("ID is not in the list!")
        for x in self._data:
            if x.id ==  value:
                return x
            
    def store(self, value):
        if value in self._data:
            raise RepoError("ID already in the list!")
        self._data.append(value)
    
    def delete(self, value):
        self._data.remove(value)


class RepoTest(unittest.TestCase):
    def testRepo(self):
        r = Repository()
        #check length of repo using len()
        self.assertEquals(0, len(r))
        r.store((c := Client(1,"Ana", 19)))
        self.assertEquals(1,len(r))
        #use [] operator to access repo stuff
        self.assertEquals(c, r[0]) # __getitem__
        r.store((c2 := Client(2, "Marius", 20)))
        self.assertEquals(2, len(r))
        self.assertEquals(c, r[0])
        self.assertEquals(c2, r[1])
        #client with id 2 is at index 1
        self.assertEquals(1,r.find(2))
        #trying to add Marius again shoud raise an exception
        self.assertRaises(RepositoryException, r.store, c2)
        #delete clients from repo
        r.delete(1)
        r.delete(2)
        self.assertEquals(0, len(r))














