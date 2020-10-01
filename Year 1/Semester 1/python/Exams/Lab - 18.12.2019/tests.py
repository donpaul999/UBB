import unittest
from domain import *
from service import *
from repo import *

class TestOrders(unittest.TestCase):
    def test_add_order(self):
        order = Order(1, 4)
        assert order.km == 4
        assert order.ID == 1
        o = Repository()
        d = Repository()
        os = OrderSer(o)
        d.add(Driver(1, "name"))
        o.add(Order(1,65))
        assert len(o._data) == 1
        try:
            os.add(Order(2,10), d._data)
            assert False
        except:
            assert True