from domain import *
from repo import *
from ui import *
from service import *

orderRep = TextRepository("orders.txt", 'o')
driverRep = TextRepository("drivers.txt", 'd')

orderSer = OrderSer(orderRep)
driverSer = DriverSer(driverRep)
ser = Service()
ui = UI(orderSer, driverSer, ser)

ui.start()