from service import Service

class UI:
    def _init_(self, service):
        self._service = service

    def addExpense(self):
        newExpense = None
        self._service.Expense(newExpense)

    def filterExpenses(self):
        pass

    def print_menu():
        print("1. Add a new expense to the list")
        print("2. Show the list of the expenses")
        print("3. Filter the list of the expenses")
        print("4. Undo the last operation")

    def start(self):
        print_menu()

s = Service()
ui = UI()
ui.start()
