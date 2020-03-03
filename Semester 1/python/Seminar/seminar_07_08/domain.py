import unittest
'''
We want to use feature-driven development
    - we start impelemnting a feature and make it work :)
     - Add a new client. Each client is a physical person having a unique ID, name, age.

'''

'''
1. Write a Client class in the domain
    - Client has an ID(set in constructor, read-only otherwise)
    - CLient has a name of len >= 3 and an age >= 18(properties)
'''

class Client:
    def __init__(self, id, name, age):
        if id == None:
            raise ValueError("ID cannot be None!")
        self._clientId = id
        self.Name = name
        self.Age = age

    @property
    def id(self):
        return self._clientId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        if value == None or len(value) < 3:
            raise ValueError("Client name is too short!")
        else:
            self._name = value

    @property
    def Age(self):
        return self._age
    
    @Age.setter
    def Age(self, value):
        if value < 18:
            raise ValueError("Client is too young!")
        self._age = value

def __eq__(self, z):
    if isinstance(z, Client) == False:
        return False
    return self.id == z.id

def __str__(self):
    return "Id= " + str(self.id) + ", Name= " + self.Name + ", Age= " + str(self.Age)


'''
1. Must not forget to run my tests!
2. First test failure crashes my program :(
    -What s the status of remaining tests?
    -No reports, no feedback, nada
3. No difference between running the program and testing it
Support for running unit tests is spotty in VS Code
    - It's ok in PyCharm and Eclipse
    - Probably ok in VS Community 

'''
#special type of class which contains tests
#Python should find these classes and run the tests on its own
class TestClient(unittest.TestCase):  
    def test_client(self):
        c = Client(1, "Pop Andreea", 19)
        assert c.id == 1
        assert c.Name == "Pop Andreea"
        assert c.Age == 19

    def test_client_again(self):
        c = Client(1, "Pop Mihnea", 19)
        try:
            c.Age = 17
            assert False #Should have raised an exception
        except ValueError:
            assert True
        except Exception:
            assert False #a different exception was raised
