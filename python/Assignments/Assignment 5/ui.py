from service import Service
from domain import Expense

class UI:
    def __init__(self, service):
        self._service = service
        self._service.addExpense(Expense(3,200,"water"))
        self._service.addExpense(Expense(2,220,"gas"))
        self._service.addExpense(Expense(20,300,"water"))
        self._service.addExpense(Expense(15,900,"electricity"))
        self._service.addExpense(Expense(23,100,"water"))
        self._service.addExpense(Expense(5,20,"gas"))
        self._service.addExpense(Expense(3,2,"heat"))
        self._service.addExpense(Expense(7,10,"heat"))
        self._service.addExpense(Expense(1,230,"heat"))
        self._service.addExpense(Expense(17,100,"water"))
        self._service._history = []

    def addExpense(self):
        day = input("Input day: ")
        amount = input("Input amount: ")
        type = input("Input type: ")
        try:
            self._service.addExpense(Expense(day,amount,type))
        except ValueError as e:
            print(e)
    
    def filterExpenses(self):
        value = input("Input value: ")
        try:
            self._service.filterExpenses(value)
        except ValueError as e:
            print(e)

    def print_invalid(self):
        print("Invalid command!")

    def print_menu(self):
        print("1. Add a new expense to the list")
        print("2. Show the list of the expenses")
        print("3. Filter the list of the expenses")
        print("4. Undo the last operation")
        print("5. Exit")

    def printExpenses(self):
        print("**********************")
        ok = 0
        for i in self._service._expenses:
            if int(i.Amount) != 0:
                ok = 1
                print(i)
                print(" ")    
        if ok == 0:
            print("There are no expenses in the list!")
        print("**********************")
   
    def undo(self):
        try:
            self._service.undo()
        except ValueError as e:
            print(e)

    def start(self):
        while True:
            self.print_menu()
            choice = input(">")
            if choice == "1":
                self.addExpense()
            elif choice == "2":
                self.printExpenses()
            elif choice == "3":
                self.filterExpenses()
            elif choice == "4":
                self.undo()
            elif choice == "5":
                return
            else:
                self.print_invalid()

