from domain import Expense

class Service:
    def __init__(self):
        self._expenses = []
    
    def addExpense(self, expense):
       self._expenses.append(expense)

    def filterExpenses(self, cmp):
        pass

