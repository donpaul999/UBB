from domain import *
from repo import *

class OrderSer:
    def __init__(self, OrderRep):
        self._orderRep = OrderRep

    def add(self, object, drivers):
        '''
        Append a new order to data, if order's distance and driver's ID are valid
        '''
        ok = 0
        if int(object.km) < 1:
            raise ValueError("Distance too short!")
        for i in drivers:
            if i.ID == object.ID:
                ok = 1
                break
        if ok == 0:
            raise ValueError("No driver with this id!")
        self._orderRep.add(object)

    def getAll(self):
        return self._orderRep.getAll()


class DriverSer:
    def __init__(self, DriverRep):
        self._driverRep = DriverRep

    def getAll(self):
        return self._driverRep.getAll()


class Service:
    def income(self, id, orders, drivers):
        sum = 0
        ok = 0
        for i in drivers:
            if int(i.ID) == int(id):
                driver = i.Name
                ok = 1
                break
        if ok == 0:
            print("NO driver with such ID!")
            return
        for s in orders:
            if int(s.ID) == id:
                sum = sum + int(s.km) * 2.5
        return driver,sum

