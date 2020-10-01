import unittest
from domain import *
class TestCase(unittest.TestCase):
    def test_string(self):
        assert st.Name == "test"