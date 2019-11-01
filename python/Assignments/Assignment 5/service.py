class Service:
    def _init(self):
        self._expenses = []
    
    def addExpense(self, expense):
        '''
        Add the new expense to the existing ones
        '''
        ok = 1
        if expense.Day < 1 and expense.Day > 30 or expense.amount < 1:
            ok = 0
        if ok == 1:
            for i in range(0, len(expense.Type))
                if(expense.Type[i] >= '0' and expense.Type[i] <= '9')
                    ok = 0
                    break
        if ok == 0
            raise ValueError("New expense parameters are not valid!")
        self._expenses.append(expense)