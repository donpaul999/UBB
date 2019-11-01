from service import Service

class UI:
    def __init__(self, service):
        self._service = service

    def addExpense(self):
        newExpense = None
        self._service.Expense(newExpense)

    def filterExpenses(self):
        pass

    def print_invalid(self):
        print("Invalid command!")

    def print_menu(self):
        print("1. Add a new expense to the list")
        print("2. Show the list of the expenses")
        print("3. Filter the list of the expenses")
        print("4. Undo the last operation")
        print("5. Exit")

    def print_expenses(self):
        pass
    
    def undo(self):
        pass

    def start(self):
        while True:
            self.print_menu()
            choice = input(">")
            if choice == "1":
                self.addExpense()
            elif choice == "2":
                self.print_expenses()
            elif choice == "3":
                self.filterExpenses()
            elif choice == "4":
                self.undo()
            elif choice == "5":
                return
            else:
                self.print_invalid()

s = Service()
ui = UI(s)
ui.start()