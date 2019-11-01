class Service:
    def _init(self):
        self._expenses = []
    
    def addExpense(self, expense):
        '''
        Add the new expense to the existing ones
        '''
        ok = 1
        if expense.Day < 1 and expense.Day > 30 or isinstance(expense.Day, int) == False:
            raise ValueError("New expense parameters are not valid!")
        self._expenses.append(expense)

    def filterExpenses(self, cmp):
        pass

