class Service:
    def __init__(self):
        self._expenses = []
    
    def addExpense(self, expense):
        '''
        Add the new expense to the existing ones
        '''
        ok = 1
        if expense.Day < 1 and expense.Day > 30 or isinstance(expense.Amount int) == False:
            raise ValueError("New expense parameters are not valid!")
        self._expenses.append(expense)

    def filterExpenses(self, cmp):
        pass

