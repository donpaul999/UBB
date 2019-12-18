from domain import *

class UI:
    def __init__(self, orderSer, driverSer, Service):
        self._orderSer = orderSer
        self._driverSer = driverSer
        self._service = Service

    def print_stars(self):
        print("****************")

    def addOrder(self):
        id = input("Input id: ")
        km = input("Input distance: ")
        try:
            drivers = self._driverSer.getAll()
            self._orderSer.add(Order(id, km), drivers)
        except ValueError as e:
            self.print_stars()
            print(e)
            self.print_stars()

    def printOrders(self):
        self.print_stars()

        ok = 0
        id = 0
        orders = self._orderSer.getAll()
        drivers = self._driverSer.getAll()
        for i in orders:
            for j in drivers:
                if i.ID == j.ID:
                    driver = j.Name
                    break
            print(driver + ": " + str(i.km))
        self.print_stars()


    def printIncome(self):
        id = input("Input id: ")
        drivers = self._driverSer.getAll()
        orders = self._orderSer.getAll()
        driver,income = self._service.income(int(id), orders, drivers)
        print(driver +": " + str(income))

    def print_menu(self):
        print("1. Add an order")
        print("2. Display all orders")
        print("3. Compute the income for a driver")
        print("4. Exit")

    def start(self):
        while True:
            self.print_menu()
            choice = input("> ")
            if choice == "1":
                self.addOrder()
            elif choice == "2":
                self.printOrders()
            elif choice == "3":
                self.printIncome()
            elif choice == "4":
                return
            else:
                print("Invalid command!")
