from domain import Expense
from copy import deepcopy

class Service:
    def __init__(self):
        self._expenses = []
        self._history = []
        
    def addExpense(self, expense):
       self._history.append(deepcopy(self._expenses[:]))
       self._expenses.append(expense)

    def filterExpenses(self, value, x):
        ok = 0
        self._history.append(deepcopy(self._expenses[:]))
        try:
            for i in self._expenses:
                if int(i.Amount) <= int(x):
                    i.Amount = 0
                    ok = 1
        except:
            raise ValueError("The value should be an integer!")
        if ok == 0:
            self._history.pop()

    def printExpenses(self, x):
        for i in self._expenses:
            if int(i.Amount) != 0:
                print(i)

    @property
    def Expenses(self):
        return self._expenses

    def undo(self):
        if len(self._history) == 0:
            raise ValueError("No more undos!")
        self._expenses.clear()
        self._expenses.extend(self._history.pop())
