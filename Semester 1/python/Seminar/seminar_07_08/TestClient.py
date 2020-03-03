import unittest
from Client import Client

class TestClientAgain(unittest.TestCase):  
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
