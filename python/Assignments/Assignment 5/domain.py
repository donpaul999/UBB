'''
Manage a list of expenses. Each expense has a day (integer between 1 and 30), amount of money (positive integer) and expense type (string). Provide the user the following features:
    1. Add a new expense read to the list. Expense data is read from the console.
    2. Show the list of expenses on the console.
    3. Filter the list so that it contains only expenses above a certain value that is read from the console.
    4. Undo the last operation that modified program data. This step can be repeated.
'''

class Expense:

    def __init__(self, day, amount, type):
        self.Day = day
        self.Amount = amount
        self.Type = type

    @property
    def Day(self):
        return self._day

    @Day.setter
    def Day(self, value):
        if value > 30 and value < 1 or isinstance(value, int) == False:
            raise ValueError("Expense's day should be an integer between 1 and 30!")
        self._day = value

    @property
    def Amount(self):
        return self._amount

    @Amount.setter
    def Amount(self, value):
        if value < 0 or isinstance(value, int) == False:
            raise ValueError("Amount should be a positive integer!")
        self._amount = value

    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, value):
        self._type = value

    