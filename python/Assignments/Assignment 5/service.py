from domain import Expense

class Service:
    def __init__(self):
        self._expenses = []
        self._history = []
        
    def addExpense(self, expense):
       self._expenses.append(expense)

    def filterExpenses(self, cmp):
        pass

    @property
    def Expenses(self):
        return self._expenses

